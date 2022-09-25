

import time

def get_urls(arg):
    time.sleep(arg)
    print("retrieved all urls")

def write_msg(arg):
    time.sleep(arg)
    print("write all to database")

def main():
    tic = time.time()
    get_urls(3)
    write_msg(2)
    toc = time.time()
    print(f"Elapsed: {toc-tic} s")

main()

