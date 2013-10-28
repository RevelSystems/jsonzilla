import functools
import json
import random
import requests


def post(method):
    def decorate(f):
        @functools.wraps(f)
        def decorator(*args, **kwargs):
            json_zilla = args[0]
            params = kwargs
            if 'result' in params:
                del params['result']
            if 'error' in params:
                del params['error']

            for i in range(1, len(args)):
                name = f.func_code.co_varnames[i]
                params[name] = args[i]

            error = None
            result = None

            querystring = {
                "method": method,
                "params": [
                    params
                ],
                "id": random.randint(1, 100)
            }
            r = json_zilla.session.post(json_zilla.service_url, data=json.dumps(querystring))

            if r.status_code == requests.codes.ok:
                if len(r.text):
                    contents = r.json()
                    if 'error' in contents:
                        if contents['error']:
                            error = contents['error']
                    if 'result' in contents:
                        if contents['result']:
                            result = contents['result']
            params['error'] = error
            params['result'] = result
            f(json_zilla, **params)
        return decorator
    return decorate
