# Write a function that attempts to open a URL and read its contents. Use try, except, and finally blocks to handle network-related errors and print an appropriate message.

import requests
def read_url(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Network Error: {e}")
        return None
    finally:
        print("URL check complete")
    
print(read_url('https://jsonplaceholder.typicode.com/posts/1'))
print(read_url('https://nonexistent.url'))
