def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # mamy słownik z wyliczonymi kluczami i dodajemy tam słowo
    # jeśli jest ono tak samo wyliczone
    hashmap = defaultdict(list)
    for s in strs:
        count = [0] * 26  # zliczamy dla każdego słowa litery
        for l in s:
            count[ord(l) - ord("a")] += 1

        hashmap[tuple(count)].append(s)  # w python listy nie mogą być kluczami
    return hashmap.values()