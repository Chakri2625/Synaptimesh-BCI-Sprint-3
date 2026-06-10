import os
import time

from app.keyboard_controller import *

os.system(
    "start notepad"
)

time.sleep(2)

type_text(
    "Sprint 4 Day 3"
)

select_all()

copy()

paste()

undo()

redo()

save()