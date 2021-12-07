import cmd

class Submarine(cmd.Cmd):
    depth = 0
    horizontal = 0
    aim = 0
    use_rawinput = False

    def do_forward(self, args):
        self.horizontal += int(args[0])
        self.depth += self.aim * int(args[0])

    def do_down(self, args):
        self.aim += int(args[0])

    def do_up(self, args):
        self.aim -= int(args[0])

if __name__ == '__main__':
    sub = Submarine()
    with open("input_day2") as f:
        for line in f.readlines():
            sub.onecmd(line)

    print(sub.depth, sub.horizontal)
    print(sub.depth * sub.horizontal)

