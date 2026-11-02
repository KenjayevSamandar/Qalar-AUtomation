import requests

javob = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status code:", javob.status_code)

malumot = javob.json()
print("ID:", malumot["id"])
print("Sarlavha:", malumot["title"])
print("UserId:", malumot["userId"])