import json
import os

# Hold the application conf
conf = {}
train = ""
test = ""


def load_conf(conf_file):
    """
    Load conf from the conf json file
    Encapsulated with in a function to re-load at run time
    """
    global conf
    conf.clear()  # should keep the named reference to the mutable object
    conf.update(json.load(open(os.path.abspath(conf_file))))
    _commands()


def _commands():
    os.chdir(conf["classPath"])
    global train
    train = "java -mx1g -classpath stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -props " + \
            conf["propsPath"]
    global test
    test = "java -mx1g -classpath stanford-postagger.jar edu.stanford.nlp.tagger.maxent.MaxentTagger -model " + \
           conf["modelPath"] + " -testFile trainingData/corpus-1.txt -dump > " + conf["dumpFile"]


# Execute the command in shell
def execute_cmd(cmd):
    import subprocess
    std_out = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT)
    _write_dump_file(std_out)  # Write the std out to the file
    pass


# Write the stdout to the file
def _write_dump_file(std_out):
    f = open(conf["dumpSTDOUT"], 'w')
    f.write(std_out)
    f.close()
    pass
