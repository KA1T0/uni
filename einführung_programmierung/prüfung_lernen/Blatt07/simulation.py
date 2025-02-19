from dataclasses import dataclass
from enum import Enum


# a)
class State(Enum):
    RUNNING = 'running'
    IDLE = 'idle'


@dataclass(frozen=True)
class Machine:
    state: State
    time_left: int


# b)
def time_step(machine: Machine) -> Machine:
    match machine:
        case Machine(State.RUNNING):
            return Machine(State.RUNNING, machine.time_left - 1)
        case Machine(State.IDLE):
            return Machine(State.IDLE, machine.time_left)
        case Machine(State.RUNNING, 0):
            return Machine(State.IDLE, 0)
        case _:
            return machine


assert time_step(Machine(State.RUNNING, 42)) == Machine(State.RUNNING, 41)
assert time_step(Machine(State.RUNNING, 1)) == Machine(State.RUNNING, 0)
assert time_step(Machine(State.IDLE, 1337)) == Machine(State.IDLE, 1337)
assert time_step(Machine(State.IDLE, 0)) == Machine(State.IDLE, 0)


# c)
class Action(Enum):
    START = 'start'
    STOP = 'stop'
    NONE = 'none'


def apply_action(machine: Machine, action: Action) -> Machine:
    match machine, action:
        case Machine(State.IDLE, 0), Action.START:
            return machine
        case Machine(State.IDLE, machine.time_left), Action.START:
            return Machine(State.RUNNING, machine.time_left)
        case Machine(State.RUNNING, machine.time_left), Action.STOP:
            return Machine(State.IDLE, machine.time_left)
        case Machine(_, machine.time_left), Action.NONE:
            return machine
        case _:
            return machine


assert apply_action(Machine(State.IDLE, 42), Action.START) == Machine(State.RUNNING, 42)
assert apply_action(Machine(State.IDLE, 0), Action.START) == Machine(State.IDLE, 0)
assert apply_action(Machine(State.RUNNING, 42), Action.STOP) == Machine(State.IDLE, 42)
assert apply_action(Machine(State.RUNNING, 0), Action.STOP) == Machine(State.IDLE, 0)


# d)
def simulate(machine: Machine, actions: list[Action]) -> list[Machine]:
    machines = [machine]
    for action in actions:
        machine = apply_action(machine, action)
        machine = time_step(machine)
        machines = machines + [machine]
    return machines


machine = Machine(State.IDLE, 7)
assert simulate(machine, []) == [Machine(State.IDLE, 7)]
assert simulate(machine, [Action.NONE]) == [Machine(State.IDLE, 7), Machine(State.IDLE, 7)]
act = [Action.START, Action.NONE, Action.STOP, Action.START]
assert simulate(machine, act) == [Machine(State.IDLE, 7), Machine(State.RUNNING, 6), Machine(State.RUNNING, 5), Machine(State.IDLE, 5), Machine(State.RUNNING, 4)]
