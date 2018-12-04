import time
from efficient_apriori import apriori


edits_per_user = []

file = open('data/itemsets3mil.txt','r+')
for line in file:
    line = line[:-1]
    user, pages = line.split('", ')
    pages = pages[:-1]
    pages = [page.replace(' ','') for page in pages.split(",")]

    user = user.replace('"', '')

    pages = tuple(pages)
    
    edits_per_user.append(pages)

print("done reading data ")
unique_users = [400, 300, 200,100,90,80,70,60,50,40,30,25,20,15,10,9,8,7,6,5,4,3,2,1]

for user in unique_users:
	support = user/22600.0
	t1 = time.time()
	itemsets, rules = apriori(edits_per_user, min_support=support, 
							 min_confidence=0.5, max_length = 2)
	

	print("support: ", user, support)
	print("time: ", time.time() - t1)
	print("itemsets: ", len(itemsets[1]) + len(itemsets[2]))
	print("rules: ", len(rules))
	print()