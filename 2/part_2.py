from dataclasses import dataclass, fields

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
    
    def update_to_maxium(self, other: "Result"):
        for field in fields(self):
            setattr(self, field.name, max(getattr(self, field.name), getattr(other, field.name)))

        
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
    
    def minimum_cubes(self):
        final_result = Result()
        for result in self.results:
            final_result.update_to_maxium(result)
        return final_result

    def __str__(self) -> str:
        return (f"Game id: {self.id}; Results: {self.results}")
        

with open("input.txt") as f:
    valid_sum = 0
    for raw_game in f:
        game = Game.parse(raw_game)
        min_cubles = game.minimum_cubes()
        valid_sum+=min_cubles.red * min_cubles.green * min_cubles.blue

print(valid_sum)
    
