"""
import json
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool, WebSearchTool
from openai.types.responses.response_input_param import (
    MCPApprovalResponse,
    ResponseInputParam,
)

# TODO 3.1: Provide project endpoint.
PROJECT_ENDPOINT = ""

# Create clients to call Foundry API
project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True,
        exclude_workload_identity_credential=True,
        exclude_shared_token_cache_credential=True,
    ),
)

openai = project.get_openai_client()

print("1. Created project client.")

# [Start Toolbox creation]
# TODO 3.2: Implement the correct method.
my_toolbox = project.beta.toolboxes.(
    name="OperationsToolbox",
    description="Toolbox with web search and an MCP server",
    tools=[
        # TODO 3.3 Add the Microsoft Learn MCP Server.
        # TODO 3.4 Add the Azure Functions MCP.
    ],
)
# [End Toolbox creation]

print("2. Created toolbox.")

# Create a prompt agent with MCP tool capabilities
agent = project.agents.create_version(
    agent_name="Agent2",
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="Use MCP tools as needed",
        # TODO 3.5 Connect to the toolbox Tools.
        tools=[],
    ),
)

print(
    f"Agent created (id: {agent.id}, name: {agent.name}, "
    f"version: {agent.version})"
)

# Create a conversation to maintain context across multiple interactions
conversation = openai.conversations.create()
print(f"Created conversation (id: {conversation.id})")

# Send initial request that will trigger the MCP tool
response = openai.responses.create(
    conversation=conversation.id,
    input="What incidents are currently active in our system?",
    extra_body={
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference",
        }
    },
)

# Process any MCP approval requests that were generated
input_list: ResponseInputParam = []

for item in response.output:
    if item.type == "mcp_approval_request" and item.id:
        print("MCP approval requested")
        print(f"  Server: {item.server_label}")
        print(f"  Tool: {getattr(item, 'name', '<unknown>')}")
        print(
            f"  Arguments: "
            f"{json.dumps(getattr(item, 'arguments', None), indent=2, default=str)}"
        )

        # Approve only after you review the tool call.
        # In production, implement your own approval UX and policy.
        should_approve = (
            input("Approve this MCP tool call? (y/N): ")
            .strip()
            .lower()
            == "y"
        )

        input_list.append(
            MCPApprovalResponse(
                type="mcp_approval_response",
                approve=should_approve,
                approval_request_id=item.id,
            )
        )

# Send the approval response back to continue the agent's work
response = openai.responses.create(
    input=input_list,
    previous_response_id=response.id,
    extra_body={
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference",
        }
    },
)

print(f"Response: {response.output_text}")
"""
import json
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition, MCPTool, WebSearchTool
from openai.types.responses.response_input_param import (
    MCPApprovalResponse,
    ResponseInputParam,
)

# TODO 3.1: Provide project endpoint.
PROJECT_ENDPOINT = "https://user1-63908861-resource.services.ai.azure.com/api/projects/project-63908861"

# Create clients to call Foundry API
project = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(
        exclude_environment_credential=True,
        exclude_managed_identity_credential=True,
        exclude_workload_identity_credential=True,
        exclude_shared_token_cache_credential=True,
    ),
)

openai = project.get_openai_client()

print("1. Created project client.")

# [Start Toolbox creation]
# TODO 3.2: Implement the correct method.
my_toolbox = project.beta.toolboxes.create_version(
    name="OperationsToolbox",
    description="Toolbox with web search and an MCP server",
    tools=[
        # TODO 3.3 Add the Microsoft Learn MCP Server.
        MCPTool(
            server_label="MicrosoftLearnMCPServer",
            server_url="https://learn.microsoft.com/api/mcp",
            require_approval="never",
        ),
        # TODO 3.4 Add the Azure Functions MCP.
        MCPTool(
            server_label="IncidentsMCP",
            server_url="https://function63908B61-gkhwfgdag9bfbzb2.australiaeast-01.azurewebsites.net/runtime/webhooks/mcp",
            require_approval="never",
            project_connection_id="IncidentsMCP",
        ),
    ],
)
# [End Toolbox creation]

print("2. Created toolbox.")

# Create a prompt agent with MCP tool capabilities
agent = project.agents.create_version(
    agent_name="Agent2",
    definition=PromptAgentDefinition(
        model="gpt-5-mini",
        instructions="Use MCP tools as needed",
        # TODO 3.5 Connect to the toolbox Tools.
        tools=[
            MCPTool(
                server_label="OperationsToolbox",
                server_url=f"{PROJECT_ENDPOINT}/toolboxes/OperationsToolbox/mcp?api-version=v1",
                require_approval="never",
            ),
        ],
    ),
)

print(
    f"Agent created (id: {agent.id}, name: {agent.name}, "
    f"version: {agent.version})"
)

# Create a conversation to maintain context across multiple interactions
conversation = openai.conversations.create()
print(f"Created conversation (id: {conversation.id})")

# Send initial request that will trigger the MCP tool
response = openai.responses.create(
    conversation=conversation.id,
    input="What incidents are currently active in our system?",
    extra_body={
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference",
        }
    },
)

# Process any MCP approval requests that were generated
input_list: ResponseInputParam = []

for item in response.output:
    if item.type == "mcp_approval_request" and item.id:
        print("MCP approval requested")
        print(f"  Server: {item.server_label}")
        print(f"  Tool: {getattr(item, 'name', '<unknown>')}")
        print(
            f"  Arguments: "
            f"{json.dumps(getattr(item, 'arguments', None), indent=2, default=str)}"
        )

        # Approve only after you review the tool call.
        # In production, implement your own approval UX and policy.
        should_approve = (
            input("Approve this MCP tool call? (y/N): ")
            .strip()
            .lower()
            == "y"
        )

        input_list.append(
            MCPApprovalResponse(
                type="mcp_approval_response",
                approve=should_approve,
                approval_request_id=item.id,
            )
        )

# Send the approval response back to continue the agent's work
response = openai.responses.create(
    input=input_list,
    previous_response_id=response.id,
    extra_body={
        "agent_reference": {
            "name": agent.name,
            "type": "agent_reference",
        }
    },
)

print(f"Response: {response.output_text}")
