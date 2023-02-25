import unittest
import requests

def get_repo_info(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    if response.status_code == 200:
        repo_info = response.json()
        repo_list = []
        for repo in repo_info:
            repo_name = repo['name']
            repo_commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
            commits_response = requests.get(repo_commits_url)
            commits_info = commits_response.json()
            repo_commits = len(commits_info)
            repo_list.append((repo_name, repo_commits))
        return repo_list
    else:
        return None

username = 'BMKR4 '
repo_info = get_repo_info(username)
print(repo_info)

class TestGitHubAPI(unittest.TestCase):

    def test_get_repo_info(self):
        username = 'example_user'
        repo_info = get_repo_info(username)
        self.assertIsNotNone(repo_info)
        self.assertIsInstance(repo_info, list)
        self.assertGreater(len(repo_info), 0)
        for repo in repo_info:
            self.assertIsInstance(repo, tuple)
            self.assertEqual(len(repo), 2)
            self.assertIsInstance(repo[0], str)
            self.assertIsInstance(repo[1], int)