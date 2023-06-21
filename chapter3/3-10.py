def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_dict = {}
    str2_dict = {}

    for char in str1:
        str1_dict[char] = str1_dict.get(char, 0) + 1

    for char in str2:
        str2_dict[char] = str2_dict.get(char, 0) + 1

    return str1_dict == str2_dict


print(is_anagram("cbaa", "aabc"))
