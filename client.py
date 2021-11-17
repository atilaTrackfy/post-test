import requests
r = requests.post("http://yoururl/post", data={'foo': 'bar'})
# And done.
print(r.text) # displays the result body.
