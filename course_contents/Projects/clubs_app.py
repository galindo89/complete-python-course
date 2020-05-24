import csv
import json

clubs_file=open("clubs.csv","r")
clubs_list=clubs_file.readlines()
clubs_file.close()
clubs_dict=[]
clubs_list=[lines.strip() for lines in clubs_list]
clubs_key=clubs_list[0].split(",")
clubs_list=[line.split(",") for line in clubs_list[1:]]


for club in clubs_list:
    club_dictionary={k: v for k, v in zip(clubs_key, club)}
    clubs_dict.append(club_dictionary)

club_json=open("clubs.json","w")

json.dump(clubs_dict,club_json)

club_json.close()

