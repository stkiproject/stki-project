import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import os
nltk.download('stopwords')

# Inisialisasi stop words dan stemmer
stop_words = set(stopwords.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def load_model(model_path):
    return joblib.load(model_path)

def load_vectorizer(vectorizer_path):
    return joblib.load(vectorizer_path)

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

def predict(input_text, model_path="multinomial_nb_model.pkl", vectorizer_path="tfidf_vectorizer.pkl"):
    """
    Predict apakah input text adalah hoax atau tidak

    Args:
        model: model machine learning model (default: "multinomial_nb_model.txt")
        vectorizer: vectorizer yang digunakan (default: "tfidf_vectorizer.pkl")
        input_text: raw input text untuk diklasifikasi

    Returns:
        str: "Hoax" atau "Tidak Hoax" berdasarkan prediksi
    """
     # Get the directory path of the current file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Join the directory path with the filenames
    model_path = os.path.join(dir_path, model_path)
    vectorizer_path = os.path.join(dir_path, vectorizer_path)

    # Load the model and vectorizer
    model = load_model(model_path)
    vectorizer = load_vectorizer(vectorizer_path)

    # Preprocess the input text
    processed_text = preprocess_text(input_text)
    
    # Vectorize the input text
    vectorized_text = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction = model.predict(vectorized_text)
    
    # Map prediction to class label
    if prediction[0] == 0:
        return "Tidak Hoax"
    else:
        return "Hoax"