# multiSentence

## Paper
[Unsupervised Abstractive Meeting Summarization with Multi-Sentence
Compression and Budgeted Submodular Maximization](https://arxiv.org/pdf/1805.05271v2.pdf)

## This Repository
Here present a program of the algorithm in "Chapter 4 Our Framework" of the paper.


## Usage
Here use the python Flask, it will turn on the 5000 port on localhost as a API
  * API URI: /api/v1.0/multi-sentence/calculator


### Run
```bash
$ python main.py
```

then curl and given the arguments: sentence, path, Pi, Pj.


```bash 
curl -i -H "Content-Type: application/json" -X POST -d \
'{
"method":1, 
"sentence": "This article is written for unmanaged VPS which is recommended for experienced users who prefer to manage all the aspects of their infrastructure on their own. But if you don’t have technical knowledge it is much cheaper for you to use managed hosting. Manged hosting has at least twice higher price than unmanaged, for example unmanaged VPS on DigitalOcean cost $20 vs $70 for manged Fastcomet and $75 for RoseHosting. However the difference is still in ~ $50 per month, it is a small price for saving you tons of time and guarantee that everything will work fast and secure. If you will decide to hire someone to maintain your server you will have to pay 20-50 per hour.", 
"path": "If you will decide to hire someone to maintain your server you will have to pay 20-50 per hour", 
"Pi": "will", 
"Pj": "decide"
}' \
http://localhost:5000/api/v1.0/multi-sentence/calculator

```
