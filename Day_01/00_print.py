"""So we are learn python from solving Problem like Mathematicals, condition, loop structure, Array
String, matrices , Recursive function and many more"""


""" Today focus point is  print , input, data type or Operator  we are learing from solving problem
not theory """

" Let's Start From Print"

# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)
# print function is used to print the output to the console
# *object means we can pass multiple arguments to the print function
# sep is used to separate the arguments with a space by default
# end is used to specify what to print at the end of the output, by default it is a new line
# file is used to specify the file where the output will be printed, by default it is sys.stdout
# flush is used to flush the output buffer, by default it is False


print("Hello","World", sep="--")  # prints Hello World
print("Hello", "World", end="!")  # prints Hello World!
print("Hello", "World", sep="--", end="!")  # prints Hello--World!
print("Hello", "World", sep="--", end="$$$", file=open("output.txt", "w"))  # prints Hello--World! to output.txt
print("Hello", "World", sep="--", end="!", flush=True)  # prints Hello--World! and flushes the output buffer
