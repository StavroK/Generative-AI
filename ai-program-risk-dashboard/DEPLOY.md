# Deploy the AI Program Risk Dashboard

## Streamlit Community Cloud

This app is structured for direct deployment from GitHub.

### Repository
`StavroK/Generative-AI`

### Main file path
`ai-program-risk-dashboard/app.py`

### Python dependencies
`ai-program-risk-dashboard/requirements.txt`

## Deployment steps
1. Sign in to Streamlit Community Cloud with GitHub.
2. Choose **Create app**.
3. Select repository `StavroK/Generative-AI`.
4. Select branch `main`.
5. Set main file path to:
   `ai-program-risk-dashboard/app.py`
6. Deploy.

## Expected app
The dashboard displays:
- active initiatives;
- portfolio health;
- approved vs. forecast budget;
- schedule variance;
- GenAI operational metrics;
- portfolio risks and executive attention.

## Production note
The current dashboard uses fictional CSV data intentionally. A production version should source a governed system of record such as Jira, ServiceNow SPM, Smartsheet, Azure DevOps, or a controlled data warehouse.
