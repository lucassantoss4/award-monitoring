from abc import ABC, abstractmethod
from pathlib import Path

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, input_data) -> str:
        """
        Método padrão para extração.
        input_data pode ser um Caminho (Path), uma URL (str) ou um dicionário.
        """
        pass