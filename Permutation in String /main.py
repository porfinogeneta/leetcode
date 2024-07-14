import string


# jak działa algorytm
# można ten problem rozwiązać na dwa sposoby:
# 1. O(26n) -> przechodzić oknem o rozmiarze s1, zliczać odpowiednie elementy i porównywać za każdym razem
# ze słownikiem zbudowanym na s1
# 2. zbudować raz słownik na s1 i na len(s1) pierwszych elementach s2
# przechodzić oknem o rozmiarze len(s1) po s2 i modyfikować liczbę matchy, czyli
# liczbę wspólnych elementów między oboma słownikami, jak będziemy mieli 26 matchy ->
# elementów wspólnych między słownikami s1 i s2 będzie tyle samo mamy matcha

def checkInclusion(s1, s2):
    # jak string w którym mamy szukać permutacji jest mniejszy to na pewno nie ma co szukać
    if len(s1) > len(s2):
        return False
    counter_s1 = dict.fromkeys(string.ascii_lowercase, 0)
    counter_s2 = dict.fromkeys(string.ascii_lowercase, 0)
    # uzupełniamy hashmapy o długość permutacji
    for i in range(len(s1)):
        counter_s1[s1[i]] += 1
        counter_s2[s2[i]] += 1

    matches = 26
    # liczymy matche
    for key, value in counter_s2.items():
        if counter_s1[key] != value:
            matches -= 1

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True
        # przesuwając się w z oknem dodajemy literę do słownika
        counter_s2[s2[r]] += 1
        # jak dodanie sprawiło że mamy takie same wartości w permutacji
        if counter_s2[s2[r]] == counter_s1[s2[r]]:
            matches += 1
        # wcześniej były równe więc straciliśmy matcha
        elif counter_s1[s2[r]] + 1 == counter_s2[s2[r]]:
            matches -= 1
        # przesuwając się z oknem odejmujemy element ze słownika
        counter_s2[s2[l]] -= 1
        # po odjęciu elementu możemy dostać matcha
        if counter_s2[s2[l]] == counter_s1[s2[l]]:
            matches += 1
        # mogło być tak że wcześniej był match, więc teraz musimy go odjąć
        elif counter_s1[s2[l]] - 1 == counter_s2[s2[l]]:
            matches -= 1

        l += 1

    # match mógł wystąpić po przerobieniu całej pętli
    return matches == 26


if __name__ == "__main__":
    print(checkInclusion("ab", "eidbaooo"))
