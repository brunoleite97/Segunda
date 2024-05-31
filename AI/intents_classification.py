import os
import json

def check_local_intent(text):
    try:
        if not os.path.exists('actions.json'):
            return None
        else:
            with open('actions.json', 'r', encoding='utf-8') as f:
                actions = json.load(f)
            for action in actions:
                if text in action['example']:
                    return action['intent']
                if action['intent'] in text:
                    return action['intent']
                if action['example'] == "":
                    continue
    except Exception as e:
        return None

def classify_intent(text):
    intent = check_local_intent(text)
    if intent is not None:
        return intent, 1.0
    return "unknown", 0.0

if __name__ == "__main__":
    intent, _ = classify_intent("olá")
    print(intent, _)
