# Complete the function below.

def  encode_string(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vow = ''.join([c for c in s if c not in vowels])
    #print(no_vow)
    no_dups = list()
    for i in no_vow:
        if i not in no_dups:
            no_dups.append(i)
    #print(no_dups)
    #a - 97 ord() - 96
    final_list = list()
    for i, ch in enumerate(no_dups):
        if i == len(no_dups) - 1:
            new_char = (ord(ch) - 96 + ord(no_dups[0]) - 96)
            if new_char > 26:
                new_char = new_char % 27 + 1
        else:
            new_char = (ord(ch) - 96 + ord(no_dups[i + 1]) - 96)
            if new_char > 26:
                new_char = new_char % 27 + 1
        new_char = chr(new_char + 96)
        final_list.append(new_char)
    #print(''.join(final_list))
    final_str = ''.join(final_list)
    return final_str

