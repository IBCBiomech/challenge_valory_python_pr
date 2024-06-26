# message_generator.py

from abc import ABC, abstractmethod
from datetime import datetime

class AbstractBehaviour(ABC):
    """
    Abstract base class for generating messages based on input parameters.

    :cvar ABC: Marks the class as an abstract base class.
    """

    @abstractmethod
    def process_message(self) -> str:
        """
        Abstract method to generate a message from the provided input.

        :param input_data: The data used to generate the message.
        :type input_data: Any
        :return: The generated message.
        :rtype: str
        """

