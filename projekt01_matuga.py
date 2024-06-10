# """
# projekt_1.py: první projekt do Engeto Online Python Akademie

# author: Ľubomír Maťuga

# email: matugalubomir@gmail.com

# discord: Ľubomír Maťuga

# """
import sys
from task_template import TEXTS

users = {"bob":"123",
       "ann":"pass123",
        "mike":"password123",
        "liz":"pass123"
       }
user_name = input("username:")
user_password = input("password:")

if user_name in users and users[user_name] == user_password:
       print("----------------------------------------")
       print(f"Welcome to the app, {user_name}.\nWe have 3 texts to be analyzed.")
else:
       print("Unregistered user, terminating the program...")
       sys.exit()

print("----------------------------------------")

try:
       text_number = int(input("Enter a number btw. 1 and 3 to select: "))
       if text_number not in range(1,4) or text_number is str:
              print("Wrong input, terminating the program...")
              sys.exit()

except ValueError:
       print("Wrong input, terminating the program...")
       sys.exit()

print("----------------------------------------")

# CLEARING TEXT
clear_text=[]
for sign in (TEXTS[text_number - 1]):
       if sign.isalnum() or sign == " " or sign == "\n": 
              clear_text.append(sign)
join_text = "".join(clear_text)
final_text = join_text.split()

# TEXT STATISTICS
sum_words = (len(final_text))
print(f"There are {sum_words} words in the selected text.")

titlecase_words = []
for titlecase_word in final_text:
       if titlecase_word[0].isupper():
              titlecase_words.append(titlecase_word)
sum_titlecase_words = len(titlecase_words)
print(f"There are {sum_titlecase_words} titlecase words.")

uppercase_words = []
for uppercase_word in final_text:
       if uppercase_word.isupper() and uppercase_word.isalpha():
              uppercase_words.append(uppercase_word)
sum_uppercase_words = (len(uppercase_words))
print(f"There are {sum_uppercase_words} uppercase words.")

lowercase_words = []
for lowercase_word in final_text:
       if lowercase_word.islower() and lowercase_word.isalpha():
              lowercase_words.append(lowercase_word)
sum_lowercase_words = (len(lowercase_words))
print(f"There are {sum_lowercase_words} lowercase words.")

numerical_words = []
for numerical_word in final_text:
       if numerical_word.isnumeric():
              numerical_words.append(numerical_word)
num_words = (len(numerical_words))
print(f"There are {num_words} numeric strings.")

int_numerical_words = list(map(int,numerical_words))
sum_numerical_words = sum(int_numerical_words)
print(f"The sum of all the numbers {sum_numerical_words}.")

print("----------------------------------------")

# GRAPF OF WORDS LENGTH FREQUENCY
symbol = "*"
empty_sign = " "
len_words_list = []
len_words_dict = {}

for word in final_text:
       len_words_list.append(len(word))
len_words_set = (set(len_words_list))
max_length = max(len_words_list, key = len_words_list.count)
word_count_max_length = len_words_list.count(max_length)

print(f"""LEN|  OCCURENCES{(word_count_max_length - 10) * empty_sign}|NR.""")

print("----------------------------------------")

for number in len_words_set:
       len_words_dict[number] = len_words_list.count(number)
       if number < 10:
              print(f"""{2 * empty_sign}{number}|{len_words_list.count(number) * 
                     symbol + ((word_count_max_length + 2) - len_words_list.count(number)) * 
                     empty_sign}|{len_words_list.count(number)}""")
       else:
              print(f"""{empty_sign}{number}|{len_words_list.count(number) * 
              symbol + ((word_count_max_length + 2) - len_words_list.count(number)) * 
              empty_sign}|{len_words_list.count(number)}""")