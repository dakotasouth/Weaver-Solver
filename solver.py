
word_list_file = open("C:\\Users\\Dakota\\Weaver-Project\\Weaver-Solver\\words4.txt", "r") 
file_words = word_list_file.read().split(", ")

# Can use list comp here
words = []
for word in file_words:
    words.append(word[1:5])

start = []
start.append(str(input('Enter first starting word: ')))
end = input('Enter ending word: ')
words.remove(start[0])
# print("start type: ", type(start))
# print("start: ", start)
q = []
q.append(start)
# print("q type: ", type(q))
# print("q: ", q)
answer = []
count = 0

while (len(q) > 0):

    # pop next word and see if it is the answer
    curr = q.pop(0)
    # print("curr type: ", type(curr))
    # print("curr: ", curr)
    curr_word = curr[-1]
    if (curr_word == end):
        answer = curr
        print("Answer found")
        break
    matches = []
    
    # print("curr_word type: ", type(curr_word))
    print("curr_word: ", curr_word)
    # loop through word list and add to matches if match
    for word in words:
        word = str(word)
        if len(word) == 4 and word != curr_word:
            if word.replace(word[0],'') == curr_word.replace(curr_word[0],''):
                matches.append(word)
            if word.replace(word[1],'') == curr_word.replace(curr_word[1],''):
                matches.append(word)
            if word.replace(word[2],'') == curr_word.replace(curr_word[2],''):
                matches.append(word)
            if word.replace(word[3],'') == curr_word.replace(curr_word[3],''):
                matches.append(word)

    # remove each match from word list and add to queue
    # print(matches)
    for word in matches:
        next = []
        next = curr.copy()
        next.append(str(word))
        print(next)
        # print("next type: ", type(next))
        # print("next: ", next)
        words.remove(word)

        q.append(next)
    count += 1

print("answer: ", answer)


    
    

