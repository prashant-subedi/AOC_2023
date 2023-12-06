from dataclasses import dataclass

@dataclass
class Result:
    red: int  = 0
    green: int = 0
    blue: int = 0

    def is_possible(self, red, green, blue) -> bool:
        return (
            red >= self.red
            and green >= self.green
            and blue >= self.blue
        )

        
class Game:
    @classmethod
    def parse(cls, line: str):
        raw_game_id, raw_results = line.split(":", 1)
        game_id = int(raw_game_id[5:])
        obj = cls(game_id)
        
        for raw_result in raw_results.split(";"):
            color_count = {}
            for raw_ball_count in raw_result.split(", "):
                count, color = raw_ball_count.strip().split(" ")
                color_count[color] = int(count)
            obj.add_result(color_count)

        return obj

    def __init__(self, id: int):
        self.id = id
        self.results = []

    def add_result(self, result_dict: dict):
        self.results.append(Result(**result_dict))

    def is_valid(self, red: int, green: int, blue: int) -> bool:
        for result in self.results:
            if not result.is_possible(red, green, blue):
                return False
        return True

    
    def __str__(self) -> str:
        return (f"Game id: {self.id}; Results: {self.results}")
        

print(Game.parse("Game 79: 9 red, 11 green, 6 blue; 1 red, 3 green; 7 blue, 7 red, 11 green; 8 red, 9 blue, 11 green; 7 red, 11 green, 4 blue"))

with open("input.txt") as f:
    valid_sum = 0
    for raw_game in f:
        game = Game.parse(raw_game)
        if game.is_valid(red=12, green=13, blue=14):
            valid_sum+=game.id

print(valid_sum)
    
