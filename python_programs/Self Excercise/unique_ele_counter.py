def element_frequency(elements):
    dict = {}
    #i = 0
    for i in elements:
        dict[i] = dict.setdefault(i , 0) + 1
        #i += 1
    return dict
        
        

# Test the function
result = element_frequency([1, 2, 3, 1, 2, 4, 5, 1, 2])
print(result)
# Output: {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}
