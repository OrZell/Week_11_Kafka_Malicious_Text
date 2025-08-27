from Manager_Fetching import Manager_Fetching
import time

manager = Manager_Fetching()

def run():
    while True:
        manager.run()
        time.sleep(60)

if __name__ == '__main__':
    run()