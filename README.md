# DemoTest_A
A test repo to demonstrate git, developing python for actuaries with the code that should enable an automatic docker build. Key points include:
- branches and use of master
- a requirements.txt file for including dependent libraries
- a pytest file (test_*.py or *_test.py) with the required format for test names. For more info see [pytest site](https://docs.pytest.org/en/latest/getting-started.html)
- a dockerfile which could serve as a template for all python docker images in this model

We will use this as a starting point for doing changes.

The example is trivial, but it is such to just demonstrate.

To build and run:

```
git clone https://github.voya.net/i719184/DemoTest_A
cd DemoTest_A
docker build . -t pythonactuary:latest

# assuming it worked
docker run pythonactuary:latest
```

Of course to do the more complete (adds meta data) run in powershell

```
buildDock.ps1
(docker inspect pythonactuary:latest | convertFrom-json).ContainerConfig.labels
docker run pythonactuary:latest
```

## Azure Pipeline note
if you use the azure pipeline docker task it adds many more (and probably better) set of of metadata for labels. see https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/build/docker?view=azure-devops for details