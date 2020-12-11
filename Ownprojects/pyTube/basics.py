import pytube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"
try:
    youtube = pytube.YouTube(url)
except KeyError:
    cipher_url = [
### parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
    (lambda i,data: [ parse_qs(data[k]) for k in ("cipher","signatureCipher") if k in data ])(i, data) for i, data in enumerate(formats)
    ]
print(youtube.title)
