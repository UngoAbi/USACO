class SubTestCase:
    def __init__(self, n, k, grid):
        self.n = n
        self.k = k
        self.grid = grid
        self.paths = 0

    def __repr__(self):
        return f"SubTestCase({self.k = } {self.grid = })"

    def depth_first_search(self, pos=(0, 0), k=None, d=True):
        if pos == (self.n - 1, self.n - 1):
            self.paths += 1
        if k is None:
            k = self.k

        x, y = pos
        if not self.is_inbounds(x, y) or self.grid[y][x] == "H":
            return

        self.depth_first_search(self.get_new_pos(x, y, d), k, d)
        if k != 0:
            d = not d
            k = k if pos == (0, 0) else k-1
            self.depth_first_search(self.get_new_pos(x, y, d), k, d)

    @staticmethod
    def get_new_pos(x, y, d):
        match d:
            case True:
                x, y = x + 1, y
            case False:
                x, y = x, y + 1
        return x, y

    def is_inbounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n


def main():
    test_cases = get_test_cases()
    for test_case in test_cases:
        test_case.depth_first_search()
        print(test_case.paths)


def get_test_cases():
    test_cases = list()
    t = int(input("t: "))
    for i in range(t):
        n, k = [int(x) for x in input(f"{i} n, k: ").split(" ")]
        grid = [[x for x in input(f"{j} r: ")] for j in range(n)]
        test_cases.append(SubTestCase(n, k, grid))
    return test_cases


if __name__ == "__main__":
    main()
