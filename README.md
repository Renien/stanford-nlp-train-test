<h1 align="center">
    <br>
        stanford-nlp-train-test
    <br>
  <h4 align="center">Support app to train and test custom corpus</h4>
</h1>

<p align="center">
  <a href="https://github.com/Renien/stanford-nlp-train-test/blob/master/LICENSE">
    <img src="https://img.shields.io/npm/l/express.svg?maxAge=2592000&style=flat-square"
         alt="License">
  </a>
  <a href="https://travis-ci.org/Renien/stanford-nlp-train-test">
    <img src="https://travis-ci.org/Renien/stanford-nlp-train-test.svg?branch=master"
         alt="Travis Build">
  </a>
</p>

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