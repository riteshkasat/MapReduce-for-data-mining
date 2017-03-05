# Project Title

Term frequency and Document frequency

## Getting Started

This program uses MapReduce paradigm to calculate term frequency and document frequency for each word in the input dataset.


## Prerequisites

This program runs on python 2.7


## Input data

This program comes with sample input dataset called books.json. Each line contains the name of the book followed by the contents of the book.

```
["milton-paradise.txt", "[ Paradise Lost by John Milton 1667 ] Book I Of Man ' s first disobedience , and the fruit Of that forbidden tree whose mortal taste Brought death into the World , and all our woe , With loss of Eden"]
```



## How to run this program

Pass books.json as the command line parameter to tf_dy.py

```
python tf_df.py books.json
```

### Sample output


```
["all", 3, [["milton-paradise.txt", 1], ["blake-poems.txt", 1], ["melville-moby_dick.txt", 2]]]

```

Each line contains a word followed by its total frequency in the entire dataset. Next, the output show the individual books in which the word appears along with the frequency in each book.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


