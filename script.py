import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud


nltk.download('stopwords')
nltk.download('punkt')

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def remove_stopwords(text):
    
    stop_words = set(stopwords.words('english'))
    
    words = word_tokenize(text)
    
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

def count_word_frequency(words):
    
    word_freq = Counter(words)
    return word_freq

def display_word_frequency(word_freq):
    
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

def analyze_word_distribution(word_freq):
    
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print("Word Distribution:")
    for word, freq in sorted_word_freq:
        print(f'{word}: {freq}')

def identify_keywords(word_freq, threshold=5):
    
    print(f"\nKeywords (appearing more than {threshold} times):")
    for word, freq in word_freq.items():
        if freq > threshold:
            print(f'{word}: {freq}')

def visualize_word_frequency(word_freq):
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    
    file_path = "random_paragraphs.txt"
    
    text = read_file(file_path)
    if text is None:
        return
    
    words = remove_stopwords(text)
    
    word_freq = count_word_frequency(words)
    
    display_word_frequency(word_freq)
    
    analyze_word_distribution(word_freq)

    identify_keywords(word_freq)

    visualize_word_frequency(word_freq)

    
if __name__ == "__main__":
    main()
