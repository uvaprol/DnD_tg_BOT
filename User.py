from Actor import *
class User():
    __state: [None, str] = None
    __name: str = 'Путник'
    __actor: object = Actor()
    @property
    def state(self) -> str:
        return self.__state
    @state.setter
    def state(self, state: str) -> None:
        self.__state = state
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    @property
    def actor(self) -> object:
        return self.__actor
    @actor.setter
    def actor(self, actor: object) -> None:
        self.__actor = actor
