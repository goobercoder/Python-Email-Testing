def function(func):
    def wrapper():
        print("hello")
        func()
        print("onain")
    return wrapper

@function
def goog():
    print("goog")


goog()