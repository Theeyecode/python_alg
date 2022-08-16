def zigzagTraverse(array):
    # Write your code here.
    height = len(array) -1
    width = len(array[0]) -1
    goingDown = True
    row, col = 0,0
    result = []

    while not outOfBound(row, col, height, width):
        result.append(array[row][col])
        print(goingDown)
        print(row,col)
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col+=1
                else:
                    row +=1
            else:
                col -=1
                row +=1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row+=1
                else:
                    col+=1
            else:
                col +=1
                row -=1
    return  
                
def outOfBound(row,col, height, width):
    return row < 0 or row > height or col < 0 or col > width

x = zigzagTraverse([ [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]])
print(x)