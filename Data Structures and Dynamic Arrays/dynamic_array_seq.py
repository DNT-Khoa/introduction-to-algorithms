from array_seq import Array_Seq

class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r = 2):                          # O(1)
        super().__init__()
        self.size = 0
        self.r = r
        self._computer_bounds()
        self.resize(0)

    def __len__(self):                                  # O(1)
        return self.size

    def __iter__(self):                                 # O(n)
        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):                                 # O(n)
        for a in X:
            self.insert_last(a)

    def _computer_bounds(self):                         # O(1)
        self.upper = len(self.A)
        self.lower = len(self.A)

    def _resize(self, n):                               # O(1) or O(n)
        if (self.lower < n < self.upper):
            return

        m = max(n, 1) * self.r
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)
        self.A = A
        self._computer_bounds()

    def insert_last(self, x):                           # O(1) a
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):                              # O(1) a
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)

    def insert_at(self, i, x):                          # O(n)
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):                             # O(n)
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x 
    
    def insert_first(self, x):                          # O(n)
        self.insert_at(0, x)

    def delete_first(self):                             # O(n)
        return self.delete_at(0)
    
