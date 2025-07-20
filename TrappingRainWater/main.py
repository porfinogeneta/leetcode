
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    idea: 1. zapisać dla każdego indeksu maximum z lewej i maksimum z prawej
    i policzyć wodę na każdym polu, czyli min(left_max, right_max) - h[i]
    2. zrobić dwa pointery i trzymać zmienne left_max, right_max, przechodząć
    pointerami znając mnijeszą wysokość wiemy ile co najwyżej wody się zmieści między nimi,
    przesuwamy zawsze pointer który ma mnijeszą wysokość max
    """
    lMax = height[0]
    rMax = height[-1]
    l,r = 0, len(height)-1
    trapped = 0
    # nie możemy wziąć skrajnego, bo woda się będzie wylewała w takim przypadku
    while l < r:
        # w przypadku równości też przesuwamy lewy
        if lMax <= rMax:
            l += 1
            # to nigdy nie będzie ujemne, bo zawsze lMax będzie odpowiednio większy albo równy height[l]
            lMax = max(lMax, height[l])
            trapped += lMax - height[l]

        else:
            r -= 1
            rMax = max(rMax, height[r])
            trapped += rMax - height[r]

    return trapped



if __name__ == '__main__':
    print(trap([4,2,0,3,2,5]))
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))