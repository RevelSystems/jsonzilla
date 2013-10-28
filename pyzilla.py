import functools
import inspect
import json
import logging
import random
from protocol import post
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
        self.__login(username, password)

    @post("User.login")
    def __login(self, login, password, remember=True, result=None, error=None):
        """ Login into bugzilla with given credentials. """
        pass

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

    @post("Bug.get")
    def bugs(self, ids, result=None, error=None):
        """ Returns information about a list of bugs. """
        print result

    @post("Bug.search")
    def search(self, id, result=None, error=None):
        """ Returns information about a list of bugs matching criterias. """
        print result

    @post("Bug.get_bugs")
    def __compatibility_bugs_method(self, ids, result=None, error=None):
        """ Returns information about a list of bugs. """
        print result

    def bug(self, bug_id):
        """ Returns information about a single bug. """
        return self.bugs(bug_id)


