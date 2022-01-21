
class TennisGameEasy:
    P1point = 0
    P2point = 0
    P1res = ""
    P2res = ""
    player1Name: str
    player2Name: str

    def __init__(self, player1_name: str, player2_name: str):
        self.player1Name = player1_name
        self.player2Name = player2_name

    def get_score(self):
        score = ""

        if self.P1point == self.P2point and self.P1point < 4:
            if self.P1point == 0:
                score = "Love"
            if self.P1point == 1:
                score = "Fifteen"
            if self.P1point == 2:
                score = "Thirty"
            score += "-All"

        if self.P1point == self.P2point and self.P1point >= 3:
            score = "Deuce"

        if self.P1point > 0 and self.P2point == 0:
            if self.P1point == 1:
                self.P1res = "Fifteen"
            if self.P1point == 2:
                self.P1res = "Thirty"
            if self.P1point == 3:
                self.P1res = "Forty"

            self.P2res = "Love"
            score = self.P1res + "-" + self.P2res

        if self.P2point > 0 and self.P1point == 0:
            if self.P2point == 1:
                self.P2res = "Fifteen"
            if self.P2point == 2:
                self.P2res = "Thirty"
            if self.P2point == 3:
                self.P2res = "Forty"

            self.P1res = "Love"
            score = self.P1res + "-" + self.P2res

        if self.P1point > self.P2point and self.P1point < 4:
            if self.P1point == 2:
                self.P1res = "Thirty"
            if self.P1point == 3:
                self.P1res = "Forty"
            if self.P2point == 1:
                self.P2res = "Fifteen"
            if self.P2point == 2:
                self.P2res = "Thirty"
            score = self.P1res + "-" + self.P2res

        if self.P2point > self.P1point and self.P2point < 4:
            if self.P2point == 2:
                self.P2res = "Thirty"
            if self.P2point == 3:
                self.P2res = "Forty"
            if self.P1point == 1:
                self.P1res = "Fifteen"
            if self.P1point == 2:
                self.P1res = "Thirty"
            score = self.P1res + "-" + self.P2res

        if self.P1point > self.P2point and self.P2point >= 3:
            score = "Advantage player1"

        if self.P2point > self.P1point and self.P1point >= 3:
            score = "Advantage player2"

        if self.P1point >= 4 and self.P2point >= 0 and (self.P1point - self.P2point) >= 2:
            score = "Win for player1"

        if self.P2point >= 4 and self.P1point >= 0 and (self.P2point - self.P1point) >= 2:
            score = "Win for player2"
        return score

    def P1Score(self):
        self.P1point += 1

    def P2Score(self):
        self.P2point += 1

    def WonPoint(self, player: str):
        if player == "player1":
            self.P1Score()
        else:
            self.P2Score()

    def set_p1_score(self, number: int):
        for i in range(number):
            self.P1Score()

    def set_p2_score(self, number: int):
        for i in range(number):
            self.P1Score()

