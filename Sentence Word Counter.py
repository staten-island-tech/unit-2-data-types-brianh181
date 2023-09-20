sentence=input("Say something.")

def wordsInSentence(sentence):
    Words=sentence.split()
    WordNum=0

    for i in range(Words):
        WordNum += 1
    


wordsInSentence(sentence)

print("there are "+WordNum" words in this sentence.")