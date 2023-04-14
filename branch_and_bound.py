import file_operations as fo


class Node:
    def __init__(self, w, v, c, i):
        self.weight = w
        self.value = v
        self.label = c
        self.index = i  # index in the original array since we need to do some sorting
        self.cost = v / w  # idk old man said to do this

    def print(self):  # mainly for debugging
        print("weight: ", self.weight)
        print("value: ", self.value)
        print("class: ", self.label)
        print("index: ", self.index)
        print("cost: ", self.cost)


class Solver:
    def __init__(self, input="input.txt", output="output.txt"):
        self.upper_bound = 0
        self.answer = []
        self.data = []  # list of Nodes
        (
            self.capacity,
            self.num_of_class,
            self.weight,
            self.value,
            self.label,
        ) = fo.read_file(input)
        self.data = list(
            Node(self.weight[i], self.value[i], self.label[i], i)
            for i in range(self.weight.__len__())
        )
        self.zmap = {i: self.data[i] for i in range(len(self.data))}
        self.data.sort(key=lambda x: x.cost, reverse=True)  # prio q
        self.file_out = output

    def print(self):
        temp = 0
        temp_str = ""
        for i, idx in enumerate(self.answer):
            temp_str += str(idx) + ", "
            temp += idx * self.zmap[i].value
        temp_str = temp_str[:-2]
        print(temp)
        print(temp_str)
        with open(self.file_out, "w") as f:
            f.write(str(temp) + "\n" + temp_str)
        f.close()

    def class_check(self, candidate):
        # check whether candidate contains all classes
        classes = set()
        for i, idx in enumerate(candidate):
            if idx == 1:
                classes.add(self.label[i])
        return len(classes) == self.num_of_class

    def solve(self):
        candidate = [0] * len(self.data)
        self.solve_branch_and_bound(candidate, 0, self.capacity, 0)
        self.print()

    def solve_branch_and_bound(self, candidate, depth, current_weight, current_value):
        for i in range(2):
            candidate[self.data[depth].index] = i
            if i == 1:
                current_weight -= self.data[depth].weight
                current_value += self.data[depth].value
            if current_weight >= 0:
                if depth == len(self.data) - 1:
                    if current_value > self.upper_bound and self.class_check(candidate):
                        self.upper_bound = current_value
                        self.answer = candidate.copy()
                elif (  # best value (not)achievable but told to do it anyway
                    current_value + current_weight * self.data[depth + 1].cost
                    > self.upper_bound
                ):
                    self.solve_branch_and_bound(
                        candidate, depth + 1, current_weight, current_value
                    )
            # if i == 1:    # this is not needed since we are not going to use the candidate # array again
            #     current_weight += self.data[depth].weight
            #     current_value -= self.data[depth].value


if __name__ == "__main__":
    s = Solver("dataset.txt")
    s.solve()
