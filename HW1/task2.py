class TowersOfHanoi:
    def __init__(self):
        self.number_of_moves = 0
        self.rods = [[i for i in range(n_disks, 0, -1)], [], []]

    def play(self, number_of_disks, start_rod=1, final_rod=3):
        if number_of_disks == 1:
            self.move(self.rods[start_rod-1], self.rods[final_rod-1])
            print(self.rods)
        else:
            rod_range = [i for i in range(1, 4)]
            rod_range.remove(start_rod)
            rod_range.remove(final_rod)
            new_final_rod = rod_range[0]
            self.play(number_of_disks - 1, start_rod, new_final_rod)
            self.play(1, start_rod, final_rod)
            self.play(number_of_disks - 1, new_final_rod, final_rod)

    def move(self, first_rod, second_rod):
        second_rod.append(first_rod.pop())
        self.number_of_moves += 1


n_disks = int(input("Enter a number of disks:"))
game = TowersOfHanoi()
game.play(n_disks)
print("Number of moves =", game.number_of_moves)
