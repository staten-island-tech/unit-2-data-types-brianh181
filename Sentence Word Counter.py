sentence=input("Say something.")
WordNum=0 

def wordsInSentence(sentence):
    Words=sentence.split( )
    WordNum=len(Words)

    
    return WordNum

wordsInSentence(sentence)

print(WordNum)
print(("There are ") ((WordNum)) ("in this sentence."))
