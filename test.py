import requests

if __name__ == "__main__":
    headers = {"User-Agent": "NielsenSVOD",
               "Accept": "*/*"}
    r = requests.get("http://localhost:7878", headers=headers)
    print(r.status_code)
