word_list_file = open("C:\\Users\\Dakota\\Weaver-Project\\Weaver-Solver\\words4.txt", "r") 
file_words = word_list_file.read().split(", ")

# Can use list comp here
words = []
for word in file_words:
    words.append(word[1:5])


start = input('Enter first starting word: ')
end = input('Enter ending word: ')
curr = start
words.remove(start)

while(curr != end):
    options = []
    for word in words:
        if len(word) == 4 and word != curr:
            if word.replace(word[0],'') == curr.replace(curr[0],''):
                options.append(word)
                words.remove(word)
            if word.replace(word[1],'') == curr.replace(curr[1],''):
                options.append(word)
                words.remove(word)
            if word.replace(word[2],'') == curr.replace(curr[2],''):
                options.append(word)
                words.remove(word)
            if word.replace(word[3],'') == curr.replace(curr[3],''):
                options.append(word)
                words.remove(word)
    print(options)
    curr = input('select word: ')
