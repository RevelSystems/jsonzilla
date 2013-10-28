import functools
import inspect
import json
import logging
import random
import requests

import httplib
#httplib.HTTPConnection.debuglevel = 1

#logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True


class JsonZilla:
    def __init__(self, rpc_url, username, password):
        self.service_url = rpc_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json-rpc"}
        self._id = random.randint(1, 100)

    def login(self):
        querystring = {
            "method": "User.login",
            "params": [
                {
                    "login": self.username,
                    "password": self.password,
                    "remember": True
                }
            ],
            "id": self._id
        }
        r = self.session.post(self.service_url, data=json.dumps(querystring))
        print ""
        print r.status_code, r.text
        print ""

    def time(self):
        data = {
            "method": "Bugzilla.time",
            "Bugzilla_login": self.username,
            "Bugzilla_password": self.password,
            "id": self._id
        }
        r = self.session.get(self.service_url, params=data)
        print ""
        print r.text
        print ""

    def version(self):
        data = {
            "method": "Bugzilla.version",
            "Bugzilla_login": self.username,
            "Bugzilla_password": self.password,
            "id": self._id
        }
        r = self.session.get(self.service_url, params=data)
        print ""
        print r.text
        print ""

    def bugs(self, ids):
        """ Returns information about a list of bugs. """
        querystring = {
            "method": "Bug.get",
            "params": [
                {'ids': ids}
            ],
            "id": self._id
        }
        r = self.session.post(self.service_url, data=json.dumps(querystring))
        print ""
        print r.status_code, r.text
        print ""

    def search(self, bug_ids):
        """ Returns information about a list of bugs matching criterias. """
        querystring = {
            "method": "Bug.search",
            "params": [
                {'id': bug_ids}
            ],
            "id": self._id
        }
        r = self.session.post(self.service_url, data=json.dumps(querystring))
        print ""
        print r.status_code, r.text
        print ""

    def __compatibility_bugs_method(self, bug_ids):
        """ Returns information about a list of bugs. """
        querystring = {
            "method": "Bug.get_bugs",
            "params": [
                {
                    'ids': bug_ids
                }
            ],
            "id": self._id
        }
        r = self.session.post(self.service_url, data=json.dumps(querystring))
        print ""
        print r.status_code, r.text
        print ""

    def bug(self, bug_id):
        """ Returns information about a single bug. """
        return self.bugs(bug_id)

