class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def win_ball(self):
        self.score += 1


score_dict = {
    0: "love",
    1: "fifteen",
    2: "thirty",
    3: "forty"
}


def is_normal(p1_score, p2_score):
    return (p1_score > 0 or p2_score > 0) and not is_same(p1_score, p2_score)


def is_initial(p1_score, p2_score):
    return p1_score == 0 and p2_score == 0


def is_deuce(p1_score, p2_score):
    return p1_score >= 3 and p2_score >= 3 and is_same(p1_score, p2_score)


def is_same(p1_score, p2_score):
    return p1_score == p2_score


def is_game(p1_score, p2_score):
    return (p1_score >= 4 or p2_score >= 4) and abs(p1_score - p2_score) > 1


def is_advantage(p1_score, p2_score):
    return (p1_score > 3 or p2_score > 3) and not is_same(p1_score, p2_score) and not is_game(p1_score, p2_score)


def is_game_point(p1_score, p2_score):
    return (p1_score == 3 or p2_score == 3) and not is_game(p1_score, p2_score)


def game_point(player_1, player_2):
    game_point_player = player_1 if player_1.score > player_2.score else player_2
    return "{} game point".format(game_point_player.name)


def advantage(player_1, player_2):
    advantage_player = player_1 if player_1.score > player_2.score else player_2
    return "{} advantage".format(advantage_player.name)


def game(player_1, player_2):
    winner = player_1 if player_1.score > player_2.score else player_2
    return "{} game".format(winner.name)


def normal_score(p1_score, p2_score):
    return "{}-{}".format(score_dict.get(p1_score), score_dict.get(p2_score))


def same_score(p1_score, p2_score):
    if is_initial(p1_score, p2_score):
        return "all-love"
    return "{}-all".format(score_dict.get(p1_score))


def announce_score(player_1, player_2):
    p1_score = player_1.score
    p2_score = player_2.score

    if is_deuce(p1_score, p2_score):
        return "Deuce"
    elif is_advantage(p1_score, p2_score):
        return advantage(player_1, player_2)
    elif is_game_point(p1_score, p2_score):
        return "{}\n{}".format(normal_score(p1_score, p2_score), game_point(player_1, player_2))
    elif is_game(p1_score, p2_score):
        return game(player_1, player_2)
    elif is_normal(p1_score, p2_score):
        return normal_score(p1_score, p2_score)
    else:
        return same_score(p1_score, p2_score)
