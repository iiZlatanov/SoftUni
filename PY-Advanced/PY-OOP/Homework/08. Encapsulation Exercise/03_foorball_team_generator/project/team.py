from project.player import Player
from typing import List, Union


class Team:
    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"

        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str) -> Union[str, Player]:
        try:
            player = [p for p in self.__players if p.name == player_name][0]
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"
