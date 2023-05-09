# Write a Python program that takes a list of strings as input and outputs
#  the number of times each string appears in the list, using a dictionary and conditional statements.
def occurence_string(list):
    count=dict()
    for string in list:
        if string in count:
            count[string]+=1
        else:
            count[string]
            return count
    print(occurence_string("The tall man met a short man in the streets"))
# Write a Python program that takes a list of numbers as 
# input and outputs the median of the numbers 
def median(numbers):
    for number in numbers:
       return number
print(median([1,2,3,4,5,6,7,8,9]))
# Write a Python program that takes a list of numbers as input and 
# outputs the second largest number in the list using conditional statements and a for loop.
def second_largest_number(numbers):
    second_largest_number=numbers[::-1]
    return second_largest_number
print(second_largest_number([12,23,45,14,56,78,98]))


# Write a Python program that takes a year as input and determines if it is a leap year.
def year(int):
  if year%4==0:
   year=int(2004)
   print("The year is a leap year")
  else:
   print("the year is not a leap year")
# Write a Python program that takes a string as input and checks if it
#  is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.
def check_palindrome(string):
   string="dad"
   return string==string[::-1]
string=check_palindrome
if string==check_palindrome:
    print("is palindrome")
else:
    print("not palindrome")
check_palindrome(string)