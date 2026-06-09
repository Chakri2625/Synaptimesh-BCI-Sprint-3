from queue import Queue

command_queue = Queue()


def add_command(command):

    command_queue.put(command)

    print(
        f"[QUEUE] {command} added"
    )


def process_queue():

    while not command_queue.empty():

        command = command_queue.get()

        print(
            f"[EXECUTING] {command}"
        )

        print(
            f"[COMPLETED] {command}"
        )