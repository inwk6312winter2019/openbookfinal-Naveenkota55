book_open=open("Book1.txt",'r')
book_open2=open("Book2.txt",'r')
book_open3=open("Book3.txt",'r')

unique_list1=[]
unique_list2=[]
unique_list3=[]
list_common=[]
i=0
for line in book_open:
	for word in line.split():
		if word not in unique_list1:
			unique_list1.append(word)
for line1 in book_open2:
        for word1 in line1.split():
                if word1 not in unique_list2:
                        unique_list2.append(word)
for line2 in book_open3:
        for word2 in line2.split():
                if word2 not in unique_list3:
                        unique_list3.append(word)


unique_list1==unique_list1.sort()
unique_list2=unique_list2.sort()
unique_list3=unique_list3.sort()
for items in unique_list1:
	if items in unique_list2 and unique_list3:
		list_common.append(items)
for items1 in unique_list1:
	my_dict[iems1]=i
	i+=1
print (mydict)
