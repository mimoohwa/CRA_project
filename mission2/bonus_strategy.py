class BonusStrategy:
    def add_points(self,player):
        if player.wednesday_count > 9:
            player.add_points(10)
        if player.weekend_count > 9:
            player.add_points(10)