from collections import Counter

import subprocess


subprocess.run('cls', shell=True)



values = ["Äpple", "Päron", "Apelsin", "Päron", "Apelsin", "Apelsin"]   #lista

most_common_numbers = Counter(values)

most_common = most_common_numbers.most_common(1)[0]

print(most_common)


# print("mest vanlig namnet:", most_common[0])
# print("hur många av den mest vanliga:", most_common[1])


most_common_letters = Counter("abcbadfbcb").most_common(3)
print(most_common_letters)
