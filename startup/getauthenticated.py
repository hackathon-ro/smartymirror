import urllib2
import urllib

url='https://smartymirror.com/wp-login.php'

headers = [  ("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5")]

data = [
    ("log","admin"), 
    ("pwd","soccer98"), 
    ("testcookie",1), 
    ("submit","Log In"), 
    ("redirect_to","http://smartymirror.com/"), 
    ("rememberme","forewer")]

req = urllib2.Request(url, urllib.urlencode(dict(data)), dict(headers))
response = urllib2.urlopen(req)

the_page=response.read()
print the_page
