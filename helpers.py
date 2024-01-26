from base64 import standard_b64decode, standard_b64encode
from datetime import datetime

import pytz
import requests

def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode("ascii")
    bytes_b64 = standard_b64encode(str_bytes)
    b64 = bytes_b64.decode("ascii")
    return b64


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode("ascii")
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode("ascii")
    return __str


def get_current_time():
    tz = pytz.timezone("Asia/Kolkata")
    return int(datetime.now(tz).timestamp())


def shorten_url(url):
    site_url = f"https://gplinks.in//api?api=0208c5e8afe718af4a0d9d2b41f7070cd3dc108b&url={url}&format=text"
    return str(requests.get(site_url).text)

def shorten_urll(url):
    site_url = f"https://filesendxbot.link/api?api=011be3b5ecc730204b9863e29c3af7df5525d3c5&url={url}&format=text"
    return str(requests.get(site_url).text)
