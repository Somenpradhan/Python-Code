#Ask the user to enter her mobile number
#make a list of unique present in the numebrs
#make another list 'b' which consist of the digits not present in the number
#create a square matrix of all prime numbers less than min number that can be formed using the digits present in b(append 0 if required)
#find all the diagonal elements of the square matrix
#replace all the values greater than the avg value with 1 and others with 0


import math
import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    mobile_number = input("Enter her mobile number: ")
   
    unique_digits = list(set(mobile_number))
    print(f"Unique digits in the mobile number: {unique_digits}")
    
    all_digits = set("0123456789")
    digits_not_in_number = list(all_digits - set(unique_digits))
    print(f"Digits not present in the mobile number: {digits_not_in_number}")
    
    digits_not_in_number.sort()
    min_number = int("".join(digits_not_in_number))
    print(f"Minimum number that can be formed: {min_number}")
    
    primes = [x for x in range(min_number) if is_prime(x)]
    print(f"Primes less than {min_number}: {primes}")
    
    matrix_size = int(len(primes) ** 0.5)
    primes = primes[:matrix_size ** 2]
    square_matrix = np.array(primes).reshape(matrix_size, matrix_size)
    print("Square matrix of primes:")
    print(square_matrix)
    
    diagonals = np.concatenate([np.diagonal(square_matrix), np.diagonal(np.fliplr(square_matrix))])
    print(f"Diagonal elements: {diagonals}")

    avg_value = np.mean(diagonals)
    print(f"Average of diagonal elements: {avg_value}")
    
    replaced_matrix = np.where(square_matrix > avg_value, 1, 0)
    print("Replaced matrix:")
    print(replaced_matrix)

if __name__ == "__main__":
    main()
