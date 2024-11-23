import requests
import matplotlib.pyplot as plt

# Fetch data from GitHub API
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
repo_names, stars = [], []
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
    
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Plotting the data
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.barh(repo_names, stars, color='skyblue')
ax.set_xlabel('Stars')
ax.set_title('Most Starred Python Repositories on GitHub')
plt.show()



""" 

 Pxbox ( x = , y = title = , labels = , have_rate = [])



 """
