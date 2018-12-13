from flask import Flask, request, render_template

app = Flask(__name__)
default_key = '1'

"""
# We are using a python dictionary
# to store all the key value pairs in memory
# and initialize the dictionary with a single entry.
"""
cache = {default_key: 'one'}



"""
We register the view function to accept the POST and GET 
methods to the url /
The first time the web page going to be a GET request to
the server
If he clicked to save or load button the browser with 
sent a post request to the server 
By default the view function only handles GET Method
So we need to explicitly specify both post and get method 
secure so that The View function can handle both cases 
"""
@app.route('/', methods=['GET', 'POST'])
def mainpage():

    """
    We assign the default value which is Arabic number one to 
    the variable key so that if we first load the web page the 
    app will display a default key value pair.
    """
    key = default_key

    """
    If the user specified the key in the form we then override 
    the key variable.
	"""
    if 'key' in request.form:
        key = request.form['key']

    """
	if the user clicks the save button will go ahead and see if 
    the key value pair in our in-memory dictionary
    """
    if request.method == 'POST' and request.form['submit'] == 'save':
        cache[key] = request.form['cache_value']


    """
    Then we do a key value a up in the dictionary to get the 
    key value pair and pass it to the template to render the HTML
    page
    """
    cache_value = None;
    if key in cache:
        cache_value = cache[key]

    return render_template('index.html', key=key, cache_value=cache_value)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
