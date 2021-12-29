# Code based on docs: https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
# Requests library docs: https://docs.python-requests.org/en/latest/
import requests
import requests.auth

# https://stealthbits.com/blog/how-to-hide-api-keys-github/
import config

# Our app's client ID and app's client secret obtained from https://www.reddit.com/prefs/apps
# Documentation: https://github.com/reddit-archive/reddit/wiki/OAuth2
client_auth = requests.auth.HTTPBasicAuth(config.REDDIT_CLIENT_ID, config.REDDIT_CLIENT_SECRET)
post_data = {
    "grant_type": "password",
    "username": config.REDDIT_USERNAME,
    "password": config.REDDIT_PASSWORD
}

headers = {
    "User-Agent": f"rslash_manga_subs/0.1 by /u/{config.REDDIT_USERNAME}"
}

# Github token test
# curl -i -H "Accept: application/vnd.github.v3+json" -H "Authorization: token {config.GITHUB_AUTH_TOKEN}" https://api.github.com/repos/vaishnavgade/rslash_manga_subs/actions/secrets

# string formatting with dictionaries 
# print("Headers with User-Agent used: {User-Agent}".format(**headers));

# string formatting with f-Strings
# print(f"Headers with User-Agent used: {headers['User-Agent']}")

# print("Requesting access_token from Reddit");
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# print(f"Response from access_token: {response.json()}")

# if 'access_token' not in response.json():
#     raise ValueError("No access_token in response")

# headers = {
#     "Authorization": f"bearer {response.json()['access_token']}",
#     "User-Agent": f"rslash_manga_subs/0.1 by /u/{config.REDDIT_USERNAME}"
# }

# comment out above code once you get your token and start testing your code
headers = {
    "Authorization": f"bearer {config.REDDIT_ACCESS_TOKEN}",
    "User-Agent": f"rslash_manga_subs/0.1 by /u/{config.REDDIT_USERNAME}"
}

print("Requesting identity information from Reddit")
# response = requests.get("https://oauth.reddit.com/api/v1/me/karma", headers=headers)
# print(f"Response from api v1 me: {response.json()}")
# %3A => : (symbol)
# restrict_sr=1 => true (boolean) Limit my search to Subreddit
response = requests.get("https://oauth.reddit.com/r/manga/search/?q=title%3A[DISC] Fire Force&restrict_sr=1&sr_nsfw=&include_over_18=1&t=all&sort=new", headers=headers)

if 'data' not in response.json():
    raise ValueError("No data in response")

# Might have to keep this updated based on r/manga
chapterVariations = ['Ch', 'Chapter']

for post in response.json()['data']['children']:
    if any(chapterVariation in post['data']['title'] for chapterVariation in chapterVariations):
        # print the tile and url for a post
        print(f"Title: {post['data']['title']}, url: {post['data']['url']}")