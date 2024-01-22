# Haiku Web App
A small haiku web app that allow users to put in their haiku and get feedback from our AI, or to receive AI-generated haiku.

# dependencies
- python3
- flask
  - check https://flask.palletsprojects.com/en/3.0.x/installation/ for dependencies of flask
- langchain
  - openAI api key: https://platform.openai.com/api-keys

# to run the app (in linux terminal)
- save a local copy of this repo
- install python3
- install flask
  - `pip install Flask`
- install langchain
  - `pip install langchain`
  - `pip install langchain-openai`
- get openai api key from https://platform.openai.com/api-keys, save it under `haikuapp/llm/vault/openai`
- create python virtual environment
  - `python3 -m venv .venv`
  - `. .venv/bin/activate`