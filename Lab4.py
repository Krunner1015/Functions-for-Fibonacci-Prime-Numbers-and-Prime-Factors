def fibonacci(n):
    p1 = 0 #initiates the first value in the fibonacci sequence
    p2 = 1 #initiates the second value in the fibonacci sequence
    if n == 0:
        return p2
    for _ in range(1, n): #loops through the mathematical process to find the values of the fibonacci sequence up until the number inputted
        p1, p2 = p2, p1 + p2 #mathematical process to get the fibonacci values interchanging p1 and p2 and setting p2 equal to p1 + p2 without the need for a temporary variable
    return p1

def is_prime(n):
    if n < 2: #checks if the inputted value is less than two and returns false if so because no value less than two is prime
        return False
    for i in range(2, n): #iterates through every integer from 2 to n - 1 and returns false if n is divisible by that number
        if n % i == 0: #checks if n is divisible by the number assigned to i
            return False
    return True #returns true after checking all the conditions of none prime numbers, meaning the number is prime

def print_prime_factors(n):
    ogn = n #assigns the inputted value n to ogn so n can be modified and ogn be used in the print function along with the result
    factors = [] #initiates the list for all the prime factors
    if is_prime(n): #checks if the inputted value of n is prime using the is_prime function previously defined
        factors.append(n) #prints the value of n as the one and only prime factor of n since n is already prime
    else:
        while n % 2 == 0: #divides the value of n by two until it is no longer divisible by two, adding two to the list of prime factors each time
            factors.append(2)
            n = n // 2
        for i in range(3, n + 1, 2): #iterates through all the odd numbers from 3 to n
            while n % i == 0: #checks if n is divisible by the odd number i
                factors.append(i) #adds i to the prime factors list for every time n is divisible by i
                n = n // i
    result = " * ".join(map(str, factors)) #formats the integers in the list from being listed with commas to actually being multiplied
    print(f"{ogn} = {result}") #prints n along with its prime factors given the inputted value of n