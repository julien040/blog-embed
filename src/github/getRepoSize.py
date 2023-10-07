from streamlit import cache_data
from requests import get
from urllib.parse import urlparse


@cache_data(ttl=60*60*2)
def getRepoSize(url: str):
    parsedURL = urlparse(url)

    if parsedURL.netloc != "github.com":
        raise Exception("Invalid URL")
    if parsedURL.path == "":
        raise Exception("Invalid URL")

    repoURL = f"https://api.github.com/repos{parsedURL.path}"
    response = get(repoURL)
    if response.status_code != 200:
        raise Exception("Invalid URL")

    repoData = response.json()
    return int(repoData["size"]*1024)
