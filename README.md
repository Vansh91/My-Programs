# Basic_Python_Programs
- Check if the user input is palindrome or not:

def palindromeMethod():
  user_input = list(input('enter a word or list:'))
  a = []
  for i in user_input:
    a.append(i)
  if a == list(reversed(a)):
    print('Yes this is a palindrome')
  else:
    print('No this is not a plaindrome')
    
- 
