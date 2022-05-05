from collections import Counter

class HarryPotter:
    def __init__(self):
        self.discount = {
            0: 1,
            1: 1,
            2: 0.95,
            3: 0.9,
            4: 0.8,
            5: 0.75,
        }

    def getPrice(self, books: list):
        total = 0;
        length = []
        while len(books):
            s = set(books)
            for e in s:
                books.remove(e)
            length.append(len(s))
        sizes = Counter(length)
        while sizes.get(3) and sizes.get(5):
            sizes[3] -= 1
            sizes[5] -= 1
            sizes[4] += 2
        for k in sizes.keys():
            total += 8 * k * self.discount[k] * sizes[k]

        return total

