
from agents import Runner


from agentic_system.agents_self.master_agent import MasterAgent

from agentic_system.core.session_manager import MyCustomSession

from openai.types.responses import ResponseTextDeltaEvent

import traceback





class AssistantRunner:
    """
    Manages the lifecycle of an agentic conversation using the OpenAI Agents SDK.
    Handles agent selection, context injection, and memory logging.
    """

    def __init__(self, session_id: str, initial_messages=None):
        self.session_id = session_id
        self.session = MyCustomSession(session_id=session_id)
        self.master_agent = MasterAgent(session_id=session_id)



    async def process_user_query(self, user_query: str):
        """
        Accepts a user_query string, runs the agent via Runner, and yields the streamed output.
        The first yielded chunk always contains the agent name.
        """


        prompt = f"user_query: {user_query}"
        result_stream = Runner.run_streamed(self.master_agent.agent, prompt, session=self.session)

        # Buffer events until we know the correct agent name (after agent_updated_stream_event or first raw_response_event)
        agent_name = getattr(self.master_agent.agent, "name", "Agent")
        first_chunk_yielded = False
        buffered_events = []
        tool_names = set()
        try:
            async for event in result_stream.stream_events():
                # Track tool_called events
                if event.type == "run_item_stream_event":
                    if hasattr(event.item, "type") and event.item.type == "tool_called":
                        tool_used = getattr(event.item, "name", None)
                        
                        if tool_used:
                            tool_names.add(tool_used)
                if not first_chunk_yielded:
                    # Buffer events until we see agent_updated_stream_event or raw_response_event
                    if event.type == "agent_updated_stream_event":
                        # print("DEBUG: agent_updated_stream_event", event)
                        agent_name = getattr(event.new_agent, "name", agent_name)
                        # Add all tool names from the agent definition
                        if hasattr(event.new_agent, "tools"):
                            for tool in event.new_agent.tools:
                                tool_names.add(getattr(tool, "name", str(tool)))
                        buffered_events.append(event)
                        continue
                    elif event.type == "run_item_stream_event":
                        if hasattr(event.item, "type") and event.item.type == "tool_called":
                            tool_used = getattr(event.item, "name", None)
                            if tool_used:
                                tool_names.add(tool_used)
                    elif event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                        # Now we know the agent name, yield the first chunk
                        yield {"stream": True, "msg": "", "agent": agent_name, "tool_names": list(tool_names)}
                        first_chunk_yielded = True
                        # Now process this event as normal below
                    else:
                        buffered_events.append(event)
                        continue
                # After first chunk, process all buffered events (if any)
                if buffered_events and first_chunk_yielded:
                    for buffered_event in buffered_events:
                        # Only process raw_response_event for streaming
                        if buffered_event.type == "raw_response_event" and isinstance(buffered_event.data, ResponseTextDeltaEvent):
                            delta = buffered_event.data.delta
                            if delta and isinstance(delta, str):
                                yield {"stream": True, "msg": delta, "agent": agent_name, "tool_names": list(tool_names)}
                    buffered_events = []
                # Now process the current event
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    delta = event.data.delta
                    if delta and isinstance(delta, str):
                        print("DEBUG: tool name delta", tool_names)
                        yield {"stream": True, "msg": delta, "agent": agent_name, "tool_names": list(tool_names)}
        except Exception as e:
            print(f"DEBUG: Exception in agent stream: {e}")
            traceback.print_exc()


