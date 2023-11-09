word= input('Enter a word: ')
Word= word.lower()
reversed_word= word[::-1]
word = word.replace(' ','')
if word==reversed_word:
    print('The word is a paindrome.')
else:
    print('The word is not a palindrome.')