import requests
import json

# Your LinkedIn access token
access_token = 'YOUR_ACCESS_TOKEN'

# LinkedIn API endpoint for creating a post
url = 'https://api.linkedin.com/v2/ugcPosts'

# Headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'X-Restli-Protocol-Version': '2.0.0'
}

# Post data
post_data = {
    "author": "urn:li:person:YOUR_LINKEDIN_ID",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello, LinkedIn! This is a post from the API."
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(post_data))

# Check the response
if response.status_code == 201:
    print("Post created successfully!")
else:
    print(f"Failed to create post: {response.status_code}, {response.text}")
