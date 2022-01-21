class TennisGameHard:
    p2 = 0
    p1 = 0
    p1N: str
    p2N: str

    def __init__(self, p1N: str, p2N: str):
        self.p1N = p1N
        self.p2N = p2N

    def get_score(self):
        s: str

        if self.p1 < 4 and self.p2 < 4 and not (self.p1 + self.p2 == 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            if self.p1 == self.p2:
                return s + "-All"
            return s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N

            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s


    def WonPoint(self, player_name: str):
        if player_name == "player1":
            self.p1 += 1;
        else:
            self.p2 += 1;