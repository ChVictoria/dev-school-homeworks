def groupAnagrams(arr):
    flag = False
    result = []
    for word in arr:
        for group in result:
            if all([letter in group[0] for letter in word]) and len(group[0])==len(word):
                group.append(word)
                flag = True
                break
        if not flag:
            result.append([word])
        flag = False
    return result

print(groupAnagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]))