import spacy
import numpy as np

nlp = spacy.load('en_core_web_sm')

def extract_features(text):
    doc = nlp(text)
    return np.array([token.vector for token in doc if token.has_vector])

if __name__ == "__main__":
    sample_text = 'This is a sample text for feature extraction.'
    features = extract_features(sample_text)
    print(features)
