from Helpers import DataOperator as cvh

index_artist = 0
index_title = 1
index_link = 2
index_text = 3

if __name__ == "__main__":
    # mydict = cvh.load_object("SongsDict1")
    # print(mydict.keys())

    # csv_files_list, dict_files_list = cvh.create_lists_of_names()

    # helper_dict = cvh.create_dict_helper(csv_files_list, dict_files_list)
    #
    # cvh.create_dict_from_csvs(helper_dict)

    # song_dict1 = cvh.load_object("SongsDict1.pkl")
    # song_dict2 = cvh.load_object("SongsDict2.pkl")
    # song_dict3 = cvh.load_object("SongsDict3.pkl")
    # song_dict4 = cvh.load_object("SongsDict4.pkl")
    # song_dict5 = cvh.load_object("SongsDict5.pkl")
    # song_dict6 = cvh.load_object("SongsDict6.pkl")
    # song_dict7 = cvh.load_object("SongsDict7.pkl")
    # song_dict8 = cvh.load_object("SongsDict8.pkl")
    # song_dict9 = cvh.load_object("SongsDict9.pkl")
    # song_dict10 = cvh.load_object("SongsDict10.pkl")
    # song_dict11 = cvh.load_object("SongsDict11.pkl")
    # song_dict12 = cvh.load_object("SongsDict12.pkl")
    # song_dict13 = cvh.load_object("SongsDict13.pkl")
    # song_dict14 = cvh.load_object("SongsDict14.pkl")
    #
    # song_dicts_list = [
    #     song_dict1,
    #     song_dict2,
    #     song_dict3,
    #     song_dict4,
    #     song_dict5,
    #     song_dict6,
    #     song_dict7,
    #     song_dict8,
    #     song_dict9,
    #     song_dict10,
    #     song_dict11,
    #     song_dict12,
    #     song_dict13,
    #     song_dict14
    # ]

    # song_dict_tokenized1 = cvh.load_object("TokenizedSongs1.pkl")
    # song_dict_tokenized2 = cvh.load_object("TokenizedSongs2.pkl")
    # song_dict_tokenized3 = cvh.load_object("TokenizedSongs3.pkl")
    # song_dict_tokenized4 = cvh.load_object("TokenizedSongs4.pkl")
    # song_dict_tokenized5 = cvh.load_object("TokenizedSongs5.pkl")
    # song_dict_tokenized6 = cvh.load_object("TokenizedSongs6.pkl")
    # song_dict_tokenized7 = cvh.load_object("TokenizedSongs7.pkl")
    # song_dict_tokenized8 = cvh.load_object("TokenizedSongs8.pkl")
    # song_dict_tokenized9 = cvh.load_object("TokenizedSongs9.pkl")
    # song_dict_tokenized10 = cvh.load_object("TokenizedSongs10.pkl")
    # song_dict_tokenized11 = cvh.load_object("TokenizedSongs11.pkl")
    # song_dict_tokenized12 = cvh.load_object("TokenizedSongs12.pkl")
    # song_dict_tokenized13 = cvh.load_object("TokenizedSongs13.pkl")
    # song_dict_tokenized14 = cvh.load_object("TokenizedSongs14.pkl")
    #
    # tokenized_song_dicts_list = [
    #     song_dict_tokenized1,
    #     song_dict_tokenized2,
    #     song_dict_tokenized3,
    #     song_dict_tokenized4,
    #     song_dict_tokenized5,
    #     song_dict_tokenized6,
    #     song_dict_tokenized7,
    #     song_dict_tokenized8,
    #     song_dict_tokenized9,
    #     song_dict_tokenized10,
    #     song_dict_tokenized11,
    #     song_dict_tokenized12,
    #     song_dict_tokenized13,
    #     song_dict_tokenized14
    # ]

    # song_dict_filtered1 = cvh.load_object("FilteredSongs1.pkl")
    # song_dict_filtered2 = cvh.load_object("FilteredSongs2.pkl")
    # song_dict_filtered3 = cvh.load_object("FilteredSongs3.pkl")
    # song_dict_filtered4 = cvh.load_object("FilteredSongs4.pkl")
    # song_dict_filtered5 = cvh.load_object("FilteredSongs5.pkl")
    # song_dict_filtered6 = cvh.load_object("FilteredSongs6.pkl")
    # song_dict_filtered7 = cvh.load_object("FilteredSongs7.pkl")
    # song_dict_filtered8 = cvh.load_object("FilteredSongs8.pkl")
    # song_dict_filtered9 = cvh.load_object("FilteredSongs9.pkl")
    # song_dict_filtered10 = cvh.load_object("FilteredSongs10.pkl")
    # song_dict_filtered11 = cvh.load_object("FilteredSongs11.pkl")
    # song_dict_filtered12 = cvh.load_object("FilteredSongs12.pkl")
    # song_dict_filtered13 = cvh.load_object("FilteredSongs13.pkl")
    # song_dict_filtered14 = cvh.load_object("FilteredSongs14.pkl")
    #
    # filtered_song_dicts_list = [
    #     song_dict_filtered1,
    #     song_dict_filtered2,
    #     song_dict_filtered3,
    #     song_dict_filtered4,
    #     song_dict_filtered5,
    #     song_dict_filtered6,
    #     song_dict_filtered7,
    #     song_dict_filtered8,
    #     song_dict_filtered9,
    #     song_dict_filtered10,
    #     song_dict_filtered11,
    #     song_dict_filtered12,
    #     song_dict_filtered13,
    #     song_dict_filtered14
    # ]
    #
    # lemmatized_filenames_list = cvh.create_list_of_given_names("LemmatizedSongs", ".pkl")
    #
    # lemmatized_dicts_list = []
    #
    # for filtered_dict in filtered_song_dicts_list:
    #     lemmatized_dict = cvh.lemmatize_dict(filtered_dict)
    #     lemmatized_dicts_list.append(lemmatized_dict)
    #
    # for i in range(len(lemmatized_dicts_list)):
    #     cvh.save_object_to_file(lemmatized_dicts_list[i], lemmatized_filenames_list[i])

    # lemmatized_dict1 = cvh.load_object("LemmatizedSongs1.pkl")
    # tokenized_dict1 = cvh.load_object("TokenizedSongs1.pkl")
    # filtered_dict1 = cvh.load_object("FilteredSongs1.pkl")
    # print(tokenized_dict1["Adele"][1])
    # print(filtered_dict1["Adele"][1])
    # print(lemmatized_dict1["Adele"][1])

    # newdict = cvh.get_all_words(lemmatized_dict1)

    # combined_songs_dict_filenames = cvh.create_list_of_given_names("CombinedSongs", ".pkl")
    #
    # combined_songs_dicts_list = []
    #
    # for filtered_dict in filtered_song_dicts_list:
    #     combined_dict = cvh.get_all_words(filtered_dict)
    #     combined_songs_dicts_list.append(combined_dict)
    #
    # for i in range(len(combined_songs_dicts_list)):
    #     cvh.save_object_to_file(combined_songs_dicts_list[i], combined_songs_dict_filenames[i])

    # combined_dict1 = cvh.load_object("CombinedSongs1.pkl")
    # combined_dict2 = cvh.load_object("CombinedSongs2.pkl")
    # combined_dict3 = cvh.load_object("CombinedSongs3.pkl")
    # combined_dict4 = cvh.load_object("CombinedSongs4.pkl")
    # combined_dict5 = cvh.load_object("CombinedSongs5.pkl")
    # combined_dict6 = cvh.load_object("CombinedSongs6.pkl")
    # combined_dict7 = cvh.load_object("CombinedSongs7.pkl")
    # combined_dict8 = cvh.load_object("CombinedSongs8.pkl")
    # combined_dict9 = cvh.load_object("CombinedSongs9.pkl")
    # combined_dict10 = cvh.load_object("CombinedSongs10.pkl")
    # combined_dict11 = cvh.load_object("CombinedSongs11.pkl")
    # combined_dict12 = cvh.load_object("CombinedSongs12.pkl")
    # combined_dict13 = cvh.load_object("CombinedSongs13.pkl")
    # combined_dict14 = cvh.load_object("CombinedSongs14.pkl")
    #
    # combined_song_dicts_list = [
    #     combined_dict1,
    #     combined_dict2,
    #     combined_dict3,
    #     combined_dict4,
    #     combined_dict5,
    #     combined_dict6,
    #     combined_dict7,
    #     combined_dict8,
    #     combined_dict9,
    #     combined_dict10,
    #     combined_dict11,
    #     combined_dict12,
    #     combined_dict13,
    #     combined_dict14
    # ]
    #
    # filesnames = cvh.create_list_of_given_names("CleanCombinedSongs", ".pkl")
    # cleanlist = []
    # for combined_dict in combined_song_dicts_list:
    #     clear_dict = cvh.remove_noise(combined_dict)
    #     cleanlist.append(clear_dict)
    #
    # for i in range(len(cleanlist)):
    #     cvh.save_object_to_file(cleanlist[i], filesnames[i])

    # clean_dict1 = cvh.load_object("CleanCombinedSongs1.pkl")
    # clean_dict2 = cvh.load_object("CleanCombinedSongs2.pkl")
    # clean_dict3 = cvh.load_object("CleanCombinedSongs3.pkl")
    # clean_dict4 = cvh.load_object("CleanCombinedSongs4.pkl")
    # clean_dict5 = cvh.load_object("CleanCombinedSongs5.pkl")
    # clean_dict6 = cvh.load_object("CleanCombinedSongs6.pkl")
    # clean_dict7 = cvh.load_object("CleanCombinedSongs7.pkl")
    # clean_dict8 = cvh.load_object("CleanCombinedSongs8.pkl")
    # clean_dict9 = cvh.load_object("CleanCombinedSongs9.pkl")
    # clean_dict10 = cvh.load_object("CleanCombinedSongs10.pkl")
    # clean_dict11 = cvh.load_object("CleanCombinedSongs11.pkl")
    # clean_dict12 = cvh.load_object("CleanCombinedSongs12.pkl")
    # clean_dict13 = cvh.load_object("CleanCombinedSongs13.pkl")
    # clean_dict14 = cvh.load_object("CleanCombinedSongs14.pkl")
    #
    # clean_song_dicts_list = [
    #     clean_dict1,
    #     clean_dict2,
    #     clean_dict3,
    #     clean_dict4,
    #     clean_dict5,
    #     clean_dict6,
    #     clean_dict7,
    #     clean_dict8,
    #     clean_dict9,
    #     clean_dict10,
    #     clean_dict11,
    #     clean_dict12,
    #     clean_dict13,
    #     clean_dict14
    # ]
    #
    # filenames_frequent_words = cvh.create_list_of_given_names("MostFrequentWords", ".pkl")
    #
    # freq_dicts_list = []
    # for clean_dict in clean_song_dicts_list:
    #     freq = cvh.get_frequency_list(clean_dict)
    #     freq_dict = cvh.get_interesting_words(freq)
    #     freq_dicts_list.append(freq_dict)
    # for i in range(len(freq_dicts_list)):
    #     cvh.save_object_to_file(freq_dicts_list[i], filenames_frequent_words[i])

    freq = cvh.load_object("MostFrequentWords14.pkl")  # 1, 2, 5, 8, 12, 14
    cvh.create_wordcloud(freq)

