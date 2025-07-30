#NESTED FUNCTION:A function within a function is called nested functions
def outerfunction():
    print("outer function statements")
    def innerfunction():
       print("inner function statements")       
    innerfunction()
outerfunction()   