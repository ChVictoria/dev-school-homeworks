class Warrior:
    def __init__(self):
        self.level = 1
        self.experience = 100
        self.possible_ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror",
                               "Champion", "Master", "Greatest"]
        self.rank = self.possible_ranks[0]
        self.achievements = []

    def check_level(self):
        if self.level < 100:
            return True

    def update(self):
        if self.experience > 10000:
            self.experience = 10000
        self.level = int(self.experience // 100)
        self.rank = self.possible_ranks[int(self.level // 10)]

    def battle(self, enemy_level):
        if enemy_level in range(1, 101):
            diff = enemy_level - self.level
            if self.check_level:
                if diff == 0:
                    self.experience += 10
                elif diff == -1:
                    self.experience += 5
                elif diff > 0 and diff < 5:
                    self.experience += 20 * diff * diff
                self.update()
            if diff <= -2:
                return "Easy fight"
            elif diff == 0 or diff == -1:
                return "A good fight"
            elif diff >= 5 and self.possible_ranks.index(self.rank) < int(enemy_level // 10):
                return "You've been defeated"
            else:
                return "An intense fight"

        return "Invalid level"

    def training(self, param):
        if self.level >= param[2]:
            if self.check_level:
                self.experience += param[1]
                self.update()
            self.achievements.append(param[0])
            return param[0]
        return "Not strong enough"
