from ManagerFetching import ManagerFetching
import time

manager = ManagerFetching()

def run():
    while True:
        manager.run()
        time.sleep(60)

if __name__ == '__main__':
    run()