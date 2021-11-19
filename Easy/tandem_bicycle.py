def tandem(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        reverseTeamSpeed(redShirtSpeeds)

    total_speed = 0

    for idx in range(len(redShirtSpeeds)):
        redShirtSpeed = redShirtSpeeds[idx]
        blueShirtSpeed = blueShirtSpeeds[len(blueShirtSpeeds) - idx - 1]
        total_speed += max(redShirtSpeed, blueShirtSpeed)

    return total_speed


def reverseTeamSpeed(array):
    start = 0
    end = len(array)-1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1


red = [5, 5, 3, 9, 2]
blue = [3, 6, 7, 2, 1]

y = tandem(red, blue, False)
print(y)
