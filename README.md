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
docker build . -t pythonActuary:latest

# assuming it worked
docker run pythonActuary:latest
```
