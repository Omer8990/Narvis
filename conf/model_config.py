import os

import google.generativeai as genai

from conf.setup import API_KEY_ENV_NAME, MODEL_NAME

genai.configure(api_key=os.getenv(API_KEY_ENV_NAME))

_model = genai.GenerativeModel(MODEL_NAME)


def get_model_config():
    return _model
