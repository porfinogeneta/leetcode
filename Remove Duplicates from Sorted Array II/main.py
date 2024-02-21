def removeDuplicates(nums):
    i, j = 0, 1
    toMove = 0  # o ile elementów przesuwać liczby, w razie wystąpień wcześniej za dużej liczby powtórzeń
    k = 1  # liczba poprawnych elementów
    while j < len(nums):
        if nums[i] == nums[j]:
            # sprawdzamy czy nie było za dużo wystąpień danej liczby
            if j - i <= 1:
                nums[j - toMove] = nums[j]
                k += 1
            else:
                toMove += 1
        else:
            i = j
            # po zmianie indexów chcemy też przesunąć odpowiednio wartości
            nums[j - toMove] = nums[j]
            k += 1

        j += 1
    return k

print(removeDuplicates([1,1,1,2,2,3]))