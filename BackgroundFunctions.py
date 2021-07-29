def num_names(player_name):
    count=1
    for i in range(0,len(player_name)):
        if player_name[i] == " ":
            count+=1
    return count