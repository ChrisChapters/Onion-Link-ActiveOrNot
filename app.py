import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def get_hidden_wiki_links():
    url = "https://thehiddenwiki.org/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return links
    else:
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entered_link = request.form["web_address"]
        hidden_wiki_links = get_hidden_wiki_links()

        if entered_link in hidden_wiki_links:
            result = "Valid! The entered link is ACTIVE on TOR."
        else:
            result = "Invalid! The entered link is NOT ACTIVE on TOR."

        return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)