# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_word="true"
love_word="love"
true_count=0
love_count=0
combined_name = name1.lower() + name2.lower()

true_count += combined_name.count(true_word[0])
true_count += combined_name.count(true_word[1])
true_count += combined_name.count(true_word[2])
true_count += combined_name.count(true_word[3])

love_count += combined_name.count(love_word[0])
love_count += combined_name.count(love_word[1])
love_count += combined_name.count(love_word[2])
love_count += combined_name.count(love_word[3])

love_score = str(true_count) + str(love_count)
love_score = int(love_score)

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")