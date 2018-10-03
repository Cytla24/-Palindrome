def Word(Wordx):
  return Wordx[::-1]

print("Hi! This code will tell you if your favourite word is a palindrome")
Word_a = input("type in any word!\n")
Word_b = Word(Word_a)

if Word_a == Word_b:
  print("Sweet! You have a palindrome.")
else:
  print("Sorry, you don't have a palindrome.")
