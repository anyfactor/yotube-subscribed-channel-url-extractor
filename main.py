import re

# After loding all the subscribed channel name manually, then saving the webpage in the machine as html

# Path to the html file in your machine
file_path = 

def url_scraper(file_path):
  f = open(file_path, 'r', encoding = "utf8", errors='ignore')
  urls = re.findall(r'/channel/([^\'" >]+)', f.read())
  for i in urls:
    # Returns the channel id, so concatnate with the following string
    print('https://www.youtube.com/channel/' + i)
