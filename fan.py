import os
import sys
import pandas as pd

#anaconda: python distribution

class TripleRecord:
    def __init__(self, pid, sec, mac):
        self.pid = pid
        self.sec = sec
        self.mac = mac

    def __repr__(self):
        return 'pid: ' + str(self.pid) + '\n' + 'secret: ' + self.sec + '\n' + 'mac: ' + self.mac

    def secret(self):
        return bytearray.fromhex(self.sec)

    def addr(self):
        return bytearray.fromhex(self.mac)

def main(excel):
    xl = pd.ExcelFile(excel)
    #print(xl.sheet_names)
    df = xl.parse('设备密钥表', header=1)
    df10 = df.head(10)
    for index, row in df10.iterrows():
        rec = TripleRecord(row['Product ID(十进制)'], row['Product Secret'], row['Mac地址'])
        #print(rec)
        #print(rec.secret())
        print('{ ', end='')
        for j in rec.secret():
            print('{0:#02x},'.format(j), end=' ')
        print('}')

        print('{ ', end='')
        for j in rec.addr():
            print('{0:#02x},'.format(j), end=' ')
        print('}')
    
if __name__ == "__main__":
    main(sys.argv[1])
