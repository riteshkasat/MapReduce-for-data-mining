# Frequent Itemsets

This program uses Map Reduce paradigm to compute frequent itemsets of size 2 from a given list of transactions. The frequency of each frequent itemsets is atleast 100

## Getting Started

This code comes with a sample transactions.json file. Each line in this file represents a single transaction. Each transaction is a list of integers each of which represents unique identity of an item.

### Prerequisites

This program runs on python 2.7 

### How to run this program

Pass transactions.json as a command line input to itemsets.py 


```
python itemsets.py transactions.json
```


## Sample Output


```
[38, 39]
[38, 48]
[41, 48]
[39, 41]
[39, 48]

```
Each line in the output represents frequents itemsets of size 2.



## License

This project is licensed under the MIT License 
