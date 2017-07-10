from threading import Thread, Event
from queue import Queue, Empty
import urllib.request,sys,csv,io,os,time;
import argparse

FILE_URL = 'https://s3.amazonaws.com/carto-1000x/data/yellow_tripdata_2016-01.csv'
FIELD = 'tip_amount'
#OPERATION = 'AVG' # Number of threads to retrieve concurrently the remote file from the server.

def download_task(url,chunk_queue,event):
    
    CHUNK = 1*1024
    response = urllib.request.urlopen(url)
    event.clear()
    #counter = 0 
    print('%% - Starting Download  - %%')
    print('%% - ------------------ - %%')
    '''VT100 control codes.'''
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    while True:
        chunk = response.read(CHUNK)
        if not chunk:
            print('%% - Download completed - %%')
            event.set()
            break
        chunk_queue.put(chunk)

def count_task(chunk_queue, event, field):
    part = False
    time.sleep(5) #give some time to producer
    M=0
    amnt=0.0
    contador = 0
    '''VT100 control codes.'''
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    while True:
        try:
            #Default behavior of queue allows getting elements from it and block if queue is Empty.
            #In this case I set argument block=False. When queue.get() and queue Empty ocurrs not block and throws a 
            #queue.Empty exception that I use for show partial result of process.
            chunk = chunk_queue.get(block=False)
            for line in chunk.splitlines(True):
                if line.endswith(b'\n'):
                    if part: ##for treat last line of chunk (normally is a part of line)
                        line = linepart + line
                        part = False
                    if M > 1: #skip header
                        row = next(csv.reader(io.StringIO(line.decode('utf-8'))))
                        amnt += float(row[15]) 
                    M += 1
                else: 
                ##if line not contains '\n' is last line of chunk. 
                ##a part of line which is completed in next interation over next chunk
                    part = True
                    linepart = line
        except Empty:
            # QUEUE EMPTY 
            print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
            print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
            print('Downloading records ...')
            if M>0:
                print('Partial result:  Records: %d -- AVG: %f' % (M-1, amnt/(M-1))) #M-1 because M contains header
            if (event.is_set()): #'THE END: no elements in queue and download finished (even is set)'
                print(CURSOR_UP_ONE + ERASE_LINE+ CURSOR_UP_ONE)
                print(CURSOR_UP_ONE + ERASE_LINE+ CURSOR_UP_ONE)
                print(CURSOR_UP_ONE + ERASE_LINE+ CURSOR_UP_ONE)
                print('The consumer has waited %s times' % str(contador))
                print('RECORDS = ', M-1)
                print('Average = ', amnt/(M-1))
                break
            contador += 1
            time.sleep(1) #(give some time for loading more records) 


def main():

    
    chunk_queue = Queue()
    event = Event()
    args = parse_args()
    url = args.url
    field = args.field
    #op = args.operation

    p1 = Thread(target=download_task, args=(url,chunk_queue,event,))
    p1.start()
    p2 = Thread(target=count_task, args=(chunk_queue,event,field,))
    p2.start()
    p1.join()
    p2.join()

# The user of this module can customized some parameters:
#   + URL where the remote file can be found.
#   + The field that must be parsed.
#   + The number of threads that will retrieve the remote file.
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', default=FILE_URL,
                        help='remote-csv-file URL')
    parser.add_argument('-f', '--field', default=FIELD,
                        help='calculate the average value of this field')
    #parser.add_argument('-op', '--operation', default=OPERATION,
    #                    help='operation over field (min, max, sum, avg')
    return parser.parse_args()



if __name__ == '__main__':
    main()
    #cProfile.run('main()', sort='cumtime')