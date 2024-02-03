import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Define a class to find plagiarism

class FindPlager():
    def __init__(self,text1,text2):
        self.text1 = text1
        self.text2 = text2
        
    def preprocess(self,text):
        # Tokenize the text
        tokens = word_tokenize(text.lower())
        
        # Remove stop words and non-alphanumeric characters
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
        
        # Lemmatize tokens
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        
        return tokens
      
    def get_similarity_score(self,text1, text2):
        tokens1 = self.preprocess(text1)
        tokens2 = self.preprocess(text2)
        
        # Calculate Jaccard similarity
        intersection = set(tokens1).intersection(set(tokens2))
        union = set(tokens1).union(set(tokens2))
        jaccard_similarity = len(intersection) / len(union)
        
        return jaccard_similarity
    
    def check_plagiarism(self,threshold=0.7):
        similarity_score = self.get_similarity_score(self.text1, self.text2)
        if similarity_score >= threshold:
            return True, similarity_score
        else:
            return False, similarity_score
    def main(self):
        return self.check_plagiarism()