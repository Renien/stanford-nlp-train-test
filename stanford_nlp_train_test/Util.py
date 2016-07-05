import json

# Hold the application settings
settings = {}


def load_settings():
    """
    Load settings from the settings json file
    Encapsulated with in a function to re-load at run time
    """
    global settings
    settings.clear()  # should keep the named reference to the mutable object
    settings.update(json.load(open('/Users/renienj/open-source-projects/support-apps/stanford-nlp-train-test/stanford_nlp_train_test/setting/properties.json')))


# Load settings and support data at the application start-up
load_settings()
