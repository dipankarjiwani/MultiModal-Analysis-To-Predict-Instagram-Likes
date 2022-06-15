import csv
import json
import os
from datetime import datetime
import statistics

image_data = '.\image_data'
profiles = '.\profiles'

rows = []
rootdir = 'C:\\Users\\rachi\\OneDrive\\Desktop\\Sem 6\\ML\\Project\\image_data'

#iterate through images
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # print("Subdir: ", subdir)
        # print("\n")
        # print("File: ", file)
        # print("\n")
        # print(os.path.join(subdir, file))
        username = subdir.split('\\')[-1]
        # print("Username: ", username)

        filename = file[:-4]
        # print("Filename: ", filename)

        # Opening JSON file
        with open('.\profilesFull\\'+username+'.json', encoding='utf8') as json_file:
            data = json.load(json_file)
            #add user metadata
            row_data = [data['alias'], data['username'], data['descriptionProfile'], data['website'], data['numberPosts'], data['numberFollowers'], data['numberFollowing'], data['private']]
            
            #add post data
            posts = data['posts']
            i = 0
            for post in posts:
                if post['filename'] == filename:
                    row_data.append(post['isVideo'])
                    row_data.append(post['multipleImage'])
                    row_data.append(post['tags'])
                    row_data.append(post['mentions'])
                    row_data.append(post['description'])
                    row_data.append(post['localization'])
                    row_data.append(post['date'])
                    row_data.append(post['numberLikes'])
                    row_data.append(filename+".png")
                    k = 1
                    j = i+1
                    sumPrevious10Likes = 0
                    previous10Likes = []
                    while j<len(posts) and k<11:
                        sumPrevious10Likes += posts[j]['numberLikes']
                        previous10Likes.append(posts[j]['numberLikes'])
                        k += 1
                        j += 1
                    
                    row_data.append(sumPrevious10Likes/k)
                    row_data.append(statistics.stdev(previous10Likes))
                    
                    k = 1
                    j = i+1
                    sumPrevious3Likes = 0
                    previous3Likes = []
                    while j<len(posts) and k<4:
                        sumPrevious3Likes += posts[j]['numberLikes']
                        previous3Likes.append(posts[j]['numberLikes'])
                        k += 1
                        j += 1
                    
                    row_data.append(sumPrevious3Likes/k)
                    row_data.append(statistics.stdev(previous3Likes))

                    today_date = datetime.strptime(post['date'][:10], "%Y-%m-%d")
                    last_date = datetime.strptime(posts[-1]['date'][:10], "%Y-%m-%d")
                    diff_days = (today_date-last_date).days
                    num_posts = len(posts) - i
                    avg_posts_weekly = (num_posts/(diff_days+0.001))*7
                    row_data.append(avg_posts_weekly)

                    rows.append(row_data)
                    # print("Row Data: ", row_data)
                    break
                i += 1

# print(rows)

fields = ['alias', 'username', 'descriptionProfile', 'website', 'numberPosts', 'numberFollowers', 'numberFollowing', 'private', 'isVideo', 'multipleImage', 'tags', 'mentions', 'description', 'localization', 'date', 'numberLikes', 'filename', 'avgPrevious10Likes', 'stdPrevious10Likes', 'avgPrevious3Likes', 'stdPrevious3Likes', 'avgPostsWeekly']
csv_filename = 'dataset.csv'

# writing to csv file 
with open(csv_filename, 'w', encoding='utf-8') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
    
    # writing the data rows 
    csvwriter.writerows(rows)
        

                    



            


        
