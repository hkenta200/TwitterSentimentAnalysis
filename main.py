import string
from collections import Counter

//obtain data / clean data
from matplotlib import pyplot as plt
text = open('readText.txt', encoding="utf-8").read()
lowerCase = text.lower()
cleanText = lowerCase.translate(str.maketrans('', '', string.punctuation))

//Transform data
tokenizedWords = cleanText.split()
print(tokenizedWords)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

finalWords = []
for word in tokenizedWords:
    if word not in stop_words:
        finalWords.append(word)

print(finalWords)

//Clean data
emotionList = []
with open('emotions.txt', 'r') as file:
    for ln in file:
        clearLn = ln.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clearLn.split(':')

        if word in finalWords:
            emotionList.append(emotion)

print(emotionList)
w = Counter(emotionList)
print(w)

//Visualize data
fig, axl = plt.subplots()
axl.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show()
