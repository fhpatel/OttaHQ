import pandas as pd

usersArray = []
companiesDict = {}
count = 0

jobsCSV =  pd.read_csv('data/jobs.csv')

data = pd.read_csv('data/reactions.csv')

subset = data.loc[data['direction'] == True]

# print(subset)
# print(jobsCSV)

mergedSet = pd.merge(subset, jobsCSV, left_on='job_id', right_on='job_id')

# print(mergedSet.loc[mergedSet['user_id']== 7038])

companyIds = mergedSet.company_id.unique()

# print(companyIds)
for i in companyIds:
    users = mergedSet.user_id.loc[mergedSet['company_id'] == i]
    users = users.drop_duplicates().tolist()
    if(len(users) < 2):
        continue
    companiesDict[i] = users
    usersArray.append(users)

for x in range(len(usersArray)):
    for y in range(x+1, len(usersArray)):
        temp = list(set(usersArray[x]) & set(usersArray[y]))
        if(len(temp) > count):
            company1 = usersArray[x]
            company2 = usersArray[y]
            count = len(temp)

print(list(companiesDict.keys())[list(companiesDict.values()).index(company1)])
print(list(companiesDict.keys())[list(companiesDict.values()).index(company2)])
print(count)

