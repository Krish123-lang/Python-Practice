# Reference: https://rszalski.github.io/magicmethods/

class Point:
    def __init__(self, x, y) -> None:  # CONSTRUCTOR
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:  # EQUAL TO
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:  # NOT EQUAL TO
        return self.x != other.x and self.y != other.y

    def __lt__(self, other) -> bool:  # LESS THAN
        return self.x < other.x and self.y < other.y

    def __gt__(self, other) -> bool:  # GREATER THAN
        return self.x > other.x and self.y > other.y

    def __le__(self, other) -> bool:  # LESS THAN OR EQUAL TO
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other) -> bool:  # GREATER THAN OR EQUAL TO
        return self.x >= other.x and self.y >= other.y


point = Point(5000, 4000)  # OBJECT 1
other = Point(50, 40)  # OBJECT 2
# print(point == other)
# print(point != other)
# print(point < other)
# print(point > other)
# print(point < other)
# print(point >= other)
