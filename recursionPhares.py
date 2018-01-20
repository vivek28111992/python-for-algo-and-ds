
def word_split(pharse, list_of_words, output = None):

    if output is None:

        output = []

    for word in list_of_words:

        if pharse.startswith(word):

            output.append(word)
            print(len(word))
            return word_split(pharse[len(word):], list_of_words, output)

    return output

print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))