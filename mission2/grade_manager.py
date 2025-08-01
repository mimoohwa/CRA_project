class GradeManager:
    def get_grade(self,player):
        if player.points >= 50:
            return "GOLD"
        elif player.points >= 30:
            return "SILVER"
        else:
            return "NORMAL"