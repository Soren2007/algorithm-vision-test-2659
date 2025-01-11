
n = int(input(""))

q_text = input("")

s_text = input("")

incorrect_number = 0

for i in range(n):
    if q_text[i] != s_text[i]:
        incorrect_number += 1

print(incorrect_number)