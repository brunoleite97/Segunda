import wikipedia
import re
import spacy
import os

def tell_me_about(*args, **kwargs):
    entities = kwargs.get("entities")
    if len(entities) == 0:
        return "Entity not found"
    
    li = ['EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG',
          'PERCENT', 'PERSON', 'PRODUCT', 'TIME', 'WORK_OF_ART']
    
    topics = [entity[0] for entity in entities if entity[1] in li]
    
    if not topics:
        return "No relevant entities found"
    
    topic = topics[0]
    
    try:
        ny = wikipedia.page(topic)
        res = str(ny.content[:500].encode('utf-8'))
        res = re.sub(r'[^a-zA-Z.\d\s]', '', res)[1:]
        return res
    except Exception as e:
        print(e)
        return "An error occurred while fetching the Wikipedia page"

def perform_ner(*args, **kwargs):
    query = kwargs['query']
    doc = nlp(query)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

if __name__ == '__main__':
    try:
        nlp = spacy.load("pt_core_news_lg")
    except:
        print("Downloading spaCy NLP model...")
        print("This may take a few minutes and it's a one-time process...")
        os.system("python -m spacy download pt_core_news_lg")
        nlp = spacy.load("pt_core_news_lg")

    query = "Conte me sobre Hugh Jackeman"
    entities = perform_ner(query=query)

    print(tell_me_about(query=query, entities=entities))
