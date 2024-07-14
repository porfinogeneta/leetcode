
# O(n^2)
# hasAccessToEnd = [False for _ in range(len(nums))]
# hasAccessToEnd[-1] = True
# for i in range(len(nums) - 2, -1, -1):
#     for step in range(1, nums[i] + 1):
#         if i + step < len(hasAccessToEnd) and hasAccessToEnd[i + step]:
#             hasAccessToEnd[i] = True
#             break
# return hasAccessToEnd[0]
# O(n)
# obliczamy maksymalny przeskok w tablicy i sprawdzamy czy jest ≥ od n
# będziemy to robić następująco -> wchodzimy na dany element i sprawdzamy
# czy można nim dotrzeć dalej niż korzystając z poprzedniego elementu
# jeśli tak robimy z niego nasz nowy maksymalny przeskok i badamy go
# wizualizacja to każda liczba to benzyna i przesuwamy się po liczbach dopóki
# nie skończy się nam benzyna albo natrafimy na większą niż aktualna wartość benzyny w baku,
# każde przesunięcie zmniejsza ilość benzyny o 1, jak wchodząc na dany element nie mamy benzyny,
# to nie można się dostać do końca tablicy
def canJump(nums):
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        if n > gas:
            gas = n
        gas -= 1
    return True


if __name__ == '__main__':
    print(canJump([2,3,1,1,4]))