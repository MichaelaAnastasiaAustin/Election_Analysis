print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
for county in counties:
    print(county)
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values ():
    print(voters)
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
candidate_votes = int(input("how many votes did the candidate get in the election?" ))
total_votes = int(input("what is the total number of votes in the election?" ))
message_to_candidate = (
    f"You recieved {candidate_votes:,} number of votes. " 
    f"The total number of votes in the election was {total_votes:,}. "
    f"You recieved {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 4324438}]
for county, voters in voting_data.values():
    print((f"{county} county has {voters:,} registered voters."))