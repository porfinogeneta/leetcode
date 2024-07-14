# zasada działania algorytmu
# mamy dwa słowniki, jeden z wyrazem, który chcemy znaleźć i drugi z aktualnym stringiem
# przechodzimy po stringu s i rozszerzamy okno dopóki liczba elementów w oknie nie będzie taka
# sama jak liczba elementów nam potrzebna
# jak nasze okno będzie dostatecznie duże to zaczynamy je zmniejszać od lewej strony
# do momentu aż liczba elementów w oknie jest zgodna z tym ile potrzebujemy
# przechodzimy tak cały string s i kończymy jak prawy pointer dojdzie do końca
def minWindow(s, t):
    # jak s jest krótsze nie ma co porównywać
    if len(s) < len(t):
        return ""

    # robimy słownik dla tego co potrzebujemy
    need = {c: t.count(c) for c in t}
    # i analogiczny dla tego co mamy
    have = {key: 0 for key in need}
    have_cnt = 0
    need_cnt = len(need) # potrzebujemy tyle różnych znaków

    l = 0
    # tworzymy wynikowy string
    min_sub = len(s) + 1
    min_sub_l, min_sub_r = -1, -1
    # przesuwamy po kelei prawy pointer
    for r in range(len(s)):
        # jak aktualny element jest potrzebny to zwiększamy jego ilość
        if s[r] in need:
            have[s[r]] += 1
            # zwiększamy licznik, tylko jak potrzebowaliśmy elementu, czyli teraz nam się zrównał po dodaniu
            if have[s[r]] == need[s[r]]:
                have_cnt += 1

        # przesuwamy lewy tylko dopóki mamy cały czas tyle ile potrzebujemy
        while have_cnt == need_cnt:
            # przy każdej iteracji, skoro skróciliśmy substring to trzeba zupdatować wynik
            if (r - l + 1) < min_sub:
                min_sub_r = r
                min_sub_l = l
                min_sub = r - l + 1
            # jak element jest w t to trzeba zmniejszyć nasz stan posiadania w have
            if s[l] in t:
                have[s[l]] -= 1
                # jak zmniejszając ilość sprawimy, że potrzebujemy elementu to zmniejszamy to co mamy
                if have[s[l]] < need[s[l]]:
                    have_cnt -= 1
            l += 1

    return s[min_sub_l:min_sub_r + 1] if min_sub != len(s) + 1 else ""


if __name__ == "__main__":
    print(minWindow("adobecodebanc", "abc"))
    print(minWindow("a", "a"))
    print(minWindow("a", "aa"))
    print(minWindow("a", "b"))
    print(minWindow("aa", "aa"))
