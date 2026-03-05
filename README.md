# Houseplant MD

Doctor Houseplant, your friendly botanist and experienced gardener.
Here to help you identify your plants and provide you with all the knowledge
you need to nurture and maintain them in tip-top health.

This agent was developed using the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

## Usage

A [devcontainer](https://containers.dev/)
definition will install the necessary dependencies. Refer to the
[Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563)
course for step by step configuration details.

This example uses Gemini API via Google AI Studio (recommended for personal
learning).

After cloning the repo locally, start VS Code and open the project
in the devcontainer. Also ensure the venv (`.venv`) is activated.

You'll need an API Key:

- Visit [Google Studio](https://aistudio.google.com/apikey)
- Sign in with your Google account
- Click **Create API Key**
- Copy the API key (it looks like `AIzaSyC...`)

Create your local `.env` file:

```bash
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=AIzaSyC...
```

You're now ready to start the ADK Web Server

```bash
cd src
adk web
```

For local testing and development, access `http://127.0.0.1:8000`.
Use the web interface to check the examples, you can make changes and iterate
(either using Agent builder or in the `.py` source).

Other useful commands are:

- `adk run`, terminal-based interaction
- `adk api_server`, deploy as an API Service

## References

Online Documentation

- [Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- [Google Search Tool for ADK](https://google.github.io/adk-docs/tools/gemini-api/google-search/)
- [Structuring Data with ADK](https://google.github.io/adk-docs/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key)
- [Sequential Agents](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/)

Courses, Labs and Tutorials

- [Understand Google Cloud Agents](https://www.skills.google/course_templates/1504)
- [Build your first agent with Agent Development Kit (ADK)](https://www.skills.google/course_templates/1563)
- [Build intelligent agents with the Agent Development Kit (ADK)](https://www.skills.google/course_templates/1382)
