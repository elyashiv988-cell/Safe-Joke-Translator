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

def translate_joke(joke, target_lang, key):
    
    try:
        deepl_client = deepl.DeepLClient(key)
        result = deepl_client.translate_text(joke, target_lang)
        data = result.text
        hebrew_joke  = get_display(data)
        return hebrew_joke
    except:
        print("The joke was received, but it could not be translated.")
        return joke






    

