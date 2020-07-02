#import csv
import json

with open("Campaigns.csv","r") as campaign_file:
    campaigns=campaign_file.readlines()
    campaigns_list=[line.strip().split(",") for line in campaigns[1:]]

#print(campaigns_list)

campaign_list_dictionary=[]

for campaign in campaigns_list:


    if not any(campaign[0] in campaign_dict for campaign_dict in campaign_list_dictionary):
        new_element={campaign[0]:[campaign[1]]}
        campaign_list_dictionary.append(new_element)
    else:
        for element in campaign_list_dictionary :
            if campaign[0] in element:
                element[campaign[0]].append(campaign[1])

print(campaign_list_dictionary)
gato=[]

for element in campaign_list_dictionary:
    for k in element:
        gato.append(k)

print(gato)





#keys=[k for k in element for element in campaign_list_dictionary]




#print(keys)

s="-"

new_dictionarly_list=[{k:s.join(v) for element in campaign_list_dictionary for k,v in element.items()}]

print(new_dictionarly_list)

#print(new_dictionarly_list)

with open("Campaigns_File.json","w") as file:
    json.dump(campaign_list_dictionary,file)






