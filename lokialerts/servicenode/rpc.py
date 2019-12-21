import requests


class ServiceNodeRPC:
    def get_service_nodes(self, ip, port, pubkeys):
        return requests.post("http://%s:%d/json_rpc" % (ip, port), json={
            'jsonrpc': '2.0',
            'id': 0,
            'method': 'get_service_nodes',
            'params': {
                'service_node_pubkeys': pubkeys
            }
        }, timeout=2).json()['result']['service_node_states']
