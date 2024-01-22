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
- create and activate python virtual environment
  - `python3 -m venv .venv`
  - `. .venv/bin/activate`
- install flask
  - `pip install Flask`
- install langchain
  - `pip install langchain`
  - `pip install langchain-openai`
- get openai api key from https://platform.openai.com/api-keys, 
save it under   
  - `haikuapp/llm/vault/openai`
- Initialize db. From parent directory of `haikuapp`, run
  - `flask --app haikuapp init-db`
- start app
  - `flask --app haikuapp run`

# demo
- ai response to user haiku
![reponse_before_submit](/demo/response_before_submit.png)
![response_after_subimt](/demo/response_after_submit.png)

- ai haiku generator
![generator_before_submit](/demo/generator_before_submit.png)
![generator_after_submit](/demo/generator_after_submit.png)