def removeElement(nums, val):
    toMove = 0
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[i - toMove] = nums[
                i]  # przesuwamy inną wartość niż val na początek o tyle miejsc ile wystąpiła wartość
            k += 1  # zwiększamy licznik różnych elementów
        else:
            toMove += 1
    return k