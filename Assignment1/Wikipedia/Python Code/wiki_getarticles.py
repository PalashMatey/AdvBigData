from wikiapi import WikiApi
wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'en'})

keywords=[]

with open("Important_Names.txt","r") as f:
	for line in f:
		keywords.append(line)
f.close()

count=0
for word in keywords:
	count=count+1
	results = wiki.find(word.strip('\n'))
	if len(results)!=0:
		article = wiki.get_article(results[0])
		text=article.content.encode('utf-8')
		with open("Web"+str(count)+".txt","w") as f:
			f.write(text)
		f.close()
		print article.url
