counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, value in counties_dict.items():
    print(f"{county} county has {value:,} registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    for county, value in county_dict.items():
        print(f"{county} county has {value} registered voters")
        
