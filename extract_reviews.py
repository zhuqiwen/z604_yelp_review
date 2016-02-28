import json


f = open(r"yelp_academic_dataset_review.json","r")
f_pos = open(r"positive_reviews","w")
f_neg = open(r"negative_reviews","w")
f_neu = open(r"neutral_reviews","w")
f_all = open(r"all_reviews","w")

for l in f:
	entry = json.loads(l)
	if entry['stars'] > 3:
		line = entry['text'].replace('\n','')+'\t'+'positive'+'\n'
		line = line.encode('utf8','replace')
		f_pos.write(line)
		f_all.write(line)
		# put review into positive set
	elif entry['stars'] < 3:
		line = entry['text'].replace('\n','')+'\t'+'negative'+'\n'
		line = line.encode('utf8','replace')
		f_neg.write(line)
		f_all.write(line)
		# put review into negative set
	else:
		# put review into neutral set
		line = entry['text'].replace('\n','')+'\t'+'neutral'+'\n'
		line = line.encode('utf8','replace')
		f_neu.write(line)
		f_all.write(line)

f.close()
f_pos.close()
f_neu.close()
f_neg.close()
f_all.close()