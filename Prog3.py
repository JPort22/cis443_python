# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 21:57:42 2021

@author: Grading ID: P9941
"""

#first part - getting input and making the list of 
first_roster = input("Please enter the jersey number and the power rating for the player(s):")#input to get first roster of players
split_roster = first_roster.split() #splits roster by spaces entered - tokenize
roster_dict = {} #roster
str_len = len(split_roster)#makes variable for length of split_roster
if str_len % 2 == 1:#validation for checking for pairs
    str_len -= 1 #gets rid of odd number out - a number without a partner
    
i = 0 #index is 0
while i < str_len: #while index is less than the length of tokenized roster
    key = int(split_roster[i]) #keys is player jersey number
    val = int(split_roster[i + 1]) #values is player power rating
    if (0 <= key <= 99 and 1 <= val <= 10):#if statement for checking the key in range and value in range
        roster_dict[key] = val #fills roster dictionary with key and val
    i += 2 #index going up by 2 for pairing
print(roster_dict) #prints roster dictionary after validation

next_task = input("Please enter letter for corresponding menu task:")#line of input to begin menu
while next_task != 'q':
    next_task = input("Please enter letter for corresponding menu task:")#line of input to begin menu
    
    if next_task == 'a':#a is for adding a player
            add_player = input("Please enter jersey number and power rating for player:")#add player input
            add_split = add_player.split() #splits jersey and power
            i = 0 #making index start at 0 again
            key = int(add_split[i])#taking index 0 making it key
            val = int(add_split[i + 1])#taking index 1 and making it value
            if (0 <= key <= 99 and 1 <= val <= 10):#if statement for checking the key in range and value in range
                roster_dict[key] = val #fills roster dictionary with key and val
    print(roster_dict)#prints roster dictionary with added player 
    
    if next_task == 'd':#d is for deleting player
        remove_player = int(input("Please enter jersey number of player you wish to remove:"))#delete player input
        if remove_player in roster_dict:#if remove player input is in roster dictionary
            del roster_dict[remove_player]#delete that player from dictionary
        print(roster_dict)#prints roster dictionary
        
    if next_task == 'u':# u is update player in dictionary
        update_player = int(input("Please enter existing player jersey number:"))#update player user input
        new_power = int(input("Please enter new power rating for player:"))#new power for player
        if update_player in roster_dict:#for jersey whoever in roster dictionary
            if 1 <= new_power <= 10:# if new power rating entered is between 1 and 10 inclusively
                roster_dict[update_player] = new_power#new power rating assigned to that jersey number
        print(roster_dict)#print roster dictionary
        
    if next_task == 'r': #r is for outputting players that are above user given power rating
       rating_player = int(input("Please enter minimum rating for players:"))#power rating comparison input
       for key in roster_dict.keys():#for key in roster dictionary keys
           if roster_dict[key] >= rating_player:#if power rathing threshold is less than or equal to
               print(key, roster_dict[key])#print key and value or jersey number and power rating
   
    if next_task == 'o': #o is for outputting roster as a table
        print("Jersey      Power Rating")#column headers
        print("-------     ------------ ")#column separators
        for key in sorted(roster_dict.keys()):#for key in sorted ascending list of roster dictionary keys or jersey numbers
            print(f' {key:5} {roster_dict[key]:8}')#formatted output for jersey number and power rating
            
    if next_task == 'q':#if menu choice is q
        quit()#quit program