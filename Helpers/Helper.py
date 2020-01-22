import csv
import pickle
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet


index_artist = 0
index_title = 1
index_link = 2
index_text = 3

objects_repo_location = "/Users/reckony/Desktop/UGSTUDIA/IOproject/ObjectsRepo/"


def get_data(filepath):
    data = []
    file = open(filepath)
    csv_file = csv.reader(file)

    for row in csv_file:
        data.append(row)

    return data


def get_artists_dict(data):

    dict = {}
    for row in data:
        dict[row[index_artist]] = []
    for row in data:
        dict[row[index_artist]].append(row[index_text])
    return dict


def save_object_to_file(object, name):
    with open(objects_repo_location + name, 'wb') as file:
        pickle.dump(object, file, pickle.HIGHEST_PROTOCOL)


def load_object(name):
    with open(objects_repo_location + name, 'rb') as file:
        return pickle.load(file)


def create_lists_of_names():
    csv_files_list = []
    dict_files_list = []
    for i in range(2, 16):
        filename = f'output_{i}.csv'
        filename_dict = f'SongsDict{i}.pkl'
        csv_files_list.append(filename)
        dict_files_list.append(filename_dict)

    return csv_files_list, dict_files_list


def create_list_of_given_names(name, file_format):
    csv_files_list = []
    for i in range(1, 15):
        filename = f'{name}{i}{file_format}'
        csv_files_list.append(filename)

    return csv_files_list


def create_dict_helper(csv_files_list, dict_files_list):
    file_creation_dict = {}
    for i in range(len(csv_files_list)-1):
        file_creation_dict[csv_files_list[i]] = dict_files_list[i]
    return file_creation_dict


def create_dict_from_csvs(file_creation_dict):
    for key, value in file_creation_dict.items():
        data = get_data(key)
        songs_dict_1 = get_artists_dict(data)
        save_object_to_file(songs_dict_1, value)


def tokenize_dict(dict_to_tokenize):
    tokenized_dict = {}
    for key, value in dict_to_tokenize.items():
        song_texts_list_for_one_artist = value
        artist_name = key
        tokenized_texts_list_for_one_artist = []
        for song_text in song_texts_list_for_one_artist:
            song_text_without_line_breaks = song_text.replace("\n", " ")
            tokenized_text = word_tokenize(song_text_without_line_breaks)
            tokenized_texts_list_for_one_artist.append(tokenized_text)
        tokenized_dict[artist_name] = tokenized_texts_list_for_one_artist
    return tokenized_dict


def lemmatize_dict(tokenized_dict):
    lem = WordNetLemmatizer()
    lemmatized_dict = {}
    for key, value in tokenized_dict.items():
        tokenized_songs = value
        artist_name = key
        lemmatized_song_texts = []
        for tokenized_song in tokenized_songs:
            lemmatized_song = [lem.lemmatize(word, get_wordnet_pos(word)) for word in tokenized_song]
            lemmatized_song_texts.append(lemmatized_song)
        lemmatized_dict[artist_name] = lemmatized_song_texts
    return lemmatized_dict


def get_wordnet_pos(word):
    """
    Helper method for lemmatization.
    Map POS tag to first character lemmatize() accepts
    """
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def remove_stopwords(tokenized_dict):
    stop_words = set(stopwords.words("english"))
    dict_no_stopwords = {}
    for key, value in tokenized_dict.items():
        tokenized_songs = value
        artist_name = key
        songs_text_without_stopwords = []
        for tokenized_song in tokenized_songs:
            filtered_song = []
            for word in tokenized_song:
                if word not in stop_words:
                    filtered_song.append(word)
            songs_text_without_stopwords.append(filtered_song)
        dict_no_stopwords[artist_name] = songs_text_without_stopwords
    return dict_no_stopwords


