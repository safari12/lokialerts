import requests


class ServiceNodeRPCError(requests.RequestException):
    pass


class ServiceNodeRPC:
    def get_service_node_stats(self, sn):
        try:
            ip = sn['ip']
            port = sn['port']
            pubkey = sn['pubkey']
            return requests.post("http://%s:%s/json_rpc" % (ip, port), json={
                'jsonrpc': '2.0',
                'id': 0,
                'method': 'get_service_nodes',
                'params': {
                    'service_node_pubkeys': [pubkey]
                }
            }, timeout=2).json()['result']['service_node_states'][0]
        except requests.RequestException as e:
            raise ServiceNodeRPCError(e)
