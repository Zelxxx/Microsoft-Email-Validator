import requests

with open("emails.txt", "r") as f:
    emails = f.readlines()

for email in emails:
    email = email.strip()
    url = f"https://login.live.com/?username={email}"
    response = requests.get(url)
    content = response.content.decode()
    if "IfExistsResult\":1" in content:
        print(f"Email {email} does not exist")
    elif "IfExistsResult\":0" in content:
        print(f"Email {email} exists")
        with open('validemails.txt', 'a') as f:
             print(email, file=f)
    else:
        print(f"Rate Limited")




