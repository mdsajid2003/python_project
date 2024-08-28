import math
def cal():
 # accepting the number
  expr = input("enter the number with the number")
  if expr[1] == ' ':
 #splitting the string
 
   a,o,b = (expr).split()
   # checking whether the string is less then 7 or not
   if len(a) >= 7 or len(b) >= 7 :
     print("number is greater then a")
   else:
  # converting it into floating type
    a,b = float(a),float(b)
  # checking the operators
    if o == '+':
      sum = a + b
      return sum
    elif o == '-':
     sum = a - b
     return sum
    elif o == '*':
     sum = a * b
     return sum
    elif o == '/' or o == '//':
     if b == 0:
        print("Number should be greater then 0")
     else:
        sum = a // b
        return sum
    elif o == '**':
     sum = a ** b
     return sum
    elif o == 'log':
    # a and b cannot be negative
     if a<=0 or b<=0:
       print("error")
       return None
     else:
       sum = math.log(a,b)
       return sum
    else:
     print("Error operator")
  else:
    return eval(expr) 
  
# calling the function and storing the sum into tot
tot = (cal())
# printing the value sum that is returned from the function cal
print(tot)
