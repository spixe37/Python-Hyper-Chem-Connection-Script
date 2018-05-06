import sys, json, numpy as np, pyhcs
from time import sleep

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    sleep(0.5)
    if not pyhcs.connect():
        return
    sleep(0.5)
    #get our data as an array from read_in()
    line = read_in()
    pyhcs.exec_text(line.strip())
    print(line)

#start process
if __name__ == '__main__':
    main()