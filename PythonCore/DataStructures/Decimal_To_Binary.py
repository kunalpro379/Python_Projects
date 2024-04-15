from DataStructures.Stack import Stack
def DecToBin(decimal):
    stack=Stack()
    while decimal>0:
        rem=decimal%2
        stack.push(rem)
        decimal=decimal//2

    binary=""
    while not stack.is_empty():
        binary+=str(stack.pop())

    return binary
if __name__ == "__main__":
    decimal=int(input("Enter the decimal number: "))
    print("Binary equivalent of",decimal,"is",DecToBin(decimal))

