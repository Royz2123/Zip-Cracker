import string

MAX_BUFFER = 1024

DEFAULT_MAX_LENGTH = 10
DEFAULT_MIN_LENGTH = 0

DEFAULT_DICT_FILE = "dict.txt"
DICTIONARY_SEP = "\n"
DICTIONARY_ATTACK = "-dict"

FILE_OPTIONS = {
    "-l" : list(string.lowercase),
    "-u" : list(string.uppercase),
    "-d" : list(string.digits),
    "-s" : list(string.punctuation),
}

FOUND_MSG = "Found the password! %s\n"
NOT_FOUND_MSG = "Password not found\n"