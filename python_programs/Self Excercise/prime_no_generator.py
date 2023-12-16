def generate_primes(limit):
    prime_list = []
    
    for i in range(2, limit + 1):
        is_prime = True
        for num in range(2, int(i ** 0.5) + 1):
            if i % num == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(i)
    return prime_list
   
            
        
limit = int(input())
# Test the function
result = generate_primes(limit)
print(result)
# Output: [2, 3, 5, 7, 11, 13, 17, 19]
