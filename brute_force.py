

""" 
A brute force, password protected, zip file opener.
Tool has been developed for educational purposes only, as part of the IBM's Cyber "Capture the Flag"
Enjoy
"""

import string
import sys
import time
import zipfile


FILE_OPTIONS = {
    "-c" : list(string.lowercase),
    "-u" : list(string.uppercase),
    "-d" : list(string.digits),
    "-s" : list(string.punctuation),
}

def pw_find(zip_file, max_length, chars):
    curr_pswds = [""]
    prev_pswds = [""]
    for i in range(max_length):
        print "CURRENT LENGTH: %s" %i
        prev_pswds = curr_pswds
        curr_pswds = pw_find_fixed_size(zip_file, prev_pswds, chars)
        if curr_pswds is None:
            return
    print "PASSWORD NOT FOUND!!!"

def pw_find_fixed_size(zip_file, prev_pswds, chars):
    pswds = []
    for prev_pswd in prev_pswds:
        for chr in chars:
            curr_pswd = "%s%s" % (prev_pswd, chr)
            # print "CURRENT:\t%s " % curr_pswd
            
            # check pswd
            try:
                zip_file.extractall(pwd=curr_pswd)
                print 'PASSWORD FOUND!!: %s' % curr_pswd
                return None
            except:
				pass
                
            # otherwise apped
            pswds.append(curr_pswd)
    return pswds

def main():
    if len(sys.argv) < 3:
        print "Usage: <file> <max_length> [<-u UPPERCASE> <-l LOWERCASE> <-d digits> <-s symbols>]"    
        return
        
    zipfilename = sys.argv[1]
    max_length = int(sys.argv[2])
    
    #get pswd chars
    chars = []
    for key, val in FILE_OPTIONS.items():
        if key in ''.join(sys.argv[3:]):
            chars += val
            
    print "Selected Characters: %s" % chars

    time.sleep(5)
    
    # find password
    zip_file = zipfile.ZipFile(zipfilename)
    pw_find(zip_file, max_length, chars)
    

if __name__ == '__main__':
	main()