from datetime import datetime
from datetime import timedelta
from time import sleep


def pomodoro_timer(work_time=1, break_time=5, total_rounds=4):
    for round in range(1, total_rounds + 1):
        next_break = datetime.now() + timedelta(minutes = work_time)
        start_message = f'Round {round} of {total_rounds}. Next break at {next_break: %X}!'
        break_message = f'Break time! Continue in {break_time} minutes.'
        if round == total_rounds:
            sleep(work_time * 60)
            print('Done')
        else:
            print(start_message)
            sleep(work_time * 60)
            print(break_message)
            sleep(break_time * 60)
            
if __name__ == "__main__":
    pomodoro_timer()

# TODO
# * make GUI of sorts to query input from the User
