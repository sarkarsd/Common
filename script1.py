import os
import sys
from pathlib import Path


# Function to rename multiple files
def main():
    direc = Path(sys.argv[1])
    file_extsn = sys.argv[2]
    for filename in os.listdir(direc):
        dst = Path(filename).stem + file_extsn
        src = os.path.join(direc, filename)
        dst = os.path.join(direc, dst)
        if not os.path.exists(dst):
            # rename() function will
            # rename all the files
            os.rename(src, dst)
        else:
            continue


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
