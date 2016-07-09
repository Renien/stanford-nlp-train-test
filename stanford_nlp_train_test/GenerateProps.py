import fileinput
import re


class GenerateProps:
    def __init__(self, conf):
        self.conf = conf
        self.path = conf['trainFilePath']
        self.file_name = conf['trainFileName']
        self.file_range = conf['trainFileRange']
        self.file_list = []

    def _generate_files(self):
        for i in range(1, self.file_range):
            self.file_list.append(self.path + '/' + self.file_name + str(i) + '.txt')
        pass

    def update_props_file(self):
        self._generate_files()  # Generate file list
        training_files = 'trainFile = ' + ';'.join(self.file_list)
        for line in fileinput.input(self.conf['projectPath']+'/'+self.conf['propsPath'], inplace=1):
            print re.sub('trainFile.*', training_files, line),
