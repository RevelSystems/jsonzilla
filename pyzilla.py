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

    @post("Bugzilla.version")
    def version(self, result=None):
        """ Bugzilla version. """
        return result

    @post("Bug.get")
    def bugs(self, ids, result=None):
        """ Returns information about a list of bugs. """
        return result

    @post("Bug.search")
    def search(self, id, result=None):
        """ Returns information about a list of bugs matching criterias. """
        return result

    @post("Bug.get_bugs")
    def __compatibility_bugs_method(self, ids, result=None):
        """ Returns information about a list of bugs. """
        return result

    def bug(self, bug_id):
        """ Returns information about a single bug. """
        return self.bugs(bug_id)

