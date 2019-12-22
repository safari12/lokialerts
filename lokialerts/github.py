import requests


class LokiGithub:
    def __init__(self):
        self.base_url = 'https://api.github.com'

    def get_latest_version(self):
        response = requests.get(
            self.base_url + '/repos/loki-project/loki-network/releases/latest'
        )
        results = response.json()
        tag_name = results['tag_name']
        tag_name = tag_name.replace("v", "")
        tag_name = tag_name.replace(".", "")
        return int(tag_name)
