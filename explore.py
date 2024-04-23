# iterative 'hello'
def hello(num):
    for i in range(1, num+1):
        print("hello", i)

# recursive 'hello'
def hello_rec(num):
    pass

# iterative 'sum'
def sum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i
    return sum

# recursive 'sum'
def sum_rec(num):
    pass



# TODO uncomment different lines
hello(5)
# hello_rec(5)
# print(sum(5))
# print(sum_rec(5))

