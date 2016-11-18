
# take a position, return how many bits read
def read4(pos):
    pass

def readBuffer(pos, size):
    
    # make a block of empty data for copy
    pos = [''] * size
    readBuff = [''] * 4
    curPos = 0

    while curPos < size:
        
        readBits = read4(readBuff)
        
        if readBits > 0:
            curPos += readBits
            # copy data from buffer to mem
            pos[curPos : curPos + readBits] = readBuff
        else:
            break
    
    return min(size, curPos)
    



