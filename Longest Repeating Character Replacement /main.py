import string

# jak działa algorytm?
# w każdej iteracji obliczamy długość okna, odejmujemy od niej długość najdłuższego
# ciągu tej samej litery, który moglibyśmy do tego momentu zrobić,
# w efekcie otrzymujemy ile trzeba będzie zastąpić liter,
# porównujemy z k i patrzymy czy nas na tą zamianę stać, jeśli tak to zwiększamy okno (r+1),
# wpp. zmniejszamy okno l+1
# rozszerzamy okno, jeśli stać nas na zamianę liter
# złożoność O(26n)
# można optymalniej jak się zauważy że zmiana wyniku na większy występuje wylko jak zwiększy się
# maksymalna częstotliwość wystąpień danej litery
def characterReplacement(s, k):
    # dwa pointery na początek i koniec okna
    l,r = 0, 0
    counter = dict.fromkeys(string.ascii_uppercase,0)
    # długość najdłuższego wyniku
    res = 0
    # prawy dojeżdża do końca, lewego nie ma sensu sprawdzać
    while r != len(s) and (r - l + 1) > res:
        window_len = r - l + 1
        counter[s[r]] += 1
        if window_len - max(counter.values()) <= k:
            res = max(res, window_len)
        else:
            counter[s[l]] -= 1
            l += 1
        r += 1

    return res


if __name__ == "__main__":
    print(characterReplacement("AABABBA", 1))