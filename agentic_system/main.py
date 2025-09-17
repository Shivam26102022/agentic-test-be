
# Full-featured FastAPI backend for agentic system
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import traceback
from agentic_system.agents_self.agent_manager import AGENTS, AGENT_NAMES
from pydantic import BaseModel

from agentic_system.core.agent_runner import AssistantRunner
import asyncio

app = FastAPI()

# Allow CORS for local dev/testing
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
	return {"status": "ok", "message": "Agentic system backend running."}

# WebSocket endpoint for agentic routing
@app.websocket("/ws")
async def websocket_router(websocket: WebSocket):
	await websocket.accept()
	try:
		while True:
			data = await websocket.receive_json()
			agent_name = data.get("agent")
			query = data.get("query")
			if agent_name not in AGENTS:
				await websocket.send_json({"error": f"Unknown agent: {agent_name}"})
				continue
			agent = AGENTS[agent_name]
			runner = AssistantRunner("session_id")
			output = []
			tool_names = set()
			agent_name_from_response = None
			first_chunk = True
			async for chunk in runner.process_user_query(query):
				if isinstance(chunk, dict):
					if first_chunk:
						agent_name_from_response = chunk.get("agent", agent_name)
						tool_names.update(chunk.get("tool_names", []))
						first_chunk = False
						continue
					tool_names.update(chunk.get("tool_names", []))
					if "msg" in chunk:
						output.append(chunk["msg"])
			if agent_name_from_response is None:
				agent_name_from_response = agent_name
			tool_names_str = ", ".join(tool_names) if tool_names else "none"
			response_text = f"{agent_name_from_response}({tool_names_str}): " + "".join(output)
			await websocket.send_json({
				"status": "ok",
				"agent": agent_name_from_response,
				"query": query,
				"llm_response": response_text
			})
	except WebSocketDisconnect:
		pass

# HTTP endpoint to invoke an agent/tool directly
@app.post("/invoke-agent")
async def invoke_agent(request: Request):
	data = await request.json()
	agent_name = data.get("agent")
	payload = data.get("payload", {})
	if agent_name not in AGENTS:
		return JSONResponse({"error": f"Unknown agent: {agent_name}"}, status_code=400)
	agent = AGENTS[agent_name]
	tool = agent.handler[0] if isinstance(agent.handler, list) else agent.handler
	try:
		# For demo, just call the tool with no args (expand as needed)
		result = await tool()
		return {"agent": agent_name, "result": result}
	except Exception as e:
		return JSONResponse({"error": str(e), "trace": traceback.format_exc()}, status_code=500)


# Test payload endpoint
@app.get("/test-payload")
async def test_payload():
	"""Simple endpoint to check payload routing."""
	return JSONResponse({"status": "ok", "message": "Test payload received."})

# Test query endpoint (POST, accepts JSON body with 'query')

class QueryRequest(BaseModel):
	query: str

@app.post("/test-query")
async def test_query(request: QueryRequest):
	"""Endpoint to test submitting a query string and get LLM/agent response."""
	# Use the first available agent as default
	agent_name = next(iter(AGENTS))
	agent = AGENTS[agent_name]
	runner = AssistantRunner("session_id")
	output = []
	tool_names = set()
	agent_name_from_response = None
	first_chunk = True
	async for chunk in runner.process_user_query(request.query):
		if isinstance(chunk, dict):
			if first_chunk:
				agent_name_from_response = chunk.get("agent", agent_name)
				tool_names.update(chunk.get("tool_names", []))
				first_chunk = False
				continue
			tool_names.update(chunk.get("tool_names", []))
			if "msg" in chunk:
				output.append(chunk["msg"])
	if agent_name_from_response is None:
		agent_name_from_response = agent_name
	tool_names_str = ", ".join(tool_names) if tool_names else "none"
	print("tool_names_str", tool_names_str)
	print("output", output)
	response_text = f"{agent_name_from_response}({tool_names_str}): " + "".join(output)
	return JSONResponse({
		"status": "ok",
		"agent": agent_name_from_response,
		"query": request.query,
		"llm_response": response_text
	})

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
