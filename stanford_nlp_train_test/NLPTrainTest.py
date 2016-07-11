import Util
from stanford_nlp_train_test.GenerateProps import GenerateProps


class NLPTrainTest:
    def __init__(self, conf_file):
        Util.load_conf(conf_file)
        self.genProps = GenerateProps(Util.conf)
        self.genProps.update_props_file()
