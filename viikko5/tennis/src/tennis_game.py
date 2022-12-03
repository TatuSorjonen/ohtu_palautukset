class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_score_draw_under_4()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_4_or_more()

        else:
            return self.get_score_not_draw_under_4()

    def get_score_draw_under_4(self):
        if self.m_score1 == 0:
            score_description = "Love-All"
        elif self.m_score1 == 1:
            score_description = "Fifteen-All"
        elif self.m_score1 == 2:
            score_description = "Thirty-All"
        elif self.m_score1 == 3:
            score_description = "Forty-All"
        else:
            score_description = "Deuce"
        return score_description

    def get_score_4_or_more(self):
        if self.m_score1 - self.m_score2 == 1:
            score_description = "Advantage player1"
        elif self.m_score1 - self.m_score2 == -1:
            score_description = "Advantage player2"
        elif self.m_score1 - self.m_score2 >= 2:
            score_description = "Win for player1"
        else:
            score_description = "Win for player2"
        return score_description

    def get_score_not_draw_under_4(self):
        if self.m_score1 == 0:
            player1_score_description = "Love-"
        elif self.m_score1 == 1:
            player1_score_description = "Fifteen-"
        elif self.m_score1 == 2:
            player1_score_description = "Thirty-"
        elif self.m_score1 == 3:
            player1_score_description = "Forty-"

        if self.m_score2 == 0:
            player2_score_description = "Love"
        elif self.m_score2 == 1:
            player2_score_description = "Fifteen"
        elif self.m_score2 == 2:
            player2_score_description = "Thirty"
        elif self.m_score2 == 3:
            player2_score_description = "Forty"

        return player1_score_description + player2_score_description
