from abc import ABC, abstractmethod


class Query(ABC):
    @abstractmethod
    def serialize(self) -> dict[str, str]:
        pass
