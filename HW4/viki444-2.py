from math import sqrt


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        res = "("
        for i in self.vec:
            res += str(i) + ","
        res = res[:-1] + ")"
        return res

    def add(self, vec):
        self.check_len(vec)
        res = []
        for i in range(len(self.vec)):
            res.append(self.vec[i] + vec.vec[i])
        return Vector(res)

    def subtract(self, vec):
        self.check_len(vec)
        res = []
        for i in range(len(self.vec)):
            res.append(self.vec[i] - vec.vec[i])
        return Vector(res)

    def dot(self, vec):
        self.check_len(vec)
        res = 0
        for i in range(len(self.vec)):
            res += self.vec[i] * vec.vec[i]
        return res

    def norm(self):
        res = 0
        for i in self.vec:
            res += i * i
        return sqrt(res)

    def equals(self, vec):
        for i in range(len(vec.vec)):
            if vec.vec[i] != self.vec[i]:
                return False
        return True

    def check_len(self, vec):
        if len(vec.vec) != len(self.vec):
            raise Exception("Lengths of vectors must be equal!")
