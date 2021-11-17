import requests
r = requests.post("https://trackfyapp.herokuapp.com/", data={'foo': 'bar'})
# And done.
print(r.text) # displays the result body.
