#assuming asking for only one book

book_open=open("Book1.txt",'r')

def unique_words(book):
	unique_list=[]
	for line in book:
		for word in line.split():
			if word not in unique_list:
				unique_list.append(word)
	print (unique_list)
#question not clear... so just counting the elements in given list and return integer
def count_the_article():
	list1= ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
	return (len(list1))



#assuming the words in unique_list
def sorted_words(book):
	sorted_list=[]
        for line in book:
                for word in line.split():
                        if word not in sorted_list:
                                sorted_list.append(word)
				sorted(sorted_list)
	print (sorted_list)

def character_word_count(book):
	my_dict={}
	list1=[]
	book_copy=book
	for line in book:
                for word in line.split():
                        if word not in list1:
				list1.append(word)
	for list_words in list1:
		count=0
		for lines in book_copy:
                	for word1 in lines.split():
				if word1==list_words:
					count+=1
		my_dict[list_words]=count
	print (my_dict)

def starts_with_vow(book):
	count =0
        for line in book:
                for word in line.split():
                        if word[0] in ("a","e","i","o","u"):
				count=count+1
	return (count)


#unique_words(book_open)
#print (count_the_article())
#sorted_words(book_open)
#character_word_count(book_open)
print(starts_with_vow(book_open))
