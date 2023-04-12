import re
import requests
from bs4 import BeautifulSoup

# URL du quiz Google Forms
url = "https://docs.google.com/forms/d/e/1FAIpQLScHhKtEpWc8Jyv9nOShKj-0HHBVwpMMmTWmyrbOxTTRT72Y2Q/viewform"

# Extraire le texte brut de la page
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.get_text()


# Fonction pour détecter les questions
def detect_questions(text):
    questions = []
    pattern = r"(\d+\..+\?)"
    matches = re.findall(pattern, text)
    for match in matches:
        question = match.strip()
        questions.append(question)
    return questions


# Fonction pour détecter les réponses
def detect_responses(text):
    responses = []
    pattern = r"\n([A-Z]\..+)"
    matches = re.findall(pattern, text)
    for match in matches:
        response = match.strip()
        responses.append(response)
    return responses


# Détecter les questions et les réponses dans le quiz
questions = detect_questions(text)
responses = detect_responses(text)

# Afficher les résultats
print("Questions : ")
for question in questions:
    print(question)

print("Réponses : ")
for response in responses:
    print(response)