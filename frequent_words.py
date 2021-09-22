import json
import csv
import sys
import getopt
import re


def read2dict(filename):
    words = dict()
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            res = re.findall(r'[a-zA-Z]+', line)
            for word in res:
                word = word.lower()
                words[word] = words.get(word, 0) + 1
    return words


def save2txt(filename, words):
    with open(filename, 'w') as file:
        for word in sorted(words, words.get, reverse=True):
            file.write(word + '\n')


def save2json(filename, words):
    with open(filename, 'w') as file:
        json.dump(words, file)


def save2csv(filename, words):
    with open(filename, 'w') as file:
        w = csv.writer(file)
        w.writerows(words.items())


def main(argv):
    inName = "Resources/AliceInWonderland.txts"
    outName = "Resources/output.txts"
    fType = "txt"

    try:
        options, args = getopt.getopt(argv, "hi:o:", ["type="])
    except getopt.GetoptError:
        print(
            "usage: python frequent_words.py -i <input_file> -o <output_file> [type=txt|json|csv|]")
        sys.exit(2)
    for opt, arg in options:
        if opt == '-h':
            print(
                "usage: python frequent_words.py -i <input_file> -o <output_file> [type=txt|json|csv|]")
            sys.exit()
        elif opt == "-i":
            inName = arg
        elif opt == "-o":
            outName = arg
        elif opt == "--type":
            fType = arg

    print(fType)
    words = read2dict(inName)
    if(fType == "txt"):
        save2txt(outName, words)
    elif(fType == "json"):
        save2json(outName, words)
    elif(fType == "csv"):
        save2csv(outName, words)


if __name__ == "__main__":
    main(sys.argv[1:])
