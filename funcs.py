class HarryPotter:
    def __init__(self):
        self.discount = {
            0: 0,
            1: 0,
            2: 0.05,
            3: 0.1,
            4: 0.2,
            5: 0.25,
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

