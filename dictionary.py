
import time

import base_crack
import constants

class Dictionary(base_crack.BaseCrack):        
    def __init__(
        self,
        zip_file,
        max_length,
        min_length,
        dict_file=constants.DEFAULT_DICT_FILE
    ):
        super(Dictionary, self).__init__(zip_file, max_length, min_length)
        self._dict_file = dict_file
        
    """
    Cracks using dictionary method
    Reads and parses an entire dict file 
    TODO: while reading try cracking
    Output: the found password
    """
    def crack(self):        
        for pswd in self.read_all().split(constants.DICTIONARY_SEP):
            if (
                len(pswd) <= self._max_length
                and len(pswd) >= self._min_length
                and self.try_crack(pswd)
            ):
                return pswd
        return None
        
    def read_all(self):
        read_pswds = ""
        with open(self._dict_file, "r") as f:
            while True:
                buf = f.read(constants.MAX_BUFFER)
                if buf == "":
                    break
                read_pswds += buf
        return read_pswds