import sys,os,os.path
key = "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"
os.environ['OPENAI_API_KEY']= key

from langchain_openai import ChatOpenAI

config = {"model_name": 'gpt-3.5-turbo-16k', 'openai_api_key': key}

llm_openai = ChatOpenAI(openai_api_key=key)


if __name__ == '__main__':
    res = llm_openai.invoke("generate a haiku")
    print(type(res))
    print(res.content)