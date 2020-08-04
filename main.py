from predictor import predictor, checker
import os
import time

def main(model='NN'):

    # use Riot Live Client to check if a game is being played
    time_sleep = checker()

    if not time_sleep:
        return

    open('lock.txt', 'x').close()

    time.sleep(time_sleep)

    prediction10 = predictor(10, model)
    print(prediction10)

    time.sleep(10)
    # time.sleep(300)
    prediction15 = predictor(15, model)
    print(prediction15)

    os.remove('lock.txt')


if __name__ == "__main__":

    if not os.path.exists('lock.txt'):
        main()