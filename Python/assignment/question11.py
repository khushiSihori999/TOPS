
# to check letter is vovel

letter=input("Enter your letter").lower()

if len(letter)!=1 or not letter.isalpha():
    print("Enter valid letter")

else:
    if letter in ['a','e','i','o','u']:
        print("letter is vowel")
    else:
        print("letter is not vowel")