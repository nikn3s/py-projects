import csv
import os.path
if not os.path.isfile('artists.csv'):
    exit('1')

while True:
    artist = str(input('Enter an artist: '))
    song = str(input("Song Title: "))
    with open('artists.csv', mode='a', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['Artist', 'Song'])
        writer.writerow({'Artist':artist, 'Song':song})
    question = input('Do you want to enter another artist song? y/n ')
    if question == 'y':
        continue
    else:
        for row in csv.reader(open('artists.csv')):
            print(row[0], row[1])
        open('artists.csv').close()
        break

# In this project I got a deeper understanding of how to manage CSV files in python
# by creating a program that allows the user to enter artist and song names
# and then saves them to a csv file.