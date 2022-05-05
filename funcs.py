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
        while len(books):
            s = set(books)
            discount = self.discount[len(s)]
            total += len(s) * 8 * discount
            for e in s:
                books.remove(e)
        return total

