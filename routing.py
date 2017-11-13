import random
import uuid

class operator:
    def __init__(self):
        self.name = ""
        self.dictionary = {}

    def isCandidate(self,entry):
        if self.check_number(entry):
            return [True, self.get_longest_code_length(entry)]
        else:
            return [False,-1]

    def check_number(self,entry):
        for code in self.dictionary.keys():
            if entry.startswith(str(code)):
                return True
            else:
                return False
    def get_longest_code_length(self, entry):
        tab = []
        for code in self.dictionary.keys():
            code = str(code)
            if str(entry).startswith(code):
                tab.append(len(code))
        return max(tab)

    def get_longest_code(self, entry):
        tab = []
        for code in self.dictionary.keys():
            code = str(code)
            if str(entry).startswith(code):
                tab.append(code)
        return max(tab)

    def generate_random(self):
        codesCount = random.randint(20,1000)
        for i in range(codesCount):
            code = random.randint(1,200)
            price = random.randint(100,500)*0.01
            self.dictionary.update({code:price})
        self.name = uuid.uuid4()
    def prints(self):
        print self.name, self.dictionary

class operators(list):
    def __init__(self):
        list.__init__(self)

    def getCandidates(self, entry):
        tmp = operators()
        maxLength = 0
        for op in self:
            vals = op.isCandidate(entry)
            if vals[0]:
                if vals[1] >= maxLength:
                    maxLength = vals[1]
        for op in self:
            vals = op.isCandidate(entry)
            if vals[1] == maxLength:
                tmp.append(op)
        return tmp

    def findCandidates(self,entry):
        tmp = operators()
        for op in self:
            vals = op.isCandidate(entry)
            if vals[0]:
                tmp.append(op)
        return tmp

    def iterate(self,entry):
        size = 0
        tmp = self
        while size != len(tmp):
            size = len(tmp)
            tmp = tmp.getCandidates(entry)
        return tmp

    def prints(self):
        print "Name","Dictionary",len(self)
        for i in self:
            i.prints()
    @staticmethod
    def getCheapest(opes,entry):
        if len(opes) == 0:
            return None
        else:
            lc = int(opes[0].get_longest_code(entry))
            vals = []
            for op in opes:
                vals.append(op.dictionary[lc])
            return opes[vals.index(min(vals))],op.dictionary[lc]

class scenario:
    def scenario1(self):
        """Single operator"""
        ops = operators()
        op = operator()
        op.name = "Operator 1"
        op.dictionary = {1: 2.23, 79: 3.3, 43: 1.82, 173: 3.94, 143: 1.15, 146: 4.44, 51: 2.55, 149: 3.53, 54: 4.45,
                    23: 3.5,
                    89: 4.5, 187: 2.1, 53: 4.27}
        ops.append(op)

        ops = ops.iterate("128548")
        op = ops.getCheapest(ops,"128548")
        print op

if __name__ == '__main__':
    scenario().scenario1()

