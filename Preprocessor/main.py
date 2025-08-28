from maneger_tweets import Maneger
import time

app = Maneger()

def main():
    while True:
        app.run()
        time.sleep(60)

if __name__ == '__main__':
    main()