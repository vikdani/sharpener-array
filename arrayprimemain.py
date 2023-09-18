def prime_number(n):
    array = []
    primearray=[]
    for i in range(1, n+1):
        array.append(i)
    counter = 0
    x = 2
    while counter < n:
        prime = True
        for j in range(2, x):
            if x % j == 0:
                prime = False
                break
        if prime:
            primearray.append(x)
            counter += 1
        x = x + 1
    return primearray

def main():
    n = int(input("number: "))
    output = prime_number(n)
    for i in range(0, n):
        
        print(output[i])

main()