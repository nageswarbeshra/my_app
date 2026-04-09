import requests

def download_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, "wb") as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)