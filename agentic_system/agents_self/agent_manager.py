


from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
from agentic_system.configs.settings import settings

from agentic_system.tools.search_tool import (
	iphone_battery_status_tool,
	iphone_ios_version_tool,
	iphone_camera_specs_tool,
	ipad_screen_size_tool,
	ipad_pencil_compatibility_tool,
	ipad_storage_info_tool,
	macbook_storage_tool,
	macbook_ram_size_tool,
	macbook_macos_version_tool,
	airpods_battery_tool,
	airpods_firmware_version_tool,
	airpods_find_location_tool,
	sales_target_tool,
	sales_leaderboard_tool,
	sales_inventory_tool,
)




def agent_instruction_template(
	agent_name: str,
	role: str,
	supported_scope: str,
	behavior_notes: str = "",
	citation_example: str = "",
	summary: str = "",
):
	return f"""
## {agent_name} – Operational Instructions

**Role:**  
{role}

**Scope:**  
{supported_scope}

**Behavior:**
- Provide accurate information and always clarify user intent if needed.
- Use device-specific logic for responses.
{behavior_notes}

**Response Formatting:**
- Use Markdown formatting for clarity.
- Use bullet points and tables for technical/numerical data.
{citation_example}

**Summary:**  
{summary or "Always provide answers that are detailed, concise, factual, and device-appropriate."}
"""

# iPhoneAgent
IPHONE_AGENT_INSTRUCTIONS = agent_instruction_template(
	agent_name="iPhoneAgent",
	role="Acts as a digital assistant for iPhone users.",
	supported_scope="Answer only using information and tools available for iPhone.",
	behavior_notes="- If the user does not specify a detail, ask for clarification before proceeding.",
	citation_example="Example: The battery status is 80%."
)

# iPadAgent
IPAD_AGENT_INSTRUCTIONS = agent_instruction_template(
	agent_name="iPadAgent",
	role="Acts as a digital assistant for iPad users.",
	supported_scope="Answer only using information and tools available for iPad.",
	behavior_notes="- If the user does not specify a detail, ask for clarification before proceeding.",
	citation_example="Example: The screen size is 11 inches."
)

# MacBookAgent
MACBOOK_AGENT_INSTRUCTIONS = agent_instruction_template(
	agent_name="MacBookAgent",
	role="Acts as a digital assistant for MacBook users.",
	supported_scope="Answer only using information and tools available for MacBook.",
	behavior_notes="- If the user does not specify a detail, ask for clarification before proceeding.",
	citation_example="Example: The available storage is 256GB."
)

# AirPodsAgent
AIRPODS_AGENT_INSTRUCTIONS = agent_instruction_template(
	agent_name="AirPodsAgent",
	role="Acts as a digital assistant for AirPods users.",
	supported_scope="Answer only using information and tools available for AirPods.",
	behavior_notes="- If the user does not specify a detail, ask for clarification before proceeding.",
	citation_example="Example: The left AirPod battery is 90%."
)

# SalesAgent
SALES_AGENT_INSTRUCTIONS = agent_instruction_template(
	agent_name="SalesAgent",
	role="Acts as a digital assistant for sales-related queries.",
	supported_scope="Answer only using information and tools available for sales.",
	behavior_notes="- If the user does not specify a detail, ask for clarification before proceeding.",
	citation_example="Example: The current sales target is $1M."
)







iphone_agent = Agent(
	name="iPhoneAgent",
	instructions=IPHONE_AGENT_INSTRUCTIONS,
	tools=[
		iphone_battery_status_tool,
		iphone_ios_version_tool,
		iphone_camera_specs_tool
	],
	model=LitellmModel(
		model="gemini/gemini-2.5-flash",
		api_key=settings.GEMINI_API_KEY
	)
)





ipad_agent = Agent(
	name="iPadAgent",
	instructions=IPAD_AGENT_INSTRUCTIONS,
	tools=[
		ipad_screen_size_tool,
		ipad_pencil_compatibility_tool,
		ipad_storage_info_tool
	],
	model=LitellmModel(
		model="gemini/gemini-2.5-flash",
		api_key=settings.GEMINI_API_KEY
	)
)





macbook_agent = Agent(
	name="MacBookAgent",
	instructions=MACBOOK_AGENT_INSTRUCTIONS,
	tools=[
		macbook_storage_tool,
		macbook_ram_size_tool,
		macbook_macos_version_tool
	],
	model=LitellmModel(
		model="gemini/gemini-2.5-flash",
		api_key=settings.GEMINI_API_KEY
	)
)





airpods_agent = Agent(
	name="AirPodsAgent",
	instructions=AIRPODS_AGENT_INSTRUCTIONS,
	tools=[
		airpods_battery_tool,
		airpods_firmware_version_tool,
		airpods_find_location_tool
	],
	model=LitellmModel(
		model="gemini/gemini-2.5-flash",
		api_key=settings.GEMINI_API_KEY
	)
)





sales_agent = Agent(
	name="SalesAgent",
	instructions=SALES_AGENT_INSTRUCTIONS,
	tools=[
		sales_target_tool,
		sales_leaderboard_tool,
		sales_inventory_tool
	],
	model=LitellmModel(
		model="gemini/gemini-2.5-flash",
		api_key=settings.GEMINI_API_KEY
	)
)

# Centralized agent mapping
AGENTS = {
	"iPhoneAgent": iphone_agent,
	"iPadAgent": ipad_agent,
	"MacBookAgent": macbook_agent,
	"AirPodsAgent": airpods_agent,
	"SalesAgent": sales_agent,
}

AGENT_NAMES = list(AGENTS.keys())

AGENT_DEFINITIONS = {
	"iPhoneAgent": "Handles queries specifically for iPhone users.",
	"iPadAgent": "Handles queries specifically for iPad users.",
	"MacBookAgent": "Handles queries specifically for MacBook users.",
	"AirPodsAgent": "Handles queries specifically for AirPods users.",
	"SalesAgent": "Handles queries specifically for sales-related topics.",
}

AGENT_HANDOFF_DESCRIPTIONS = {
	"iPhoneAgent": "If the query is about iPhone, hand off to iPhoneAgent.",
	"iPadAgent": "If the query is about iPad, hand off to iPadAgent.",
	"MacBookAgent": "If the query is about MacBook, hand off to MacBookAgent.",
	"AirPodsAgent": "If the query is about AirPods, hand off to AirPodsAgent.",
	"SalesAgent": "If the query is about sales, hand off to SalesAgent.",
}

AGENT_RETURN_DESCRIPTIONS = {
	"iPhoneAgent": "If the query is about iPhone, return the agent name 'iPhoneAgent'.",
	"iPadAgent": "If the query is about iPad, return the agent name 'iPadAgent'.",
	"MacBookAgent": "If the query is about MacBook, return the agent name 'MacBookAgent'.",
	"AirPodsAgent": "If the query is about AirPods, return the agent name 'AirPodsAgent'.",
	"SalesAgent": "If the query is about sales, return the agent name 'SalesAgent'.",
}
