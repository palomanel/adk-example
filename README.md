# adk-example

A Python example agent using the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

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
source .
cd src
adk web
```

For local testing, access at `http://127.0.0.1:8000`.
