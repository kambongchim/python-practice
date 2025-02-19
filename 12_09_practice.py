#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big". 
# Example: make_it_big([-1, 3, 5, -5]) returns that same list, #changed to [-1, "big", "big", -5].

def BiggieSize(lis = []):
    for k,i in enumerate(lis):
        if i > 0:
            lis[k] = 'big'
    return lis
#print(BiggieSize([-1, 3, 5, -5]))

#Count Positives - Given a list of numbers, create a function to replace last value with number of 
# positive values. 
# Example, count_positives([-1,1,1,1]) changes list #to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).

def count_positives(lis = []):
    count = 0
    for i in lis:
        if i > 0:
            count += 1
    lis[len(lis) - 1] = count
    return lis

#print( count_positives([-1,1,1,1]))

#SumTotal - Create a function that takes a list as an argument and returns the sum of all the values in
#  the list.  For example sum_total([1,2,3,4]) should return 10

def sum_total(lis = []):
    return sum(lis)

#print(sum_total([1,2,3,4]))

#Average - Create a function that takes a list as an argument and returns the average of
#  all the values in the list.  For example multiples([1,2,3,4]) should return #2.5

def multiples(lis = []):
    return sum(lis) / len(lis)

#print(multiples([1,2,3,4]))

#Length - Create a function that takes a list as an argument and returns the length of the list. 
#  For example length([1,2,3,4]) should return 4

def length(lis = []):
    return len(lis)

#print(length([1,2,3,4]))


#Minimum - Create a function that takes a list as an argument and returns the minimum value in the list. 
#  If the passed list is empty, have the function return false.  #For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def minimum(lis = []):
    if len(lis) == 0:
        return False
    else:
        return min(lis)

#print(minimum([1,2,3,4]))
#print(minimum([-1,-2,-3]))

#Maximum - Create a function that takes a list as an argument and returns the maximum value in the list.  
# If the passed list is empty, have the function return false.  #For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def maximum(lis = []):
    if len(lis) == 0:
        return False
    else:
        return max(lis)

#print(maximum([1,2,3,4]))
#print(maximum([-1,-2,-3]))

#Ultimateaalyze - Create a function that takes a list as an argument and returns a dictionary that has the
#  sumTotal, average, minimum, maximum ad length of the list.

def Ultimateaalyze(lis = []):
    dic = {}
    dic['sumTotal'] = sum_total(lis)
    dic['average'] = multiples(lis)
    dic['minimum'] = min(lis)
    dic['maximum'] = max(lis)
    dic['length'] = len(lis)
    return dic

#print(Ultimateaalyze([1,2,3,4]))
#print(Ultimateaalyze([-1,-2,-3]))

#ReverseList - Create a function that takes a list as a argument and return a list in a reversed order. 
#  Do this without creating a empty temporary list.  For example #reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.

def reverse(lis = []):
    lis.reverse()
    return lis 

#print(reverse([1,2,3,4]))


#Ispalindrome- Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as string.
#  For example, “radar” is a palindrome, but “radix” is not a palindrome.

def palindrome(string = ''):
    string = string.lower()
    if string == string[::-1]:
        return True, 'Is palindrome'
    else:
        return False, 'Not palindrome'

#print(palindrome('radar'))
#print(palindrome('radix'))

#Fizzbuzz- Create a function that will print numbers from 1 to 100, with certain exceptions:
  #If the number is a multiple of 3, print “Fizz” instead of the number.
  #If the number is a multiple of 5, print “Buzz” instead of the number.
  #If the number is a multiple of 3 and 5, print “FizzBuzz” instead of the number.

def fizzBuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz', i)
        elif i % 3 == 0:
            print('Fizz', i)
        elif i % 5 == 0:
            print('Buzz', i)

#fizzBuzz()

#Fibonacci- The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, #starting from 0 and 1. That is,
  #F(0) = 0, F(1) = 1
  #F(n) = F(n - 1) + F(n - 2), for n > 1.
  #Create a function that accepts any number and will create a sequence based on the fibonacci sequence.

def Fibonacci(i = int):
    f0 = 0
    f1 = 1
    if i == 0:
        return f0
    elif i == 1:
        return f1
    else:
        return Fibonacci(i - 1) + Fibonacci(i - 2)
