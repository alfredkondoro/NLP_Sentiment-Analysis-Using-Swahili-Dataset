import string

#to read the input from the selected text file
input_text = open('input.txt', encoding='utf-8').read()

#to change the selected text into lowercase and remove the punctuation
lowercase_text = input_text.lower()
punctless_text = lowercase_text.translate(str.maketrans('','',string.punctuation))

#to split the lumps of word into small tokens
token_words = punctless_text.split()

#to filter off the words that are not to be learnt by the machine
stop_words = []
with open ('stopwords.txt','r') as file:
    for line in file:
        formatted_line = line.replace('\n','').replace('"','').replace(',','').strip()

        stop_words.append(formatted_line)

final_words = []
for word in token_words:
    if word not in stop_words:
        final_words.append(word)

#to finally group the word in correspondance to the emotion
emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

