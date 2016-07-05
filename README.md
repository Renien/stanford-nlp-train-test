# stanford-nlp-train-test
Support app to train and test custom corpus

## Properties.json File

```
{
    "classPath": "~/support-app/postagger/stanford",
    "modelPath": "models/retail_queries.model",
    "propsPath": "props/retail_queries.model.props",
    "trainFilePath": "~/support-app/postagger/trainingData",
    "trainFileName": "corpus-",
    "trainFileRange": 17,
    "testFilePath": "~/support-app/postagger/testingData",
    "testFileName": "retail_queries",
    "testFileRange": 5,
    "dumpFile": "dump/retail_queries.model.dump",
    "dumpSTDOUT": "dump/retail_queries.model.dump.stdout",
    "corpusPath": "~/support-app/postagger/corpus"

}
```