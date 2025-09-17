from uuid import uuid4
import os
from agents import (
    Agent,
    handoff,
)
from agents.extensions.models.litellm_model import LitellmModel
from agentic_system.configs.settings import settings
from agentic_system.agents_self.agent_manager import AGENTS, AGENT_DEFINITIONS, AGENT_HANDOFF_DESCRIPTIONS
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX



from agents.model_settings import ModelSettings

import time

"""
Module: master_agent.py

This module defines the AppleMasterAgent class, which orchestrates handoff between device-specific Apple and Sales agents.

Agents:
- iPhoneAgent: Handles queries for iPhone users.
- iPadAgent: Handles queries for iPad users.
- MacBookAgent: Handles queries for MacBook users.
- AirPodsAgent: Handles queries for AirPods users.
- SalesAgent: Handles queries for sales-related topics.
"""
import logging


class MasterAgent:
    """
    AppleMasterAgent orchestrates handoff between the following device-specific agents:
      - iPhoneAgent: Handles queries for iPhone users.
      - iPadAgent: Handles queries for iPad users.
      - MacBookAgent: Handles queries for MacBook users.
      - AirPodsAgent: Handles queries for AirPods users.
      - SalesAgent: Handles queries for sales-related topics.

    This class only provides handoff logic; it does not perform routing decisions.
    """
    def __init__(self, session_id: str = None, context=None):
        self.agent_definitions = AGENT_DEFINITIONS
        self.handoffs = [
            {"agent": AGENTS[agent_name], "description": AGENT_HANDOFF_DESCRIPTIONS[agent_name]}
            for agent_name in self.agent_definitions.keys()
        ]

        agent_names_str = ", ".join([f"{name}: {desc}" for name, desc in self.agent_definitions.items()])
        self.agent = Agent(
            name="AppleAgent",
            instructions=(
                f" {RECOMMENDED_PROMPT_PREFIX} You are the Apple ecosystem router agent. Available agents: {agent_names_str}. "
                "Route queries to the correct Apple device or Sales agent. "
                "If the query is ambiguous or not device-specific, ask for clarification. "
                "Do not mention the handoff process or internal routing logic to the user. "
            ),
            model=LitellmModel(
                model="gemini/gemini-2.5-flash",
                api_key=settings.GEMINI_API_KEY
            ),
            handoffs=[
                handoff(
                    AGENTS[agent_name],
                    tool_description_override=AGENT_HANDOFF_DESCRIPTIONS[agent_name],
                )
                for agent_name in self.agent_definitions.keys()
            ],
            model_settings=ModelSettings(include_usage=True),
        )