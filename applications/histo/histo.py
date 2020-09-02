# Your code here
with open("robin.txt") as f:
    words = f.read()

def word_count(words):
    ignore = '":;,.-+=/\\|[]}{()*^&'

    for c in words:
        if c in ignore:
            words = words.replace(c, "")

    words_arr = words.lower().split()

    # find logest word for white space:
    longest_word = words_arr[0]
    i = len(words_arr) -1
    while i != 0 :
        if len(words_arr[i]) > len(longest_word):
            longest_word = words_arr[i]
        i -= 1



    cache = {}

    for word in words_arr:
        # check if word is in cache and add extra # to it
        if word in cache:
            cache[word] += '#'
        #  otherwise, word is not in cache
        else:
            cache[word] = '#'

    #  now we have a cache with counted #'s... need to sort it next
    # turn cache into a list
    cache_list = list(cache.items())
    # cache_list.sort() # sorts 
    # list.sort(reverse=True|False, key=myFunc) --> how sort() works like
    cache_list.sort(key=lambda e: e[1], reverse = True) # sort by values

    #  set up nice print
    for key, value in cache_list:
        # calculate white space
        white_space =' ' *( len(longest_word) - len(key) + 2) # 2 spaces after the longest word
        print(key +  white_space + value) 
    # print(cache_list[0][0] , key)
    # print(longest_word)

word_count(words)