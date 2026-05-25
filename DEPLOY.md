# Deployment Guide

This guide explains how to deploy DocuExtract-AI to the **Streamlit Community Cloud**.

## Streamlit Community Cloud (Recommended)

Streamlit Community Cloud is the easiest way to deploy this app directly from your GitHub repository.

### Prerequisites
1. Your repository must be public (or you need a premium Streamlit account for private repos).
2. The code must be pushed to GitHub.

### Deployment Steps
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click **New app**.
3. Select your repository, branch, and set the **Main file path** to `app.py`.
4. Click on **Advanced settings** before deploying!
5. In the **Secrets** section, configure the necessary environment variables (see below).
6. Click **Deploy!**

### Required Environment Variables (Secrets)
You must set the following variables in the Streamlit Cloud dashboard under "Advanced settings > Secrets" in TOML format:

```toml
# Your Google Gemini API Key
GEMINI_API_KEY = "your_actual_api_key_here"

# (Optional) Set to "true" ONLY if you want to bypass the LLM and use mock data for a live demo
# MOCK_LLM = "false"
```

*Note: Streamlit Community Cloud will automatically detect your `requirements.txt` and install all required packages (PyPDF2, pydantic, streamlit, google-generativeai, python-dotenv).*
