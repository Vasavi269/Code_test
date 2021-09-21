def reduce_directions(directions: list) -> list:
    print("The given directions are: %s" %directions)# Original directions

    # Initial Conditions
    old_length = len(directions)
    new_length = 0

    while old_length != new_length:# This loop ends when no further reduction can be made
        old_length = len(directions)
        for i in range(len(directions)-1):
            # To check if the adjacent directions are opposite
            if ((directions[i]=="NORTH" and directions[i+1]=="SOUTH") or (directions[i]=="SOUTH" and directions[i+1]=="NORTH") or (directions[i]=="EAST" and directions[i+1]=="WEST") or (directions[i]=="WEST" and directions[i+1]=="EAST")):
                # Removing the directions from the list
                del directions[i]
                del directions[i]
                break # Breaks when changes are made to the list of directions and starts over
        new_length = len(directions)    
    return directions # Returns the reduced list of directions

print("The reduced directions are: %s" %reduce_directions(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","WEST"]))
print("The reduced directions are: %s" %reduce_directions(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"]))
print("The reduced directions are: %s" %reduce_directions(["NORTH","WEST","SOUTH","EAST"]))
print("The reduced directions are: %s" %reduce_directions(["NORTH","SOUTH","EAST","EAST","WEST"]))