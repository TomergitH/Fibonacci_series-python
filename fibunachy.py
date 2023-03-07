num = int(input("Enter a number: "))

def f(n):
        print(0)
        if n <= 1:
            return 0
        else:
            x, y = 0, 1
            for i in range(n):
                x, y = y, x + y
            
                print(x)

f(num - 1)
