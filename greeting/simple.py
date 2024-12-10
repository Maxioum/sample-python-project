import logging
from pathlib import Path


logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """Greet the person.

    :param name: the name of the person to greet.
    :return the generated message.
    """

    message: str = f"Hello {name} !"

    logger.debug("The following message will be printed: %s", message)

    print(message)

    return message
