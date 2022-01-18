counties = ["Arapahoe", "denver", "jefferson"]
counties.insert (1, "Elpaso")
print (counties)
counties.remove("Arapahoe")
print(counties)
counties.remove("denver")
counties.append("denver")
print (counties)
counties.append("Arapahoe")
print(counties)



list_dict={}
list_dict["a"] = 1
print (list_dict)

counties_dict ={}
counties_dict['arapahoe'] = 422829
counties_dict["denver"]=463353
counties_dict["jefferson"]=432438
print(counties_dict["arapahoe"])

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"denver","registered_voters":463353})
voting_data.append({"county":"jefferson","registered_voters":432438})
print (voting_data)
print (len(voting_data))
voting_data.insert(1,({"county":"elpaso","registered_voters":422829}))
print (voting_data)
voting_data.remove(({"county":"Arapahoe","registered_voters":422829}))
print(voting_data)
voting_data.remove(({"county":"denver","registered_voters":463353}))
print(voting_data)
voting_data.append({"county":"denver","registered_voters":463353})
print(voting_data)
voting_data.append({"county":"Arapahoe","registered_voters":422829})
print (voting_data)


# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")










































































