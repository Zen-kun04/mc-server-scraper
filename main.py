import requests
import json

from bs4 import BeautifulSoup
from threading import Thread

PAGES = 5
MIN_PLAYERS = 50
global_servers = []
valid_servers = []


def check_server_players(server: str):
    r = requests.get(f"https://api.mcsrvstat.us/2/{server}")
    body = json.loads(r.text)
    if "players" in body:
        connected_players = int(body["players"]["online"])
        if connected_players >= MIN_PLAYERS:
            valid_servers.append(server)


def make_mcmp_request(page: str):
    headers = {
        'authority': 'minecraft-mp.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://minecraft-mp.com/',
    }

    response = requests.get(f'https://minecraft-mp.com/servers/list/{page}/', headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for x in soup.find_all("button", {"class", "btn btn-default btn-sm clipboard"}):
        server = x.get("data-clipboard-text")
        if server not in global_servers:
            global_servers.append(server)
            Thread(target=check_server_players, args=(server,)).start()


if __name__ == "__main__":
    for page in range(PAGES):
        make_mcmp_request(str(page))
    for server in valid_servers:
        print(server)
