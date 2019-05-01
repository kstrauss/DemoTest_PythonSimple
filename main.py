"""
A stub for the main entry point into our processing model
"""
<<<<<<< HEAD
class CMain:    
    def getInputs(self):
        # we should probably pull the data from databases
        return ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    
    """
    Computes the model score
    Expects a list of strings
    """
    def getModelScore(self, lOfStrings):
        d =  sum(len(i) for i in lOfStrings)
        return d/len(lOfStrings) # return mean    
    
    def main(self):
        print("hello my big world")
        print ("The average is ", self.getModelScore( self.getInputs()))

if __name__ == "__main__":
    # execute if run as a script
    CMain().main()
=======
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
>>>>>>> 13df09a186ec239c70a702b30f3e4b6df287f810
