a=int(input())
string=""
if a%3==0:
  string=string+"Jugs"
if a%5==0:
  string=string+"Mugs"
if a%7==0:
  string=string+"Pugs"
print(string or str(a))
  
