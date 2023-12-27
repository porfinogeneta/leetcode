

def largestRectangleArea(heights):
    max_area = -1
    stack = []
    for i,h in enumerate(heights):
        # element który dodajmy umożliwia rozszerzenie pola korzystając z poprzedniego
        if not stack or h >= stack[-1][1]:
            stack.append((i, h))
        else:
            # usuwamy ze stosu dopóki nowo dodana wysokość uniemożliwia rozszerzanie poprzednich
            new_beginning = -1
            while stack and h < stack[-1][1]:
                top_i, top_h = stack.pop()
                max_area = max(max_area, (i - top_i) * top_h) # pole liczone do obecnego indeksu
                new_beginning = top_i
            stack.append((new_beginning, h))
    # po przejściu stosem chcemy obadać pozostałe pola
    # zawsze przy liczeniu wymiarów tych prostokątów które zostały odnosimy się do ostatniego
    end_idx = len(heights)
    while stack:
        top_i, top_h = stack.pop()
        max_area = max(max_area, (end_idx - top_i) * top_h)

    return max_area


if __name__ == '__main__':
    heights = [1,1]
    print(largestRectangleArea(heights))