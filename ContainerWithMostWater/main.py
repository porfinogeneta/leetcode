
def maxArea(height):
    # dwa wskaźniki, przesuwamy ten z mniejszą wysokością, obliczamy wymiary pojemnika
    # porównujemy z maksymalnymi wymiarami
    l,r = 0,len(height)-1
    max_tank = 0
    while l < r:
        h = min(height[l], height[r])
        w = r - l
        new_tank = h*w
        if new_tank > max_tank:
            max_tank = new_tank
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_tank


if __name__ == '__main__':
    ar = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    maxArea(ar)