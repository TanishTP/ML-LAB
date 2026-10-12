
import requests

n = input("Enter program number (1-9): ")

if n == "6":
    n = input("Enter A for Linear Regression or B for Polynomial Regression: ").upper()
    filename = f"P6{n}.txt"
else:
    filename = f"P{n}.txt"

url = f"https://raw.githubusercontent.com/TanishTP/ML-Lab/main/{filename}"

response = requests.get(url, timeout=15)

if response.status_code == 200:
    with open(filename.replace(".txt", ".py"), "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Downloaded successfully:", filename.replace(".txt", ".py"))
else:
    print("File not found. Check the filename and repository.")
