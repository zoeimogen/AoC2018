def runprogram(program):
    state = [0, 0, 0, 0, 0, 0]
    ip = 0

    while True:
        state[program[ip][1]] = ip
        program[ip][0](state, program[ip][2:])
        ip = state[program[ip][1]] + 1
        if ip == 28:
            yield state
