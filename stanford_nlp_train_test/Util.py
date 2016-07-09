import json
import os

# Hold the application conf
conf = {}


def load_conf(conf_file):
    """
    Load conf from the conf json file
    Encapsulated with in a function to re-load at run time
    """
    global conf
    conf.clear()  # should keep the named reference to the mutable object
    conf.update(json.load(open(os.path.abspath(conf_file))))
