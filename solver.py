def solve(set_start, set_end):
    word_list_file = open("C:\\Users\\Dakota\\Weaver-Project\\Weaver-Solver\\words4.txt", "r") 
    file_words = word_list_file.read().split(", ")

    # Can use list comp here
    words = []
    for word in file_words:
        words.append(word[1:5])

    start = []
    start.append(str(set_start))
    end = str(set_end)
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
        # print("curr: ", curr)
        curr_word = curr[-1]
        if (curr_word == end):
            if (len(answer) == 0 or len(curr) < answer):
                answer = curr
                print(answer)
        matches = []
        
        # print("curr_word: ", curr_word)
        # loop through word list and add to matches if match
        for word in words:
            word = str(word)
            # if(word == "sinh"): print(True)
            if len(word) == 4 and word != curr_word:
                if word[1:] == curr_word[1:] and word not in matches:
                    matches.append(word)
                if word[0] + word[2:] == curr_word[0] + curr_word[2:] and word not in matches:
                    matches.append(word)
                if word[:2] + word[3] == curr_word[:2] + curr_word[3] and word not in matches:
                    matches.append(word)
                if word[:3] == curr_word[:3] and word not in matches:
                    matches.append(word)

        # remove each match from word list and add to queue
        for word in matches:
            next = []
            next = curr.copy()
            next.append(str(word))
            # print("next: ", next)
            # print(word)
            words.remove(word)
            q.append(next)

        count += 1

    return answer

def main():
    answer = solve(str(input('Enter first starting word: ')), input('Enter ending word: '))
    print("answer: ", answer, len(answer))

if __name__ == '__main__':
    main()
    
    

