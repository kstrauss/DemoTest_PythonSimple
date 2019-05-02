"""
A stub for the main entry point into our processing model
"""
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