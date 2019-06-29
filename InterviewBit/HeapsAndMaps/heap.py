class MinHeap(list):
    def _swap(self, i, j):
        tmp = self[i]
        self[i] = self[j]
        self[j] = tmp

    def _sift_up(self, ind):
        if ind == 0:
            return
        parent = (ind-1) // 2
        if self[ind][0] < self[parent][0]:
            self._swap(ind, parent)
            self._sift_up(parent)

    def _sift_down(self, ind):
        left_ch = 2*ind + 1
        right_ch = 2*ind + 2
        if left_ch >= len(self):
            return
        min_ch = left_ch
        if right_ch < len(self) and self[right_ch][0] < self[left_ch][0]:
            min_ch = right_ch
        if self[ind][0] > self[min_ch][0]:
            self._swap(ind, min_ch)
            self._sift_down(min_ch)

    def insert(self, key, value):
        self.append((key, value))
        self._sift_up(len(self)-1)

    def get_min(self):
        if not self:
            return
        return self[0]

    def extract_min(self):
        if not self:
            return
        min_kv = self[0]
        last_kv = self.pop()
        if self:
            self[0] = last_kv
            self._sift_down(0)
        return min_kv

    @classmethod
    def from_iterable(cls, it):
        h = cls()
        for k, v in it:
            h.append((k, v))
        for ind in range(len(h)-1, -1, -1):
            h._sift_down(ind)
        return h
