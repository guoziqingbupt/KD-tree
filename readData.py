import csv


def readData(fileName):
    """
    read the csv file into a 2-dimensional matrix
    :param fileName:
    :return:
    """

    data = []

    with open(fileName) as csvFile:

        reader = csv.reader(csvFile)

        for item in reader:

            temp = []

            for attribute in item:
                temp.append(float(attribute))

            data.append(temp)

    return data

