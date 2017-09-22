
import base_crack
import constants

class BruteForce(base_crack.BaseCrack):        
    def __init__(
        self,
        zip_file,
        max_length,
        min_length,
        chars = constants.FILE_OPTIONS["-l"]
    ):
        super(BruteForce, self).__init__(zip_file, max_length, min_length)
        self._found_pswd = ""
        self._chars = chars
        print "Selected Chars: %s\n" % self._chars
    
    """
    Cracks using brute force method
    Output: found pswd
    """
    def crack(self):
        curr_pswds = [""]
        prev_pswds = [""]
        for i in range(self._min_length, self._max_length):
            print "CURRENT LENGTH: %s" %i
            prev_pswds = curr_pswds
            curr_pswds = self.pw_find_fixed_size(prev_pswds)
            
            if curr_pswds is None:
                return self._found_pswd 
        return None
     
    """
    Finds all passwords of fixed size
    Input: prev_pswds - all passwords of curr_size - 1
    Output: None if finished searching and found the one, otherwise the list of passwords
    """
    def pw_find_fixed_size(self, prev_pswds):
        pswds = []
        for prev_pswd in prev_pswds:
            for chr in self._chars:
                curr_pswd = "%s%s" % (prev_pswd, chr)            
                # check pswd
                if self.try_crack(curr_pswd):
                    # password found
                    self._found_pswd = curr_pswd
                    return None
                else:
                    # otherwise append
                    pswds.append(curr_pswd)
        return pswds