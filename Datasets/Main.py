from Helpers import DataOperator as cvh
import networkx as nx
import matplotlib.pyplot as plt
import gensim
from gensim import corpora
import string
import pyLDAvis.gensim
from Helpers import Zipfs as zs

index_artist = 0
index_title = 1
index_link = 2
index_text = 3

if __name__ == "__main__":
    lemmatized_dict1 = cvh.load_object("LemmatizedSongs1.pkl")
    lemmatized_dict2 = cvh.load_object("LemmatizedSongs2.pkl")
    lemmatized_dict3 = cvh.load_object("LemmatizedSongs3.pkl")
    lemmatized_dict4 = cvh.load_object("LemmatizedSongs4.pkl")
    lemmatized_dict5 = cvh.load_object("LemmatizedSongs5.pkl")
    lemmatized_dict6 = cvh.load_object("LemmatizedSongs6.pkl")
    lemmatized_dict7 = cvh.load_object("LemmatizedSongs7.pkl")
    lemmatized_dict8 = cvh.load_object("LemmatizedSongs8.pkl")
    lemmatized_dict9 = cvh.load_object("LemmatizedSongs9.pkl")
    lemmatized_dict10 = cvh.load_object("LemmatizedSongs10.pkl")
    lemmatized_dict11 = cvh.load_object("LemmatizedSongs11.pkl")
    lemmatized_dict12 = cvh.load_object("LemmatizedSongs12.pkl")
    lemmatized_dict13 = cvh.load_object("LemmatizedSongs13.pkl")
    lemmatized_dict14 = cvh.load_object("LemmatizedSongs14.pkl")

    lemmatized_dicts_list = [
                            lemmatized_dict1,
                            lemmatized_dict2,
                            lemmatized_dict3,
                            lemmatized_dict4,
                            lemmatized_dict5,
                            lemmatized_dict6,
                            lemmatized_dict7,
                            lemmatized_dict8,
                            lemmatized_dict9,
                            lemmatized_dict10,
                            lemmatized_dict11,
                            lemmatized_dict12,
                            lemmatized_dict13,
                            lemmatized_dict14
                            ]


    zip = cvh.load_object("MergedZipfs.pkl")

    avg_zip = zs.get_average_zipf_per_artist(zip)

    zip_points = []
    zip_labels = []
    x = []
    for i in range(1, len(avg_zip) - 1):
        zip_labels.append(avg_zip[i][0])
        zip_points.append(avg_zip[i][1])
    for i in range(len(zip_points)):
        x.append(i)

    plt.scatter(x, zip_points)
    plt.title("Zipf's law average for all analyzed bands")
    plt.show()