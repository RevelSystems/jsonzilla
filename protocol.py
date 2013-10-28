import functools
import json
import random
import requests


class BugzillaRequestException(Exception):
    def __init__(self, status_code, response_text):
        self.status_code = status_code
        self.response_text = response_text

    def __repr__(self):
        return "{}: {}".format(self.status_code, self.response_text)


class BugzillaRpcException(Exception):
    def __init__(self, error):
        self.error = error

    def __repr__(self):
        return self.error


def post(method):
    def decorate(f):
        @functools.wraps(f)
        def decorator(*args, **kwargs):
            json_zilla = args[0]
            params = kwargs
            if 'result' in params:
                del params['result']

            for i in range(1, len(args)):
                name = f.func_code.co_varnames[i]
                params[name] = args[i]

            error = None
            result = None

            data = {
                "method": method,
                "params": [
                    params
                ],
                "id": random.randint(1, 1000)
            }
            r = json_zilla.session.post(json_zilla.service_url, data=json.dumps(data))

            if r.status_code == requests.codes.ok:
                if len(r.text):
                    contents = r.json()
                    if 'error' in contents:
                        error = contents['error']
                    if 'result' in contents:
                        result = contents['result']
            else:
                raise BugzillaRequestException(int(r.status_code), r.text)
            if error:
                raise BugzillaRpcException(error)
            params['result'] = result
            return f(json_zilla, **params)
        return decorator
    return decorate
