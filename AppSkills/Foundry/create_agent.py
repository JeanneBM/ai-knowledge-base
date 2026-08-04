import os

from dotenv import load_dotenv

load_dotenv()

import openai
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    CodeInterpreterTool,
    PromptAgentDefinition,
    WebSearchApproximateLocation,
    WebSearchTool,
)

project_endpoint = os.environ.get("FOUNDRY_PROJECT_ENDPOINT")
agent_name = os.environ.get("FOUNDRY_AGENT_NAME")
model_name = os.environ.get("FOUNDRY_MODEL_NAME")

project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(
        exclude_managed_identity_credential=True
    ),
)

with project_client:
    print(
        f"Connected to project. Creating a new version for agent: "
        f"{agent_name}..."
    )

    # TODO 1.2: Add instructions.
    new_instructions = (
        "Summarize each support request in exactly two concise sentences. "
        "Return only the summary without any additional commentary."
    )

    # TODO 2.1 Initialize the code interpreter tool.
    # code_interpreter =

    # TODO 2.2 Initialize web search tool.
    # web_search = xxx(
    #     # TODO 2.3 Add the user location web search.
    #     # user_location=
    # )

    try:
        # TODO 1.3 Call the appropriate function.
        new_agent_version = project_client.agents.create_version(
            agent_name=agent_name,

            # TODO 1.4 Add a description.
            description="Agent that summarizes support requests.",

            definition=PromptAgentDefinition(
                # TODO 1.5 Specify which model to use.
                model=model_name,

                # TODO 1.6 Specify the instructions.
                instructions=new_instructions,

                # TODO 2.4 Attach the configured toolset to Agent1.
                # tools=
            ),
        )

        print("\n✅ Agent updated successfully!")
        print(f"Agent Name: {new_agent_version.name}")
        print(f"New Version: {new_agent_version.version}")

        # TODO 2.5 Test the user input.
        user_input = (
            "The customer cannot log in to the application after resetting "
            "their password. They receive an invalid credentials error."
        )

        openai_client = project_client.get_openai_client()

        response = openai_client.responses.create(
            input=user_input,
            extra_body={
                "agent_reference": {
                    "name": new_agent_version.name,
                    "type": "agent_reference",
                }
            },
        )

        print("\nResponse:")
        print(response.output_text)

    except Exception as e:
        print(f"\n❌ Failed to update agent. Error: {e}")
