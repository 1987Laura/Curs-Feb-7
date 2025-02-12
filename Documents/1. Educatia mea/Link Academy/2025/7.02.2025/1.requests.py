import requests

URL = "https://www.link-academy.com"

response = requests.get(URL)

print(response.status_code)
print(response.content)

# old style
file_handler =  open("link-academy.html", "w")
file_handler.write(response.text)
file_handler.close()

# new style

with open("link-academy.html", "w") as file_handler:
    file_handler.write(response.text)