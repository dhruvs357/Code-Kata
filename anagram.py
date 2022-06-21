def anagrams( s1, s2 ):
    #convert strings to lower case and sort them accordingly

    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())

    #If both sorted strings matched,then they are anagrams else not
    return s1 == s2

def all_anagrams( string ):
    anagrams_list = []
    with open("wordlist.txt", "r") as fileObject:
        # if it an anagram
        #append it to anagram list
        for line in fileObject:
            word = line.strip()
            if anagrams(string, word):
                anagrams_list.append(word)
    return anagrams_list
    
'''
checking any particular word anagrams

#print(all_anagrams('ABD'))

'''

with open("wordlist.txt","r") as f:
    for line in f:
       
       #for getting all sets of anagrams in file

       print(all_anagrams(line.rstrip("\n")))
       
       
       #print(line)

