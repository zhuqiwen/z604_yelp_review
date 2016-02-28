import json
import pprint
# n = int(raw_input('which review you want to see: '))
n = int(raw_input('how many negtive reviews you want to see: '))

print
f = open(r"/Users/zqw/Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json","r")
# for l in f:
# 	pprint.pprint(l)
# data_list=[l for l in f]

# pprint.pprint(data_list[0])
# print len(data_list)

# for i in range(n):
line = "XXX"
cnt = 0
while line and cnt < n:
	line = f.readline()
	d_j = json.loads(line)
	if d_j['stars'] <=3:
	# if i == n-1:   # this is for only displaying one review.
		pprint.pprint(d_j)
	# print 
	# print
		cnt += 1

f.close()