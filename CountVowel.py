#Count vowel in a sentence

sentence = "My Name is Mukul Verma"
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
op = []

for i in sentence:
    if i in vowel:
        op.append(i)
    else:
        continue
print(op)
