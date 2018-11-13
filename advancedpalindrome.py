def bigboypalindrome(string_a):
  string_a = string_a.lower()
  i = 0
  j = len(string_a) - 1

  while i < j:
    if Ignore(string_a[i]):
      i += 1
    if Ignore(string_a[j]):
      j -=1
    if string_a[i] == string_a[j]:
      i += 1
      j -= 1
    else:
      return "False"
  return "true"
  


def Ignore(char):
  return char < 'a' or char > 'z'


print(bigboypalindrome("taco.ca,t"))
