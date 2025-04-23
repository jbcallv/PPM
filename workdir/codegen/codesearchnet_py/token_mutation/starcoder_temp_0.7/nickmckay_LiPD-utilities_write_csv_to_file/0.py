def write_csv_to_file(d):
    """
    Writes columns of data to a target CSV file.

    :param dict d: a dictionary containing one character for every data column. Keys: int, Values: list
    :return None:
    """
    with open("C:/Users/lengy/Desktop/test.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in d.items():
            writer.writerow([key, value])


