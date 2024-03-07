#!/usr/bin/python3

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "reddit-top-ten-script"}
    
    response = requests.get(url, headers=headers, params={"limit": 10})
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        if posts:
            for post in posts:
                print(post["data"]["title"])
        else:
            print("No posts found.")
    else:
        print("None")
