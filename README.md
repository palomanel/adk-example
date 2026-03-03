# adk-example

A project template and examples to get you started with the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

With the ADK you can develop agents using:

- YAML-based configuration (i.e [Agent Builder](https://google.github.io/adk-docs/agents/config/))
- [Python](https://google.github.io/adk-docs/get-started/java/)
- [TypeScript](https://google.github.io/adk-docs/get-started/typescript/)
- [Go](https://google.github.io/adk-docs/get-started/go/)
- [Java](https://google.github.io/adk-docs/get-started/java/)

In the project Agent Builder and Python are used.

A [devcontainer](https://containers.dev/)
definition will install the necessary dependencies. Refer to the
[Build Your First Agent with Agent Development Kit (ADK)](https://www.skills.google/paths/3545/course_templates/1563)
course for step by step configuration details.

## Usage

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
