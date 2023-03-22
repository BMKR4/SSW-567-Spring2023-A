import unittest
from unittest.mock import patch
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

class TestGitHubAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_repo_info(self, mock_get):
        mock_response = [('helloworld', 1)]
        mock_get.return_value.json.return_value = mock_response

        username = 'BMKR4'
        actual_data = get_repo_info(username)
        self.assertIsNotNone(actual_data)
        self.assertIsInstance(actual_data, list)
        self.assertGreater(len(actual_data), 0)
        mock_response = [('helloworld', 1)]
        self.assertEqual(actual_data, mock_response)
        

