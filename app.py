# import time

# import redis
# from flask import Flask

# app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return 'Hello World! I have been seen {} times.\n'.format(count)
# import redis
# from flask import Flask

# app = Flask(__name__)
# cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     return cache.incr('hits')

# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return 'Hello World! I have been seen {} times.\n'.format(count)


#oepnAPI Key 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

# import os
# import openai
# openai.organization = "org-KOnnLWJP5kUmNw0GwuxVT9DV"
# openai.Model.list()

import openai
import os
import IPython
from langchain.llms import OpenAI
from dotenv import load_dotenv


# curl https://api.openai.com/v1/models \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "OpenAI-Organization: org-KOnnLWJP5kUmNw0GwuxVT9DV"
