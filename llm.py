import sys,os,os.path
from langchain_openai import ChatOpenAI
from . import err
from flask import flash


p = __file__.split("/")
p = '/'.join(p[:-1]) + '/llm/vault/openai'
key = open(p, "r").read()
os.environ['OPENAI_API_KEY']= key

# TODO: bring config under llm/config.json
# config = {"model_name": 'gpt-3.5-turbo-16k', 'openai_api_key': key}

llm_openai = ChatOpenAI(openai_api_key=key)

def invoke(input):
    res = ""
    try:
        res = llm_openai.invoke(input)
    except:
        flash(err.llmRateLimit)
        return
    return res.content

if __name__ == '__main__':
    key = open("llm/vault/openai", "r").read()
    print(key)
    # res = llm_openai.invoke("generate a haiku")
    # prefix = "comment on this haiku: "
    # haiku = "i live in a castle of my own make-believe. \
    #          i am here, inside the castle, delusional. \
    #          she is there, outside the castle, unreachable."
    # res = llm_openai.invoke(prefix + haiku)
    # print(type(res))
    # print(res.content)