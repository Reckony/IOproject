from Helpers import CsvHandler as cvh


if __name__ == "__main__":

    index_artist = 0
    index_title = 1
    index_link = 2
    index_text = 3


    # data = cvh.get_data("output_1.csv")
    # songs_dict_1 = cvh.get_artists_dict(data)

    # cvh.save_object_to_file(songs_dict_1, "SongsDict1")

    mydict = cvh.load_object("SongsDict1")
    print(mydict.keys())





