word = input()
w_list = {}

def longest_substring(word):
    go = stay = count = 0
    while go < len(word):
        if word[go] not in w_list:
            w_list[word[go]] = 0
            count = max(len(w_list), count)
            go += 1
        else:
            del w_list[word[stay]]
            stay += 1
    return count

print(longest_substring(word))
