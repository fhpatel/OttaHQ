import pandas as pd 

jobsArray = []
userDict = {}
user1 = []
user2 = []
count = 0

data = pd.read_csv("data/reactions.csv")

# Only need to consider entries where direction is true & drop any duplicate rows that may exist
subset = data.loc[data['direction'] == True]
subset = subset.drop_duplicates()
userIds = subset.user_id.unique()
for i in userIds:
    jobs = subset.job_id.loc[subset['user_id'] == i].tolist()
    if len(jobs) <= 1:
        continue
    userDict[i] = jobs
    jobsArray.append(jobs)


for x in range(len(jobsArray)):
    for y in range(x+1, len(jobsArray)):
        temp = list(set(jobsArray[x]) & set(jobsArray[y]))
        if(len(temp) > count):
            user1 = jobsArray[x]
            user2 = jobsArray[y]
            count = len(temp)

# Bad practice here to search through a dictionary by values instead of keys as there could be users with the 
# same entries  
print(list(userDict.keys())[list(userDict.values()).index(user1)])
print(list(userDict.keys())[list(userDict.values()).index(user2)])
print(count)



