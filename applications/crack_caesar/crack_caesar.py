# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open("ciphertext.txt") as f:
    words = f.read()


def count_letters(words):
    counted_letters = {}

    frequencies=['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    encrypted = {}

    decrypted_string = ''

    for c in words:
        if c.isspace() or not c.isalpha():
            continue

        c = c.upper()

        if c not in counted_letters:
            # counted_letters[c] = 0
            counted_letters[c] =1
            # continue
        else:
            counted_letters[c] += 1

    # return counted_letters

    # sort decreasing
    sorted_count = list(counted_letters.items())
    sorted_count.sort(key= lambda e: e[1], reverse=True)


    # swap key with value and put it back into a dictionary
    sorted_count = {key:value for key, value in sorted_count}

    # return sorted_count

    # make a key array
    key_arr = list(sorted_count.keys())

    for i in range(len(frequencies)):
        encrypted[key_arr[i]] = frequencies[i]

    # add last value as z 
    encrypted[key_arr[-1]] = frequencies[-1]

    # return encrypted
    # return key_arr

    for letter in words:
        if letter in key_arr:
            decrypted_string += encrypted[letter]
        if letter.isspace() or not letter.isalpha():
            decrypted_string += letter
        
    return decrypted_string

print(count_letters(words))

