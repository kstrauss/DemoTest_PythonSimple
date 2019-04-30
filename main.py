"""
A stub for the main entry point into our processing model
"""
import statistics
def getInputs():
    # we should probably pull the data from databases
    return ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

"""
Computes the model score
Expects a list of strings
"""
def getModelScore(lOfStrings):
    return statistics.median([ len(i) for i in lOfStrings])
    

def main():
    print("hello my big world")
    print ("The average is ", getModelScore( getInputs()))

if __name__ == "__main__":
    # execute if run as a script
    main()
