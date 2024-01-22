# iterative 'hello'
def hello(num):
    for i in range(1, num+1):
        print("hello", i)

# recursive 'hello'
def hello_rec(num):
    if num>1:
        hello_rec(num-1)
    else:
        print("base case reached, popping off stack...")

# iterative 'sum'
def sum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i
    return sum

# recursive 'sum'
def sum_rec(num):
    if num == 1:
        print("base case reached, popping off stack...")
        return 1
    else:
        return num + sum_rec(num-1)



# TODO uncomment different lines
hello(5)
# hello_rec(5)
# print(sum(5))
# print(sum_rec(5))

