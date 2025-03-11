import gradio as gr, os, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI()

openai_key = os.getenv("OPENAI_API_KEY")
model = 'gpt-4o'

sys_prompt = 'You are an AI assistant that is involved with a store called Daniels Clothings'
sys_prompt += 'Your focus should be on Daniels Store and nothing else, if user ask a question not regarding Daniel Clothings\
    politely ask them to ask you about Daniels Clothings'
sys_prompt += 'You should always explain what Daniels Clothings does so the customer understands your duty.'
sys_prompt += 'Your main focus should be convincing the customers to buy at least one kit before they go, \
    either through humor or offering a bargain, like the cheapest one in stock'
sys_prompt += 'Always look through the whole inventory in the tools list to know the kit and the price and also offer customers less popular and cheap kits'
sys_prompt += 'If the customer agrees to buy, generate a random 4 digit code and tell them to email their address to efereprecious@gmail.com to get their delivery started'

football_kits = {
    "arsenal": 45, "liverpool": 56, "manchester city": 129, "chelsea": 89,
    "manchester united": 99, "tottenham hotspur": 75, "leicester city": 65,
    "west ham united": 70, "everton": 60, "aston villa": 55, "newcastle united": 50,
    "wolverhampton wanderers": 59, "crystal palace": 54, "southampton": 49,
    "brighton & hove albion": 53, "leeds united": 58, "burnley": 47,
    "fulham": 52, "west bromwich albion": 48, "sheffield united": 46,
    "real madrid": 150, "barcelona": 145, "atletico madrid": 120,
    "sevilla": 95, "villarreal": 85, "real sociedad": 80, "real betis": 75,
    "athletic bilbao": 70, "valencia": 65, "granada": 60, "celta vigo": 55,
    "getafe": 50, "osasuna": 49, "cadiz": 48, "alaves": 47, "levante": 46,
    "eibar": 45, "valladolid": 44, "elche": 43, "huesca": 42, "juventus": 130,
    "inter milan": 125, "ac milan": 120, "napoli": 110, "atalanta": 100,
    "roma": 95, "lazio": 90, "sassuolo": 80, "sampdoria": 75, "fiorentina": 70,
    "torino": 65, "udinese": 60, "bologna": 55, "genoa": 50, "cagliari": 49,
    "parma": 48, "spezia": 47, "benevento": 46, "crotone": 45, "verona": 44,
    "bayern munich": 140, "borussia dortmund": 130, "rb leipzig": 120,
    "bayer leverkusen": 100, "borussia monchengladbach": 95, "wolfsburg": 90,
    "eintracht frankfurt": 85, "hoffenheim": 80, "hertha berlin": 75,
    "schalke 04": 70, "freiburg": 65, "augsburg": 60, "mainz 05": 55,
    "cologne": 50, "union berlin": 49, "stuttgart": 48, "arminia bielefeld": 47,
    "werder bremen": 46, "paris saint-germain": 160, "lyon": 110, "marseille": 100,
    "lille": 95, "monaco": 90, "rennes": 85, "nice": 80, "montpellier": 75,
    "saint-etienne": 70, "bordeaux": 65, "lens": 60, "nantes": 55,
    "strasbourg": 50, "reims": 49, "angers": 48, "brest": 47, "metz": 46,
    "dijon": 45, "nimes": 44, "lorient": 43, "lens": 42
}

def get_football_kit_price(kit_name):
    print(f"Tool get_football_kit_price called for {kit_name}")
    kit = kit_name.lower()
    return football_kits.get(kit, "Unknown")

get_football_kit_price('Liverpool')

kit_price = {
  "name": "get_football_kit_price",
  "description": "Get the price of a football club kit",
  "parameters": {
    "type": "object",
    "properties": {
      "kit_name": {
        "type": "string",
        "description": "The name of the football club kit"
      }
    },
    "required": ["kit_name"],
    "additionalProperties": False
  }
}

tools = [{'type':'function', 'function':kit_price}]
