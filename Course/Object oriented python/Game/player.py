class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0
    # Underscores 'hides' the methods and the lives variable from the client

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 1:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level cannot be below 1")

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score
    # This is a different way to state a getter, using different syntax and decorators

    @score.setter
    def score(self, score):
        self._score = score
    # This is a way to write a setter using decorators

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level {0.level}, Score {0.score}".format(self)
    # This function allows the client to type print(object) and it will return this string,
    # holding information of the object
