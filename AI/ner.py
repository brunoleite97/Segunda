import spacy
import os

try:
    nlp = spacy.load("pt_core_news_lg")
except:
    print("Downloading spaCy NLP model...")
    os.system("python -m spacy download pt_core_news_lg")
    nlp = spacy.load("pt_core_news_lg")

def perform_ner(*args, **kwargs):
    query = kwargs['query']
    doc = nlp(query)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

if __name__ == "__main__":
    input_text = "Quero comprar um novo iPhone 12 Pro Max da Apple."
    entities = perform_ner(query=input_text)
    print(entities)
