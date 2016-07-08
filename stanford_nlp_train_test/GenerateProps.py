import fileinput
import re

class GenerateProps:

    def __init__(self, commands):
        self.commands = commands
        self.path = commands['trainFilePath']
        self.file_name = commands['trainFileName']
        self.file_range = commands['trainFileRange']
        self.file_list = []

    def generate_files(self):
        for i in range(1, self.file_range):
            self.file_list.append(self.path+'/'+self.file_name+str(i)+'.txt')
        pass

    def update_props_file(self):
        training_files = 'trainFile = '+';'.join(self.file_list)

        for line in fileinput.input(self.commands['propsPath'], inplace = 1):
            print re.sub('trainFile.*', training_files, line),