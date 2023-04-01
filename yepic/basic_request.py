import requests

url = "https://api.yepic.ai/v1/videos"

payload = {
    "test": "False",
    "visibility": "public",
    "scenes": [{"assets": [
                {
                    "type": "avatar",
                    "assetId": "0547a65e-6b05-48ee-9b13-63e80e998425",
                    "voiceId": "en-US-JennyMultilingualNeural",
                    "script": "Well done! This is your first video using Yepic's API.",
                    "xPos": 448,
                    "yPos": 52
                }
            ]}],
    "title": "My first video"
}
headers = {
    "content-type": "application/json",
    "Authorization": "23a340b2-5b4e-40cc-9624-0c36a3eb5473"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)