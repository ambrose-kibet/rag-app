from src.config import Config
import requests


def get_my_trello_boards():

    url = "https://api.trello.com/1/members/me/boards"
    querystring = {
        "key": Config.TRELLO_API_KEY,
        "token": Config.TRELLO_TOKEN,
    }
    response = requests.request("GET", url, params=querystring)
    res = response.json()

    return [board["id"] for board in res]


def get_my_trello_cards(board_id: str):

    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    querystring = {
        "key": Config.TRELLO_API_KEY,
        "token": Config.TRELLO_TOKEN,
        "fields": "name,desc",
    }
    response = requests.request("GET", url, params=querystring)
    cards = response.json()
    cards = response.json()
    return {
        "board_id": board_id,
        "count": len(cards),
        "cards": [{"title": c["name"], "description": c["desc"]} for c in cards],
    }
