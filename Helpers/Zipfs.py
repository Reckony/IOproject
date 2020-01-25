import collections


def generate_zipf_table(text, top):
    text = _remove_punctuation(text)
    text = text.lower()
    top_word_frequencies = _top_word_frequencies(text, top)
    zipf_table = _create_zipf_table(top_word_frequencies)

    return zipf_table


def _remove_punctuation(text):
    chars_to_remove = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
    tr = str.maketrans("", "", chars_to_remove)

    return text.translate(tr)


def _top_word_frequencies(text, top):
    words = text.split()
    word_frequencies = collections.Counter(words)
    top_word_frequencies = word_frequencies.most_common(top)

    return top_word_frequencies


def _create_zipf_table(frequencies):
    zipf_table = []
    top_frequency = frequencies[0][1]

    for index, item in enumerate(frequencies, start=1):

        relative_frequency = "1/{}".format(index)
        zipf_frequency = top_frequency * (1 / index)
        difference_actual = item[1] - zipf_frequency
        difference_percent = (item[1] / zipf_frequency) * 100

        zipf_table.append({"word": item[0],
                           "actual_frequency": item[1],
                           "relative_frequency": relative_frequency,
                           "zipf_frequency": zipf_frequency,
                           "difference_actual": difference_actual,
                           "difference_percent": difference_percent})

    return zipf_table


def print_zipf_table(zipf_table):
    width = 80
    print("-" * width)
    print("|Rank|    Word    |Actual Freq | Zipf Frac  | Zipf Freq  |Actual Diff |Pct Diff|")
    print("-" * width)
    format_string = "|{:4}|{:12}|{:12.0f}|{:>12}|{:12.2f}|{:12.2f}|{:7.2f}%|"

    for index, item in enumerate(zipf_table, start=1):

        print(format_string.format(index,
                                   item["word"],
                                   item["actual_frequency"],
                                   item["relative_frequency"],
                                   item["zipf_frequency"],
                                   item["difference_actual"],
                                   item["difference_percent"]))

    print("-" * width)


def get_average_zipf_per_artist(zipfs_dict):
    diff_list = []
    for key, value in zipfs_dict.items():
        artist = key
        zipfs_table = value
        zipfs_average_values = []
        av = []
        for row_list in zipfs_table:
            diff_row_list = []
            for dict_row in row_list:
                diff = dict_row["difference_actual"]
                diff_row_list.append(diff)
            diff_row = sum(diff_row_list) / len(diff_row_list)
            av.append(diff_row)
        average_difference = sum(av) / len(av)
        zipfs_average_values.append(average_difference)
        overall_average = sum(zipfs_average_values) / len(zipfs_average_values)
        diff_info = (artist, overall_average)
        diff_list.append(diff_info)
    return diff_list


def create_zip_table_for_dict(dict):
    zip_dict = {}
    for key, value in dict.items():
        zip_table_list = []
        artist = key
        songs = value
        for song in songs:
            song = [w.lower() for w in song]
            song = [w for w in song if len(w) > 3]
            song = " ".join(song)
            zipfs_table = generate_zipf_table(song, 50)
            zip_table_list.append(zipfs_table)
        zip_dict[artist] = zip_table_list
    return zip_dict
