import json
import re
import time
import datetime

lines = []
times = []

ts=0

start = datetime.datetime.now()
y = "/home/sharan/Files/Output"+str(ts)+".txt"
text_file = open(y)

for i in text_file.readlines():
    lines.append(i)

lines = [i for i in lines if (i != '\n')]

books_author = []

for i in range(88, len(lines)):
    books_author.append(lines[i])

books_author_remove_space = [i.replace("\n", "") for i in books_author]
# print(len(books_author_remove_space)) len = 6773
books_author_remove_space.append("1234")  # last element

dict = {}

for i in range(len(books_author_remove_space) - 1):

    if (re.search('[0-9]+[A-Z]*$', books_author_remove_space[i])):
        x = ""
        sp = books_author_remove_space[i].split()
        number = sp.pop()
        sp = " ".join(sp)
        x = x + sp
        j = i + 1

        while ((not re.search('[0-9]+[A-Z]*$', books_author_remove_space[j]))):
            x = x + books_author_remove_space[j]
            j = j + 1
        dict[number] = x

remove_lang_and_brackets = {}

for i in dict:
    lang = re.search('\[L', dict[i])

    if (not lang):
        remove_lang_and_brackets[i] = dict[i]

# web_page_update = []  #removing books except [language]

for i in remove_lang_and_brackets:
    brackets = re.search("\[", remove_lang_and_brackets[i])

    if (brackets):
        s = remove_lang_and_brackets[i]
        z = ""
        for j in s:
            if (j == '['):
                break;
            else:
                z = z + j

        remove_lang_and_brackets[i] = z

for i in remove_lang_and_brackets:

    if (' by ' in remove_lang_and_brackets[i]):
        s = remove_lang_and_brackets[i].replace(' by ', ', by')
        remove_lang_and_brackets[i] = s
    elif ('. by' in remove_lang_and_brackets[i]):
        s = remove_lang_and_brackets[i].replace('. by', ', by')
        remove_lang_and_brackets[i] = s
    elif (',by' in remove_lang_and_brackets[i]):
        s = remove_lang_and_brackets[i].replace(',by', ', by')
        remove_lang_and_brackets[i] = s
    elif (', By' in remove_lang_and_brackets[i]):
        s = remove_lang_and_brackets[i].replace(', By', ', by')
        remove_lang_and_brackets[i] = s

books_author_with_by = {}
for i in remove_lang_and_brackets:
    if ((", by" in remove_lang_and_brackets[i])):
        books_author_with_by[i] = remove_lang_and_brackets[i]

books_author_with_by_without_contents = {}

for i in books_author_with_by:
    if (not ("Contents:" in books_author_with_by[i])):
        books_author_with_by_without_contents[i] = books_author_with_by[i]

final_books_and_author = {}
for i in books_author_with_by_without_contents:
    s = books_author_with_by_without_contents[i].split(", by")
    final_books_and_author[s[0]] = s[1]

for i in final_books_and_author:
    if ('Â' in final_books_and_author[i]):
        s = final_books_and_author[i].replace('Â', '')
        final_books_and_author[i] = s
    elif ('Ã«' in final_books_and_author[i]):
        s = final_books_and_author[i].replace('Ã«', '')
        final_books_and_author[i] = s

final_books_and_author_filter = {}

for i in final_books_and_author:
    if (not ('~TITLE and AUTHOR' in final_books_and_author[i])):
        final_books_and_author_filter[i] = final_books_and_author[i]

l = []
for i in final_books_and_author_filter:
    x = {}
    x["book"] = i
    x["author"] = final_books_and_author_filter[i]

    l.append(x)
start_and_end = []
s = "/home/sharan/Results_time/data_file"+str(ts)+".json"
with open(s, 'w') as f:
    json.dump(l, f, indent=2)

   # time.sleep(300)
    end = datetime.datetime.now()

    start_and_end.append(ts)
    start_and_end.append(str(start))
    start_and_end.append(str(end))
    times.append(start_and_end)
with open('time.txt','w+') as f:
	f.writelines(times)