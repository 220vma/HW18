def u_reader(fp):
    was = {}
    with open(fp, "r") as f:
        for line in f:
            try:
                if was[line] == 1:
                    continue
            except KeyError:
                was[line] = 1
                line = line.strip()
                yield line

if __name__ == "__main__":
    gen = u_reader("file.txt")
    try:
        while True:
            print(next(gen))
    except Exception as e:
        print(e)