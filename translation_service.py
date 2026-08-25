import os
import dotenv
import deepl
from bidi.algorithm import get_display

def get_key():

    if os.path.exists(".env"):
        dotenv.load_dotenv(".env")
        key = os.getenv("KEY")
        return key

    else:
        print(".env file doesn't found!")

def translate_joke(joke, target_language):
    try:
        key = get_key()
        deepl_client = deepl.DeepLClient(key)
        result = deepl_client.translate_text(joke, target_lang= target_language)
        data = result.text
        if target_language == "HE":
            data  = get_display(data)
        return data
    except:
        print("The joke was received, but it could not be translated.")
        return joke





    

