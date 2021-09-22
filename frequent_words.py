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


def safe_sorted_dict(filename, words):
    with open(filename, 'w') as file:
        for word in sorted(words, words.get, reverse=True):
            file.write(word + '\n')


def main(argv):
    inName = "Resources/AliceInWonderland.txts"
    outName = "Resources/output.txts"

    try:
        options, args = getopt.getopt(argv, "hi:o:")
    except getopt.GetoptError:
        print("usage: python frequent_words.py -i <input_file> -o <output_file>")
        sys.exit(2)
    for opt, arg in options:
        if opt == '-h':
            print("usage: python frequent_words.py -i <input_file> -o <output_file>")
            sys.exit()
        elif opt == "-i":
            inName = arg
        elif opt == "-o":
            outName = arg

    words = read2dict(inName)
    safe_sorted_dict(outName, words)


if __name__ == "__main__":
    main(sys.argv[1:])
