class TennisGameMedium:
    m_score1 = 0
    m_score2 = 0
    player1Name = ""
    player2Name = ""

    def __init__(self, player1Name: str, player2Name: str):
        self.player1Name = player1Name
        self.player2Name = player2Name

    def WonPoint(self, playerName: str):
        if playerName == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        score = "";
        tempScore = 0;
        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0:
                score = "Love-All"
            elif self.m_score2 == 1:
                score = "Fifteen-All"
            elif self.m_score2 == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minusResult = self.m_score1 - self.m_score2
            if minusResult == 1:
                score = "Advantage player1"
            elif minusResult == -1:
                score = "Advantage player2"
            elif minusResult >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    tempScore = self.m_score1
                else:
                    score += "-"
                    tempScore = self.m_score2

                if tempScore == 0:
                    score += "Love"
                elif tempScore == 1:
                    score += "Fifteen"
                elif tempScore == 2:
                    score += "Thirty"
                elif tempScore == 3:
                    score += "Forty"
        return score