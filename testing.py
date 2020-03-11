# Author: Andy R. 

import os
import subprocess
import time

# Edit these global variables to your file 
FOLDERURL = f'C:\\insert\\your\\directory\\here\\'
EXECUTABLE_NAME = "insert_your_executable_here"


def main():
    testnum = 1
    with open("./testfiles.txt", 'r') as testfiles: 
        for line in testfiles: 
            #print('cmd /c ' + f'"{FOLDERURL}{EXECUTABLE_NAME}" < "{FOLDERURL}{line}" > "{FOLDERURL}test0{testnum}.out"')
            process = subprocess.run([f'{FOLDERURL}{EXECUTABLE_NAME}', '<', f'{FOLDERURL}{line}'], stdout=subprocess.PIPE,  shell=True)
            with open(f'./cmake-build-debug/test0{testnum}.out', 'wb+') as testout:
                testout.write(process.stdout)
            testnum += 1

        for n in range(1, 8): # Swap upper bound of range to number of tests +1 
            os.startfile(f'"{FOLDERURL}test0{n}.out"')

if __name__ == "__main__":
    main()