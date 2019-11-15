from urllib import request

myurl = "http://localhost:81/MyPortfolio.php"

answ = request.urlopen(myurl)

for target_list in answ.readlines():
	print (target_list)

