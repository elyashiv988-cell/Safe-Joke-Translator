import requests

def get_joke():
    base_uml = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw&type=single"
    response = requests.get(base_uml)
    joke_data = response.json()
    return joke_data

def is_safe_joke(joke_data):
    try:
        if joke_data["error"] != False:
            return False
        if joke_data["type"] !="single":
            return False
        if len(joke_data["joke"]) == 0:
            return False
        for flag in joke_data['flags']:
            if joke_data["flags"][flag] != False:
                return False
        return True
    except KeyError:
        return False

def get_safe_joke():

    for i in range(3):
        joke = get_joke()
        if is_safe_joke(joke):
            return joke

    return None

def extract_joke_data(api_data):
    joke_dict = {"joke": api_data["joke"],
                "category": api_data["category"],
                "joke_id": api_data["id"],
                "language": api_data["lang"]
                }
    return joke_dict

def analyze_joke(joke):
    analyze_data={"chars": 0, "words": 0}
    words = joke["joke"].split(" ")
    for word in words:
        analyze_data["words"] += 1
        for char in word:
            analyze_data["chars"] += 1
    
    return analyze_data

    

        
        


