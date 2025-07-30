"""
Looping statements are also called as iterative statements

These statements are used to run a particular condition
no.of times...
they are broadly divided into two types
1. While
2.For
"""
#while: it executes when the condition is true
"""
syntax: while condition :
            statements
            exit condition/incrementation
"""
#eg:
i=1
while i<=10:
    #print(i)--> in this particular line the
    #"i" value runs "n" times because no incrementation/exit cond specific 
    print("the value",i)
    i+=1

    #eg2
    while True:
        print ("the while condition")
    #Note: As default condition is True te while loop runs "infinity"times


    #eg:3
    #while False:
        #print("the while condition")
    #As while is also called entry control
    # loop it just checks the condition in the entrace
    # as default False is given as condition it won't execut
