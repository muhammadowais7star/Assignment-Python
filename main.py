{
"cells": [
{
"cell_type": "code",
"execution_count": 43,
"id": "8e8b0eb2-b33f-4ead-a71a-494d5c62efae",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"enter first number:  1\n",
"enter end number:  10\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"\n",
"Numbers between 1 and 10 devide by 4 or 6 (but not both):\n",
"4 6 8 "
]
}
],
"source": [
"#1. Numbers Divisible by 4 or 6 (But Not Both)\n",
"\n",
"start = int(input(\"enter first number: \"))\n",
"end = int(input(\"enter end number: \"))\n",
"print(f\"\\nNumbers between {start} and {end} devide by 4 or 6 (but not both):\")\n",
"for num in range(start,end + 1):\n",
"    if (num % 4 == 0 or num % 6 == 0) and not (num % 4 == 0 and num % 6 == 0):\n",
"        print(num, end=\" \")"
]
},
{
"cell_type": "code",
"execution_count": 45,
"id": "9c532c14-d582-431f-9031-7cd3fac6a0a3",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"Enter any string:  hello@1233\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"Letters: 5\n",
"Digits: 4\n",
"Special Characters: 12\n"
]
}
],
"source": [
"# 2. Count Digits, Letters, and Special Characters\n",
"\n",
"input_string = input(\"Enter any string: \")\n",
"letters = 0\n",
"digits = 0\n",
"special_characters = 0\n",
"for char in input_string:\n",
"    if char.isalpha():\n",
"        letters += 1\n",
"    elif char.isdigit():\n",
"        digits += 1\n",
"    else:\n",
"        special_chars += 1\n",
"\n",
"print(\"Letters:\", letters)\n",
"print(\"Digits:\", digits)\n",
"print(\"Special Characters:\", special_chars)"
]
},
{
"cell_type": "code",
"execution_count": 51,
"id": "55a121a7-4273-4d86-8132-e1ce7fd7b3f8",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
" Enter any sentence:  izaAN\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"lowercase 3\n",
"uppercase 2\n"
]
}
],
"source": [
"#3 Count Uppercase and Lowercase Letters\n",
"\n",
"input_sting = input(\" Enter any sentence: \")\n",
"lower_case = 0\n",
"upper_case = 0\n",
"for letter in input_sting:\n",
"    if letter.islower():\n",
"        lower_case += 1\n",
"    elif letter.isupper():\n",
"        upper_case += 1\n",
"print(\"lowercase\", lower_case)\n",
"print(\"uppercase\", upper_case)\n",
"        \n",
"        "
]
},
{
"cell_type": "code",
"execution_count": 6,
"id": "42a12d42-fc05-4fb3-9425-85642be875c1",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
" enter any letter: izan\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"orignalwords izan\n",
"remove_vowel *z*n\n"
]
}
],
"source": [
"#4. Replace Vowels with ‘*’\n",
"word = input(\" enter any letter:\")\n",
"vowels = \"aeiou\"\n",
"new_words = \"\"\n",
"for a in word:\n",
"    if a in vowels:\n",
"        new_words += \"*\"\n",
"    else:\n",
"        new_words += a\n",
"print(\"orignalwords\", word)\n",
"print(\"remove_vowel\",new_words)\n",
"        "
]
},
{
"cell_type": "code",
"execution_count": 23,
"id": "4c9dd1e2-8251-4800-949e-9c82842c52a0",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"enter any alphabet with number:  iz1343kankan\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"input iz1343kankan\n",
"sum_of_digit 11\n"
]
}
],
"source": [
"#5. Find Sum of Numbers Entered in a String\n",
"num_letters = input(\"enter any alphabet with number: \")\n",
"total = 0\n",
"\n",
"for a in num_letters:\n",
"    if a.isdigit():\n",
"        total += int(a)\n",
"      \n",
"print(\"input\", num_letters)\n",
"print(\"sum_of_digit\", total)\n"
]
},
{
"cell_type": "code",
"execution_count": 33,
"id": "3328c4ae-1d3b-4b47-8d54-1b9b5685630d",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
" enter any sentence: my name is izan hussain\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"sentense my name is izan hussain\n",
"words starting with vowels 2\n"
]
}
],
"source": [
"6# Count Words Starting with a Vowel\n",
"user_input = input(\" enter any sentence:\")\n",
"vowel = \"aeiou\"\n",
"words = sentence.split()\n",
"count = 0\n",
"for word in words:\n",
"    if word[0] in vowels:\n",
"        count += 1\n",
"print(\"sentence\", sentence)\n",
"print(\"words starting with vowels\", count) "
]
},
{
"cell_type": "code",
"execution_count": 39,
"id": "98ddd359-5392-4478-b727-3f41d9c729f7",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
" enter start number: 1 \n",
" enter end number: 10\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
" number between 1 and 10 sum of digit\n",
"2\n",
"4\n",
"6\n",
"8\n"
]
}
],
"source": [
"7# Display Numbers with Sum of Digits Even\n",
"\n",
"start = int(input(\" enter start number:\"))\n",
"end = int(input(\" enter end number:\"))\n",
"print(f\" number between {start} and {end} sum of digit\")\n",
"for num in range(start, end + 1):\n",
"    digit_sum = 0\n",
"    for digit in str(num):\n",
"        digit_sum += int(digit)\n",
"        if digit_sum %2 == 0:\n",
"            print(num)\n"
]
},
{
"cell_type": "code",
"execution_count": 53,
"id": "f4664581-36d5-4446-8cb4-51db5bc557f4",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"enter any string: banana\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"a: 3\n",
"b: 1\n",
"n: 2\n"
]
}
],
"source": [
"#8. Character Frequency (Sorted)\n",
"\n",
"\n",
"text = input(\"enter any string:\")\n",
"freq = {}\n",
"for a in text:\n",
"    if a in freq:\n",
"        freq[a] += 1\n",
"    else:\n",
"        freq[a] = 1\n",
"for a in sorted(freq.keys()):\n",
"     print(f\"{a}: {freq[a]}\")"
]
},
{
"cell_type": "code",
"execution_count": 62,
"id": "f4725b0e-a94a-4d2a-aa3e-8afee399206b",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"enter start number: 55\n",
"enter end number: 95\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
" number between 55 and 95 is digit 3:\n",
"63\n",
"73\n",
"83\n",
"93\n"
]
}
],
"source": [
"#9. Numbers Having 3 as a Digit\n",
"start = int(input(\"enter start number:\"))\n",
"end = int(input(\"enter end number:\"))\n",
"print(f\" number between {start} and {end} is digit 3:\")\n",
"for num in range(start, end + 1 ):\n",
"    if '3' in str(num):\n",
"        print(num)\n",
"        "
]
},
{
"cell_type": "code",
"execution_count": 72,
"id": "128ea168-1ad4-40b2-8c6c-381ee8916b58",
"metadata": {},
"outputs": [
{
"name": "stdin",
"output_type": "stream",
"text": [
"Enter start number:  1\n",
"Enter end number:  100\n"
]
},
{
"name": "stdout",
"output_type": "stream",
"text": [
"Numbers between 1 and 100 that satisfy all conditions:\n",
"16\n",
"30\n",
"32\n",
"52\n",
"56\n",
"76\n",
"78\n",
"92\n",
"100\n"
]
}
],
"source": [
"#10. Complex Divisibility with Digit Logic\n",
"\n",
"start = int(input(\"Enter start number: \"))\n",
"end = int(input(\"Enter end number: \"))\n",
"\n",
"print(f\"Numbers between {start} and {end} that satisfy all conditions:\")\n",
"\n",
"for num in range(start, end + 1):\n",
"    if (num % 4 == 0) ^ (num % 6 == 0):\n",
"        digit_sum = sum(int(d) for d in str(num))\n",
"        if digit_sum % 2 != 0:\n",
"            if num % 9 != 0:\n",
"                print(num)"
]
},
{
"cell_type": "code",
"execution_count": null,
"id": "0524ab1c-7887-4a5a-a894-9fc5d4d6b171",
"metadata": {},
"outputs": [],
"source": []
}
],
"metadata": {
"kernelspec": {
"display_name": "Python 3 (ipykernel)",
"language": "python",
"name": "python3"
},
"language_info": {
"codemirror_mode": {
"name": "ipython",
"version": 3
},
"file_extension": ".py",
"mimetype": "text/x-python",
"name": "python",
"nbconvert_exporter": "python",
"pygments_lexer": "ipython3",
"version": "3.13.5"
}
},
"nbformat": 4,
"nbformat_minor": 5
}
