# Author RTS 3/16/22

# Defines function
def r_max(nested_num_lst):
    # Create for loop 
    for element in nested_num_lst:
        if type(element) == list:
            return max(element)
            
# Test
print(r_max([1, 2, 3, [45, 0]]))
