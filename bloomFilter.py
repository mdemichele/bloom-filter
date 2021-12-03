from Crypto.Hash import SHA256 
from Crypto.Hash import SHA384
from Crypto.Hash import SHA512
from Crypto.Hash import BLAKE2s
from Crypto.Hash import SHA3_256

class BloomFilter():
    """Class definition for a bloom filter. Contains method to add an element to the bit array and a method to check if an element is in the array"""
    
    def __init__(self, sizeArray=100, numHashes=3):
        """Takes two parameters: size of the bit array (M) and number of hashes (K)"""
        self.sizeArray = sizeArray 
        self.numHashes = numHashes 
        self.hashAlgorithms = [
            SHA256,
            SHA384,
            SHA512,
            BLAKE2s,
            SHA3_256
        ]
        self.bitArray = [False] * sizeArray 
             
    def createHashes(self, numHashes, plaintext):
        """Function returns an array of numHashes number of different hash values from the specified plaintext"""
        hashArray = []
        
        for index in range(0, numHashes):
            # Turn plaintext into bytearray 
            b_plaintext = bytearray(plaintext, encoding='utf-8')
            
            # Create hash value for each different hash algorithm
            hash = self.hashAlgorithms[index].new(data=b_plaintext)
            
            # Turn hash value into a hex string 
            hex = hash.hexdigest()
            
            # Add new hash value to hashes array 
            hashArray.append(hex)
            
        return hashArray
    
    def add(self, element):
        """Function adds the specified text to the bit array"""
        hashArray = self.createHashes(self.numHashes, element)
        
        # Place each hashed value at the correct index in bitArray 
        for hash in hashArray:
            # Turn hash value into an integer 
            intHash = int(hash, 16)
            
            # Turn integer into correct index 
            index = intHash % self.sizeArray
            
            # Display where element will be placed 
            # print("Element " + element + " placed at: " + str(index))
            
            # Set value at the specified index to True 
            self.bitArray[index] = True 
                   
    def check(self, element):
        """Function checks if every index of hashed element is already true. If so, return True. If not, return False"""
        # Set answer initially to true 
        answer = True 
        
        # Create hash array for the specified element 
        hashArray = self.createHashes(self.numHashes, element)
        
        # Check if each hash value is already in bitArray 
        for hash in hashArray:
            intHash = int(hash, 16)
            index = intHash % self.sizeArray 
            
            if self.bitArray[index] == False:
                answer = False 
                
        return answer 
        