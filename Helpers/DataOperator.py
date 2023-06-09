import csv
import pickle
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
import itertools
import string
from wordcloud import WordCloud
import random
import gensim
from gensim import corpora


index_artist = 0
index_title = 1
index_link = 2
index_text = 3
NUM_TOPICS = 5

objects_repo_location = "/Users/reckony/Desktop/UGSTUDIA/IOproject/ObjectsRepo/"
noise1 = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before’,' 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
noise2 = string.punctuation


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

    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


def remove_stopwords_and_noise(tokenized_dict):
    stop_words = set(stopwords.words("english"))
    punctuation = string.punctuation
    dict_no_stopwords = {}
    for key, value in tokenized_dict.items():
        tokenized_songs = value
        artist_name = key
        songs_text_without_stopwords = []
        for tokenized_song in tokenized_songs:
            filtered_song = []
            for word in tokenized_song:
                if word not in stop_words and word not in punctuation:
                    filtered_song.append(word)
            songs_text_without_stopwords.append(filtered_song)
        dict_no_stopwords[artist_name] = songs_text_without_stopwords
    return dict_no_stopwords


def get_word_frequency_plot(tokenized_text, chart_title):
    word_frequency_plot = FreqDist(tokenized_text)
    word_frequency_plot.plot(20, title=chart_title, cumulative=False)

    return word_frequency_plot


def get_frequency_list(dict_to_get_word_frequency_for_artists):
    most_frequent_words_dict = {}
    for key, value in dict_to_get_word_frequency_for_artists.items():
        artist = key
        song_text = value
        song_text = [x.lower() for x in song_text]
        word_frequency = FreqDist(song_text)
        most_common_50 = list(word_frequency.most_common(50))
        most_frequent_words_dict[artist] = most_common_50

    return most_frequent_words_dict


def get_cosine_similarity(tokenized_filtered_text1, tokenized_filtered_text2):
    text1 = []
    text2 = []
    text1_tokenized = word_tokenize(tokenized_filtered_text1)
    text2_tokenized = word_tokenize(tokenized_filtered_text2)
    sw = stopwords.words('english')

    text1_set = {w for w in text1_tokenized if not w in sw}
    text2_set = {w for w in text2_tokenized if not w in sw}

    rvector = text1_set.union(text2_set)
    for w in rvector:
        if w in text1_set:
            text1.append(1)  # create a vector
        else:
            text1.append(0)
        if w in text2_set:
            text2.append(1)
        else:
            text2.append(0)

    c = 0
    # cosine formula
    for i in range(len(rvector)):
        c += text1[i] * text2[i]
    cosine = c / float((sum(text1) * sum(text2)) ** 0.5)

    return cosine


def get_all_words(dict_to_combine_its_values):
    dict_combined_songs = {}
    for key, value in dict_to_combine_its_values.items():
        artist = key
        songs_list = value
        combined_songs = list(itertools.chain.from_iterable(songs_list))
        dict_combined_songs[artist] = combined_songs

    return dict_combined_songs


def remove_noise(dict_to_clean):
    clean_dict = {}
    for key, value in dict_to_clean.items():
        artist = key
        songs = value
        songs = [x.lower() for x in songs]
        clean_songs = [w for w in songs if w not in noise1 and w not in noise2]
        clean_dict[artist] = clean_songs

    return clean_dict


def get_interesting_words(freq_dict):
    new_freq_dict = {}
    for key, value in freq_dict.items():
        artist = key
        word_list = value
        new_word_list = []
        for info in word_list:
            if len(info[0]) > 3:
                new_word_list.append(info)
        new_word_list = new_word_list[:20]
        new_freq_dict[artist] = new_word_list

    return new_freq_dict


def create_wordcloud(dict_to_create_wordcloud):

    for key, value in dict_to_create_wordcloud.items():
        artist = key
        text = value
        text_list = []
        for data in text:
            word = data[0]
            freq = data[1]
            for i in range(freq):
                text_list.append(word)
        new_text = ' '.join(text_list)

        wordcloud = WordCloud(collocations=False, background_color="white", max_font_size=50, max_words=100).generate(new_text)
        wordcloud.to_file("/Users/reckony/Desktop/UGSTUDIA/IOproject/Wordclouds/" + f'Wordcloud_{artist}.png')
    return True


def join_text(tokenized_dict):
    joined_dict = {}
    for key, value in tokenized_dict.items():
        artist = key
        text = value
        joined_text_list = []
        for data in text:
            joined_text = ' '.join(data)
            joined_text_list.append(joined_text)
        joined_all = ''.join(joined_text_list)
        joined_dict[artist] = joined_all
    return joined_dict


def find_similar_artists(dict1, dict2):
    similar_artists = []

    for i in range(10):
        artist1 = random.choice(list(dict1.keys()))
        artist2 = random.choice(list(dict2.keys()))
        songs_text1 = dict1[artist1]
        songs_text2 = dict2[artist2]
        cosine = get_cosine_similarity(songs_text1, songs_text2)
        # if cosine >= 0.5:
        cosine_info = [artist1, artist2, cosine]
        # else:
        #     cosine_info = 0
        similar_artists.append(cosine_info)
    return similar_artists


def get_main_topics(dict_to_check):
    topics_dict = {}
    for key, value in dict_to_check.items():
        artist = key
        songs = value
        songs_topic_list = []
        for song in songs:
            song1 = [d.split() for d in song1]
            dictionary = corpora.Dictionary(song1)
            corpus = [dictionary.doc2bow(text) for text in song1]
            ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
            topics = ldamodel.print_topics(num_words=5)
            songs_topic_list.append(songs.index(song))
            songs_topic_list.append(topics)
        topics_dict[artist] = songs_topic_list
    return topics_dict




