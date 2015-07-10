import sys
import random
import string

class SimpleMarkovGenerator(object):
    character_limit = 2000

    def read_files(self, text_sources):
        """Given a list of files, make chains from them."""

        text_input = ""

        for text_file in text_sources:
            text_file = open(text_file)
            text_input += text_file.read()
            text_file_lower = text_input.lower()
        
        word_list = text_file_lower.split()
        
        return word_list


    def make_chains(self, word_list):
        """Takes input text as string; stores chains."""
        
        markov_pairs = {}

        # Traversing through indices until we reach the second-to-last word.
        # Stop at 2 because the last word will never need to be a key.
        for i in range(len(word_list) - 2):

            # Creates a new tuple where first item is a word, and second item is 
            # the word that comes after
            pair = word_list[i], word_list[i+1]

            if pair in markov_pairs:

                # Adding the word after the pair [i+2] as a value 
                markov_pairs[pair].append(word_list[i+2])
            
            else:
                # If pair is not in markov_pairs, add key and value
                # where value is a list containing word immediately after pair [i+2]
                markov_pairs[pair] = [word_list[i+2]]    

        return markov_pairs
               
        
    def make_text(self, dictionary):
        """Takes dictionary of markov chains; returns random text."""  

        # select a random word
        first_key = random.choice(dictionary.keys())

        # Start sentence with both words in first key
        goofy_sentence = first_key[0] + " " + first_key[1]


        # Run as long as key is in the dicitonary    
        while first_key in dictionary and len(goofy_sentence) <= self.character_limit:

            # go back to dictionary, find values of the key that we returned
            # randomly select word from that list
            next_word = random.choice(dictionary[first_key])

            # add that randomly selected word to the sentence
            goofy_sentence += " " + next_word

            # find key that starts with the second value in first_word and the randomly selected
            # then assigns it to first key to continue loop
            # ex:
                # first_key ('Would', 'you')
                # next_word ('could')
                # --> first_key ('you', 'could')
            first_key = (first_key[1],next_word) 
        

        return goofy_sentence
        # goofy_sent_rmv_punc = goofy_sentence
        
        # for punc in string.punctuation:
        #     goofy_sent_rmv_punc = goofy_sent_rmv_punc.replace(punc, "")   
        
        # return goofy_sent_rmv_punc


class TweetableMarkovGenerator(SimpleMarkovGenerator):
    character_limit = 130


if __name__ == "__main__":

    
    # (1) For each source file run the read function assigning each string file 
    #     to a unique variable

    text_sources = sys.argv[1:]
    

    # test = SimpleMarkovGenerator()
    
    # running_markov = test.read_files(text_sources)
    # running_markov2 = test.make_chains(running_markov)
    
    twitterbot = TweetableMarkovGenerator()
    running_twitterbot = twitterbot.read_files(text_sources)
    running_twitterbot2 = twitterbot.make_chains(running_twitterbot)

    # print test.make_text(running_markov2)

    print twitterbot.make_text(running_twitterbot2)
    

    # (2) For each string file run the dictionary creator assigning each dictionary
    #     to a unique variable.
    # (3) Find the longest dictionary, make that the master and compare the other two
    #     adding unique keys with their values and the values from non-unique keys.
    # (4) Run the make text function on our new GIANT dictionary.
