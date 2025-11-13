import webbrowser

url = 'https://www.python.org'
c = webbrowser.get('chrome')  # Use 'chrome' as the argument
c.open(url)
c.open_new_tab('https://docs.python.org')
