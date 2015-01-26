import sys

################ INPUT READING ##########################################
def smart_readline():
    line = sys.stdin.readline()
    if line is None:
        return None
    line = line.strip()
    if line == '':
        return None
    return line

grid_size = smart_readline()
R, C = map(int, grid_size.split(" "))
##print("Grid size %d X %d" %(R, C))
GRID = list()
i = 0
while i < R:
    line = smart_readline()
    if line is None:
        continue
    i += 1
    grid_row = list(line.lower())
    assert len(grid_row) == C
    GRID.append(grid_row)
##print(GRID)

line = smart_readline()
W = int(line)
WORDS = list()
i = 0
while i < W:
    line = smart_readline()
    if line is None:
        continue
    i += 1
    WORDS.append(line.lower())
##print("Word Count " + str(W))
##print(WORDS)

##########################################################################

# Modify the grid to add side wall with -
for row in GRID:
    row.append('-')
    row.insert(0, '-')
GRID.insert(0, ['-'] * len(GRID[0]))
GRID.append(['-']*len(GRID[0]))

##print(GRID)

def word_finder(row, col, k, size, word_str_list):
    #print(row, col, k)
    if k == size :
        return True
    elif  row == (len(GRID)-1) or col == (len(GRID) -1):
        return False
    elif row == 0 or col == 0:
        return False
    elif word_str_list[k] != GRID[row][col]:
        return False
    else:
        k = k + 1
        out = (word_finder(row, col+1, k, size, word_str_list)  or 
               word_finder(row, col-1, k, size, word_str_list)  or 
               word_finder(row+1, col, k, size, word_str_list ) or 
               word_finder(row-1, col, k, size,  word_str_list )  or 
               word_finder(row-1, col-1, k, size,  word_str_list ) or 
               word_finder(row+1, col-1, k, size,  word_str_list ) or 
               word_finder(row-1, col+1, k, size,  word_str_list ) or 
               word_finder(row+1, col+1, k, size,  word_str_list ))
        return out

def word_find(word):
    word_str_list = list(word)
    size = len(word_str_list)
    for row in xrange(1, len(GRID)-1):
        for col in xrange(1, len(GRID[0])-1):
            if GRID[row][col] == word_str_list[0]:
                if(word_finder(row, col, 0, size, word_str_list)):
                    print row, col
print GRID
for word in WORDS:
    print word
    word_find(word)
