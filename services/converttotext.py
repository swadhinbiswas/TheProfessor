import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    
    # Remove stop words and non-alphanumeric characters
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

def get_similarity_score(text1, text2):
    tokens1 = preprocess(text1)
    tokens2 = preprocess(text2)
    
    # Calculate Jaccard similarity
    intersection = set(tokens1).intersection(set(tokens2))
    union = set(tokens1).union(set(tokens2))
    jaccard_similarity = len(intersection) / len(union)
    
    return jaccard_similarity

def check_plagiarism(text1, text2, threshold=0.7):
    similarity_score = get_similarity_score(text1, text2)
    if similarity_score >= threshold:
        return True, similarity_score
    else:
        return False, similarity_score

# Example usage


# Example usage

# Note: This is a basic example and might not catch all forms of plagiarism.

    
    
    
    
    
    
text1="""
I'm programmed to be helpful and informative, and that includes upholding academic integrity. Providing information on how to commit plagiarism would go against that purpose. However, I'm happy to guide you on how to create original and ethical work! Here are some key strategies:

**Develop your own understanding:**

* **Deep dive into your research:** Read different sources, analyze data, and form your own interpretations. Don't just rely on one or two sources to parrot their information.
* **Take comprehensive notes:** Summarize key points in your own words, paraphrase important concepts, and jot down your own ideas and reactions to the material.

**Express your understanding in your own words:**

* **Paraphrase effectively:** Rephrase sentences and passages, using synonyms and alternative sentence structures while maintaining the original meaning. Don't just swap a few words!
* **Quote sparingly and ethically:** Use quotes only for direct speech, unique phrasing, or specific data, and always cite them properly according to the required style guide.
* **Focus on your analysis and insights:** Don't just regurgitate facts; demonstrate your understanding by analyzing information, drawing connections, and offering your own interpretations.

**Utilize ethical resources:**

* **Citation tools and guides:** Use tools like citation generators to ensure proper formatting and reference all sources you use, even if you paraphrase or summarize.
* **Plagiarism checkers:** These tools can identify potential areas of similarity, but remember, they are not foolproof. Use them as a guide, not a guarantee of originality.

**Remember:** Plagiarism is not just about copying text; it's about failing to give credit where credit is due and presenting someone else's work as your own. By understanding and respecting intellectual property, you can create original and ethical work that reflects your own learning and voice.

If you have further questions or need more specific guidance on avoiding plagiarism in your work, feel free to ask!

           """
           
           
text2="""

Being plagiarism-free is crucial for maintaining academic integrity and ethical standards in writing. Here are some tips to help you avoid plagiarism:

Understand what plagiarism is: Plagiarism is the act of using someone else's words, ideas, or work without proper acknowledgment or citation.

Use your own words: When paraphrasing or summarizing information from a source, express it in your own words while still conveying the original meaning. This demonstrates your understanding of the material.

Cite your sources: Whenever you use someone else's ideas, quotes, or data, make sure to provide proper attribution through citations. Follow the citation style required by your institution or publication (e.g., APA, MLA, Chicago).

Keep track of your sources: Keep detailed records of all the sources you consult during your research, including books, articles, websites, and interviews. This makes it easier to properly cite them later.

Use quotation marks: When directly quoting someone else's words, enclose them in quotation marks and provide a citation to indicate the source.

Give credit for ideas: Not only should you cite direct quotes, but you should also acknowledge the source of any ideas or concepts that you borrow from others, even if you rephrase them in your own words.

Use plagiarism detection tools: Utilize plagiarism detection software or online tools to check your work before submission. These tools can help identify any unintentional instances of plagiarism that may have occurred.

Be cautious with group work: When collaborating with others on projects, ensure that everyone understands the importance of avoiding plagiarism and properly citing

"""


is_plagiarized, similarity_score = check_plagiarism(text1, text2)
if is_plagiarized:
    print("Plagiarism detected! Similarity score:", similarity_score)
else:
    print("No plagiarism detected. Similarity score:", similarity_score)