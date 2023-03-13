from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data) -> str:
        pass


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data) -> str:
        return f"Algorithm A on {data}"


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data) -> str:
        return f"Algorithm B on {data}"


class Context:
    _strategy: Strategy = None

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        # ...
        result = self._strategy.do_algorithm("data")
        # ...
        print(result)
