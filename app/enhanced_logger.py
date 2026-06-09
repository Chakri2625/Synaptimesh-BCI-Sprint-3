import logging

logging.basicConfig(
    filename="execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def log_command(message):

    logging.info(message)

    print()

    print("[LOGGER]")

    print(message)

    print("Saved to execution.log")

    print()