def read_file(filename):
    with open(filename, "r") as f:
        return (
            int(f.readline()),
            int(f.readline()),
            [int(x) for x in f.readline().split(",")],
            [int(x) for x in f.readline().split(",")],
            [int(x) for x in f.readline().split(",")],
        )
