import csv
import pickle

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
    with open(objects_repo_location + name + '.pkl', 'wb') as file:
        pickle.dump(object, file, pickle.HIGHEST_PROTOCOL)


def load_object(name):
    with open(objects_repo_location + name + '.pkl', 'rb') as file:
        return pickle.load(file)
