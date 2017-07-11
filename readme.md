Script to analyze **on the fly** and display statistic of remote csv field file. Implemented by applying [producer-consumer problem](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem) approach. This pattern allows us to assign each task to a thread (or process) and show partial results.

Usage

```
$ python csv-data-test.py -u <url-csv-file> -f <index-of-field>
```

For synchronization purposes this implementation uses a Queue and a Event object from queue and multiprocessing python library, respectively.

Download stream is saved in queue and is consumed on the fly. No HDD extra space is needed and memory efficient. **Tested in Python 3.5.2 (vanilla) on Fedora Core 25 x86_64.**