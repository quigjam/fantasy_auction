# -*- coding: utf-8 -*-

import random
import csv


inst = 'n - for npc bid,b - for standard player bid, int for player bid, e - to end auction:  '
STANDARD_BID = 250

#opem file for names and budgets
#open file for items and prices

#make dictionaries for both


'''
want a system where fictional indviduals will bet versus players
they will they will give up at certain points

they will bet by a standard increment unless I can think of something better

they will bet off of oppurtunity cost = current price of the item / how much the item is worth 

however, some people value certain items differently, this modifies 

'''



auction_participants_fp = open("auction_participants.csv", "r")
auction_participants_reader = csv.reader(auction_participants_fp)

auction_items_fp = open("auction_items.csv", "r")
auction_items_reader = csv.reader(auction_items_fp)

'''
Item Catagories: 
    Combat Equipment
            Weapons
            Armor
            Staffs/ Wands
            
    Wonderous Items
        Spectacular Potions
        Things that do cool/unique things
        
    Relics
        Things that do not provide a direct benefit
        Give information or a plot thread
        Books/tomes
        Combat Equipment that has cultural value
        Weird items
 
'''

next(auction_participants_reader)

part_dict = {}

for line in auction_participants_reader:
    
    name = line[0]
    budget = int(line[1])
    
    ce_mod = int(line[2])
    wi_mod = int(line[3])
    re_mod = int(line[4])
    
    part_dict[name] = [budget,ce_mod,wi_mod,re_mod]
    
next(auction_items_reader)

item_dict = {}

for line in auction_items_reader:
    
    item_name = line[0]
    
    item_value = int(line[1])
    item_type  = line[2]    
    
    item_dict[item_name] = [item_value,item_type]    
    
    
def profit_check(highest_bid, item_list, part_list):
    
    item_type = item_list[1]
    value = item_list[0]
    
    if item_type == "CE":
        
        mod_value = part_list[1] * value
        
    elif item_type == "WI":
        
        mod_value = part_list[2] * value
    
    else:
    
        mod_value = part_list[2] * value
        
    op_cost = highest_bid / mod_value
    
    if op_cost > 1:
        
        return True
    
    else:
        
        return False
    
item_name_list = sorted(item_dict.keys())
name_list = sorted(part_dict.keys())

part_num = len(name_list)


winner_list = []

for item in item_name_list:
    
    bust_list = []
    bust_num = 0
    
    item_list = item_dict[item]
    item_value = item_list[0]
    item_type = item_list[1]
    
    inital_value = round((item_value * 0.75))
    highest_bid = inital_value
    ceiling = highest_bid + STANDARD_BID
    
    print("-----------------------------------------")
    print("New Auction!")
    print("-----------------------------------------")
    print("Item: ", item)
    print("Inital_Value: ", inital_value )
    if item_type == "CE":
            
        print("Item Type: Combat Equipment")
        
    elif item_type == "WI":
            
        print("Item Type: Wonderous Item")

    else:
            
        print("Item Type: Relic")
        

        
        
    
    winner = ""
    
    print("-----------------------------------------")
    print(inst)
    auction_input = input("Input: ")
    print("-----------------------------------------")
    while auction_input != "n" and auction_input != "b" and auction_input != "e" and auction_input.isdigit() == False:
        
        print("-----------------------------------------")
        print(inst)
        auction_input = input("Input: ")
        print("-----------------------------------------")
        
    
    while bust_num < part_num and auction_input != "e":
        
        
        
        
        if auction_input.isdigit():
        
            player_bid = int(auction_input)
            
            winner = "Player"
            highest_bid += player_bid
            
        elif auction_input == "b":
        
            winner = "Player"
            highest_bid += STANDARD_BID
            
        elif auction_input == "n":
            
            start_bid = highest_bid
            
            shuffled_names = name_list.copy()
            random.shuffle(shuffled_names)
            
            for name in shuffled_names:
                
                part_list = part_dict[name]
                budget = part_list[0]
                
                profit_value = profit_check(highest_bid, item_list, part_list)
                
                if name in bust_list or winner == name:
                    
                    continue
                
                elif ceiling > budget or profit_check == False:
                    
                    bust_list.append(name)
                    
                else:
                    
                    winner = name
                    highest_bid += STANDARD_BID
                    
                if highest_bid > start_bid:
                    
                    break
        
        ceiling = highest_bid + STANDARD_BID
        bust_num = len(bust_list)
        
        print(bust_list)
           
        print("-----------------------------------------")
        print("Item: ", item)
        print("Inital_Value: ", inital_value )
        if item_type == "CE":
            
            print("Item Type: Combat Equipment")
        
        elif item_type == "WI":
            
            print("Item Type: Wonderous Item")

        else:
            
            print("Item Type: Relic")
        
        print()
        print("Highest Bidder: ", winner)
        print("Current Bid: ", highest_bid)
        
        
        print("-----------------------------------------")
        print(inst)
        auction_input = input("Input: ")
        print("-----------------------------------------")
        
        
    
        while auction_input != "n" and auction_input != "b" and auction_input != "e" and auction_input.isdigit() == False:
        
            print("-----------------------------------------")
            print(inst)
            auction_input = input("Input: ")
            print("-----------------------------------------")
    
        
    
    
    
    print("-----------------------------------------")    
    print("Winner, Winner, Chicken Dinnner!" )
    print("-----------------------------------------")
    print("Item: ", item)
    print("Inital_Value: ", inital_value )
    if item_type == "CE":
            
        print("Item Type: Combat Equipment")
        
    elif item_type == "WI":
            
        print("Item Type: Wonderous Item")

    else:
            
        print("Item Type: Relic")
        
    print()
    print("Winner: ", winner)
    print("Price: ", highest_bid)

    winner_list.append((winner,item,highest_bid))
    
    if winner != "Player":
        
        budget = part_dict[winner][0] 
        adjusted_bid = budget - highest_bid
        part_dict[winner[0]] = adjusted_bid
        
print("-----------------------------------------")
print("Auction Finished! Thank You for Comming!")
print("-----------------------------------------")
print()

print("Winner List:")
print("-----------------------------------------")

print("{:20s}{:40s}{:<20s}".format("Winner","Item","Price"))
print("******************************************************************")

for winner in winner_list:

    print("{:20s}{:40s}{:<20d}".format(winner[0],winner[1],winner[2]))
    
print("******************************************************************")