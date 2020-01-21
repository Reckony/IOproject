import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

if __name__ == "__main__":
    text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
    The sky is pinkish-blue. You shouldn't eat cardboard"""
    tokenized_text = sent_tokenize(text)
    print(tokenized_text)
    tokenized_word = word_tokenize(text)
    print(tokenized_word)
    fdist = FreqDist(tokenized_word)
    print(fdist)
    fdist.most_common(2)
    fdist.plot(30, cumulative=False)
    plt.show()
    stop_words = set(stopwords.words("english"))
    print(stop_words)

    # removing stopwords
    # filtered_sent = []
    # for w in tokenized_sent:
    #     if w not in stop_words:
    #         filtered_sent.append(w)
    # print("Tokenized Sentence:", tokenized_sent)
    # print("Filterd Sentence:", filtered_sent)


    # ps = PorterStemmer()
    # stemmed_words = []
    # for w in filtered_sent:
    #     stemmed_words.append(ps.stem(w))
    #
    # print("Filtered Sentence:", filtered_sent)
    # print("Stemmed Sentence:", stemmed_words)

    lem = WordNetLemmatizer()

    from nltk.stem.porter import PorterStemmer

    stem = PorterStemmer()

    word = "flying"
    print("Lemmatized Word:", lem.lemmatize(word, "v"))
    print("Stemmed Word:", stem.stem(word))