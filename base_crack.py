import zipfile

import constants

class BaseCrack(object):
    def __init__(
        self,
        zip_file,
        max_length = constants.DEFAULT_MAX_LENGTH,
        min_length = constants.DEFAULT_MIN_LENGTH,
    ):
        self._max_length = max_length
        self._min_length = min_length
        self._zip_file = zip_file
        
    def crack(self):
        pass
    
    def try_crack(self, curr_pswd):
        try:
            self._zip_file.extractall(pwd=curr_pswd)
        except:
            return False
        return True