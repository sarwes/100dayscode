digit_c=int(input())
string=""
if digit_c%3==0 or '3' in str(digit_c):
  string=string+"Jugs"
if digit_c%5==0 or '5' in str(digit_c):
  string=string+"Mugs"
if digit_c%7==0 or '7' in str(digit_c):
  string=string+"Pugs"
print(string or str(digit_c))
  
