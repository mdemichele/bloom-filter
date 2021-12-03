import sys
import doctest
from bloomFilter import BloomFilter 

def main():
    """Will run all tests in the Main Function"""
    
    # This code is here in case you want to set it up to accept command line arguments 
    # file = sys.argv[1]
    # sizeArray = sys.argv[2]
    # numHashes = sys.argv[3]
    
    # Create a small array of sample words to add to bloom filter 
    words = []
    
    ## BEGIN TESTS 
    bloom = BloomFilter(800000) # Create instance of BloomFilter.
    
    # Add all the words from words array to bloom filter
    with open('./dictionary.txt') as f:
        for line in f:
            line = line.strip()
            bloom.add(line)
        
    # TEST 1: Element is NOT in bitArray 
    answer = bloom.check('RandomGoodP@SSword#29871') # NOT in bitArray 
    print("\n")
    print("----------TEST 1----------")
    print("(Check item NOT in bad password list)")
    print("Is 'RandomGoodP@SSword#29871' in bad password list? Should be False: " + str(answer))
    print("\n")
    
    # TEST 2: Element IS in bitArray 
    answer = bloom.check('!7350r13r0') # This is in bitArray
    print("----------TEST 2----------")
    print("(Check item in bad password list)")
    print("Is '!7350r13r0' in bad password list? Should be True: " + str(answer))
    print("\n")
    
    # TEST 3: Different element IS in bitArray 
    answer = bloom.check('!+!+@') # This is in bitArray
    print("----------TEST 3----------")
    print("(Check different item in bad password list)")
    print("Is '!+!+@' in bad password list? Should be True: " + str(answer))
    print("\n")
    
    # TEST 4: Check if all elements from input file are in bitArray
    # This test will output the answers to a separate output_file.txt 
    print("----------TEST 4----------")
    print("(Check all items in input file)")
    
    # First, delete any content in output file if it exists 
    outputFile = open("output.txt", "w")
    outputFile = open("output.txt", "a")
    
    # Read each line in input file and output answer to output.txt 
    with open("./sample_input.txt") as f:
        for line in f:
            line = line.strip()
            answer = bloom.check(line)
            outputFile.write(str(answer) + "\n")
            
    outputFile.close()
    
    
if __name__ == "__main__":
    main()