import requests
import json
import csv

response = requests.get('https://data.police.uk/api/crimes-street-dates')
print(response.status_code)

dict1 = response.json()
# print(dict1)
b = dict1[0].get('stop-and-search')
a = ','.join(b)
c = {'stop-and-search': a}
for data in dict1:
    data.update(c)
# print(dict1)
#
out_file = open("myfile.json", "w")

json.dump(dict1, out_file)

out_file.close()

with open('myfile.json') as json_file:
    jsondata = json.load(json_file)

data_file = open('jsonoutput.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

