# Loop else statement
# The else statement is executed after the loop has completed its execution
# The else statement is not executed if the loop is terminated by a break statement
# The else statement is not executed if the loop does not execute at all
# The else statement is not executed if the loop is terminated by an exception
# The else statement is not executed if the loop is terminated by a return statement
# This is not a common statement to use, but it is good to know that it exists
for i in range(3):
    print(f'Iteration {i}')
else:
    print('Loop completed')

while i > 0:
    i -= 1
    print(i)
else:
    print('Loop completed')
