import sys,os,os.path
key = "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"
os.environ['OPENAI_API_KEY']= key

from langchain_openai import ChatOpenAI
from . import err
from flask import flash


config = {"model_name": 'gpt-3.5-turbo-16k', 'openai_api_key': key}

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
    # res = llm_openai.invoke("generate a haiku")
    prefix = "comment on this haiku: "
    haiku = "i live in a castle of my own make-believe. \
             i am here, inside the castle, delusional. \
             she is there, outside the castle, unreachable."
    res = llm_openai.invoke(prefix + haiku)
    print(type(res))
    print(res.content)