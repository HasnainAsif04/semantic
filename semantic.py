#importing nessecery modules
import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#One interesting thing about the similarities between "cat," "monkey," and "banana" 
#is that the similarity score between "cat" and "monkey" is higher than the score between "banana" and either "cat" or "monkey."
#This is likely because "cat" and "monkey" are both animals, while "banana" is a fruit.
#As for an example of my own, I could compare the similarity between "car" and "bicycle" versus the similarity between "car" and 
#"airplane." The score between "car" and "bicycle" might be higher than the score between "car" and "airplane" because they are both land vehicles, while an airplane is a different type of transportation altogether.