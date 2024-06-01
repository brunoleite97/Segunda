import random
import json
import torch
from AI.model import NeuralNet
from AI.nltk_utils import bag_of_words, tokenize
from AI.intents_classification import classify_intent
from AI.ner import perform_ner

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('AI/intents.json', 'r', encoding='utf-8') as json_data:
    intents = json.load(json_data)

FILE = "AI/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def chat(user_input: str):
    sentence = tokenize(user_input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return response, prob.item()
    else:
        intent, confidence = classify_intent(user_input)
        if confidence > 0.25:
            entities = perform_ner(query=user_input)
            response = f"Detectei a intenção: {intent} com as entidades: {entities}"
            return response, confidence
        else:
            return "Desculpe, não entendi...", 0.0

if __name__ == "__main__":
    print("Bem-vindo ao Chatbot! Digite 'sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Encerrando o chatbot. Até mais!")
            break
        response, confidence = chat(user_input)
        print(f"Bot: {response} (Confiança: {confidence})")
