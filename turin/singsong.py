def singsong(n: int):
    for bottle in range(n,0,-1):
        if bottle > 1:
            print(f'{bottle} bottles of beer on the wall, {bottle} bottles of beer.')
            print(f'Take one down and pass it around, {bottle-1} bottles of beer on the wall.')
        else:
            print(f"{bottle} bottle of beer on the wall, {bottle} bottle of beer. \nTake one down and pass it around, no more bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
            
            
x = singsong(99)
print(x)
