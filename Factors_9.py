# Make a list of factors of a given number and write it.

def factors(n):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n/i)
        return factors
    
num = int(input("Enter a number :"))
print(f"The factors of {num} are: {factors(num)}")