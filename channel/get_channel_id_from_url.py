def get_channel_id_from_url(channel_url):
  import requests
  from bs4 import BeautifulSoup
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
  response = requests.get(channel_url, headers=headers)
  # Check if the request was successful
  if response.status_code == 200:
    source_code = BeautifulSoup(response.text, 'html.parser').prettify()
    return source_code.split('?channel_id=')[1].split('"',1)[0] #Finds the channel id from the source code of the youtube channel website and returns it
  else:
    return (f"Failed to retrieve the page. Status code: {response.status_code}")

# Testing:
channel_URL = input("Enter the YouTube channel URL: ")
channel_id = get_channel_id_from_url(channel_URL)
print(channel_id)