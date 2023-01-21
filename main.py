def FizzBuzz(num):
  if num % 3 == 0 and num % 5 == 0:
    return ('Fizzbuzz')
  elif num % 3 == 0:
    return ('Fizz')
  elif num % 5 == 0:
    return ('Buzz')
  else:
    return str(num)
 

print ('Pick a Number')
num = (int(input()))
for i in range(1, num + 1):
  print (FizzBuzz(int (i)))
