def count_change(money,coins):
    Num_ways = [0]*(money+1) # Creating an array of zeros
    Num_ways[0]=1 
    for current_coin in coins: # Iteration to consider each denomination
        for value in range(0,len(Num_ways),1): # Iteration for the total value
            if (value>=current_coin):
                Num_ways[value]+=Num_ways[value-current_coin] # To calculate the number of combinations
    return Num_ways[money]

print("The number of combinations are %d " %count_change(4, [1,2]))
print("The number of combinations are %d " %count_change(10, [5,2,3]))
print("The number of combinations are %d " %count_change(11, [5,7]))

