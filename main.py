n = int(input("Number of letters : >>> "))

q_text = input("Number of letters in the question word : >>> ")

s_text = input("Number of letters in the student's answer word : >>> ")

incorrect_number = 0

for i in range(n):
    try:
        
        if q_text[i] != s_text[i]:
            incorrect_number += 1
    except IndexError:
        print("The number of letters in the question is not equal to the input.")
        break

print(f"Number of wrong letters : {incorrect_number}")