def classPhotos(redShirtHeights, blueShirtHeights):
    if len(redShirtHeights) != len(blueShirtHeights):
        return 'FALSE'
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    first_row = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if first_row == 'RED':
            if redShirtHeight > blueShirtHeight:
                return False
        else:
            if blueShirtHeight > redShirtHeight:
                return False

    return True


blue_shirt = [6, 4, 2, 9, 5]
red_shirt = [5, 8, 1, 3, 4]
y = classPhotos(red_shirt, blue_shirt)
print(y)
