# Import libraries
from typing import Collection
import nltk
from nltk.corpus import stopwords
from gensim.models import TfidfModel

# Define functions for preprocessing and similarity calculation
def preprocess_text(text):
  tokens = nltk.word_tokenize(text)
  tokens = [t for t in tokens if t not in stopwords.words("english")]
  stemmer = nltk.PorterStemmer()
  tokens = [stemmer.stem(t) for t in tokens]
  return tokens

def calculate_similarity(text1, text2):
  # Preprocess text
  tokens1 = preprocess_text(text1)
  tokens2 = preprocess_text(text2)

  # Create TF-IDF model
  dictionary = Collection.defaultdict(int)
  for token in tokens1 + tokens2:
    dictionary[token] += 1
  model = TfidfModel([dictionary])

  # Convert texts to vectors
  vec1 = model[tokens1]
  vec2 = model[tokens2]

  # Calculate cosine similarity
  similarity_score = vec1.dot(vec2) / (vec1.norm() * vec2.norm())

  return similarity_score