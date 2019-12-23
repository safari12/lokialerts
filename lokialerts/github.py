import requests


class LokiGithubError(requests.RequestException):
    pass


class LokiGithub:
    def __init__(self):
        self.base_url = 'https://api.github.com'

    def get_latest_version(self):
        try:
            response = requests.get(
                self.base_url + '/repos/loki-project/loki-network/releases/latest'
            )
            results = response.json()
            return results['tag_name']
        except requests.RequestException as e:
            raise LokiGithubError(e)
