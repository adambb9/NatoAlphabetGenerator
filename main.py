import pandas

#aim to translate a user inputted word into a list containing the phonetic alphabet representation
#pandas library will be used to create a dataframe with letter and phonetic word

#read the alphabet doc into a dataframe
phonetic_alphabet = pandas.read_csv(r"NatoAlphabetGenerator\nato_phonetic_alphabet.csv")

#print(phonetic_alphabet)

#take input from the user
word_to_translate = input("What word would you like to translate?: ").upper()


#loop through list of letters and produce a list containing the translated letters
translated_word = [phonetic_alphabet[phonetic_alphabet["letter"] == letter].code.item() for letter in word_to_translate]

print(translated_word)


#loop through list of letters and produce a dictionary containing the translated letters
translated_word_dictionary = {row.letter: row.code  for (index, row) in phonetic_alphabet.iterrows() if row.letter in word_to_translate}

print(translated_word_dictionary)
