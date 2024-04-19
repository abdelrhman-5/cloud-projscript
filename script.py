import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download NLTK stopwords and punkt
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
    # Load stopwords
    stop_words = set(stopwords.words('english'))
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

def count_word_frequency(words):
    # Count word frequency
    word_freq = Counter(words)
    return word_freq

def display_word_frequency(word_freq):
    # Display word frequency count
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')

def analyze_word_distribution(word_freq):
    # Analyze word distribution
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print("Word Distribution:")
    for word, freq in sorted_word_freq:
        print(f'{word}: {freq}')

def identify_keywords(word_freq, threshold=5):
    # Identify keywords
    print(f"\nKeywords (appearing more than {threshold} times):")
    for word, freq in word_freq.items():
        if freq > threshold:
            print(f'{word}: {freq}')

def visualize_word_frequency(word_freq):
    # Visualize word frequency
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def main():
    # File path to random_paragraphs.txt
    file_path = "random_paragraphs.txt"

    # Read the contents of the file
    text = read_file(file_path)
    if text is None:
        return

    # Remove stopwords
    words = remove_stopwords(text)

    # Count word frequency
    word_freq = count_word_frequency(words)

    # Display word frequency count
    display_word_frequency(word_freq)

    # Analyze word distribution
    analyze_word_distribution(word_freq)

    # Identify keywords
    identify_keywords(word_freq)

    # Visualize word frequency
    visualize_word_frequency(word_freq)

    # Further analysis and tasks can be added here

if __name__ == "__main__":
    main()
