
""" 
A brute force, password protected, zip file opener.
Tool has been developed for educational purposes only, as part of the IBM's Cyber "Capture the Flag"
Enjoy
"""

import sys
import time
import zipfile

import brute_force
import constants
import dictionary
   
ATTACK_TYPES = {
    "brute_force" : brute_force.BruteForce,
    "dictionary" : dictionary.Dictionary
}        
        
def main():
    if len(sys.argv) < 3:
        print (
            "Usage: <zipped file>  <max_length>\n"
            + "OPTIONAL : [<-u UPPERCASE> <-l LOWERCASE> <-d digits> <-s symbols>]\n" 
            + "OPTIONAL : [<-d DICTIONARY> <dict_file>]\n"
        )
        return
        
    zipfilename = sys.argv[1]
    max_length = int(sys.argv[2])
            
    # decide attack type
    if constants.DICTIONARY_ATTACK in ''.join(sys.argv[3:]):
        print "Chosen attack type: DICTIONARY\n"
        attack_type = "dictionary"
        # unique arg is the dictionary file
        unique_arg = (
            ''.join(sys.argv[3:]).split(constants.DICTIONARY_ATTACK)[1].strip()
        )
    else:
        print "Chosen attack type: BRUTE FORCE\n"
        attack_type = "brute_force"
        # unique arg is the chars
        unique_arg = []
        for key, val in constants.FILE_OPTIONS.items():
            if key in ''.join(sys.argv[3:]):
                unique_arg += val
    
    # create zip file and cracker
    cracker = ATTACK_TYPES[attack_type](
        zipfile.ZipFile(zipfilename),
        max_length,
        constants.DEFAULT_MIN_LENGTH,
        unique_arg,
    )

    # crack pswd
    pswd = cracker.crack() 
    if pswd is not None:
        print constants.FOUND_MSG
    else:
        print constants.NOT_FOUND_MSG
    
if __name__ == '__main__':
	main()