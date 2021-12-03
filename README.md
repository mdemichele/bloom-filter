# Bloom Filter 
This project is a simple implementation of a bloom filter. The Bloom Filter is built as a class with 2 public methods: add and check. An instance of the BloomFilter class can add an element to the bloom filter and can check if an element exists within the bloom filter.

The project also provides a simple testing apparatus. To test the bloom filter, the test program first enters the contents of a text file through the bloom filter. The text file contains a list of commonly known bad passwords and is called 'dictionary.txt'. The program then provides at least three tests: one to check if an element is not in the bloom filter and two to check if an element is in the bloom filter. Many more tests can be added. 

# Running the Project
To run the tests, use the command:

python3 tests.py
