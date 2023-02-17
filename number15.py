def finding_number_occurence(characters, string):
    count = 0
    for letters in string:
        if letters == characters:
            count += 1
    return count

answer = finding_number_occurence("t", "The greatest information you can get")
print(answer)

#to find the specific number of times each character occurs
