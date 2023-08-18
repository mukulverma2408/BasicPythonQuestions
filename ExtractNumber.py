#Extract Number from Text String that might contains float number as well

sentence = "I am 32.5 years old"
num = []

for word in sentence.split(" "):
    if not word.isalpha():
        num.append(float(word))
    else:
        continue

print(num)

