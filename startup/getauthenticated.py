import urllib2
import urllib


url='https://smartymirror.com/wp-login.php'

headers = [ ("User-Agent", "Mozilla/5.0")]

data = [
	("log","USERNAME"),
	("pwd","PASSWORD"),
	("testcookie",1),
	("submit","Log In"),
	("redirect_to","http://smartymirror.com/?page_id=30"),
	("rememberme","forever")]

req = urllib2.Request(url, urllib.urlencode(dict(data)), dict(headers))
response = urllib2.urlopen(req)

the_page=response.read()
print the_page

