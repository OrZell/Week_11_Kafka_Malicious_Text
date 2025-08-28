from maneger_persister import ManegerPersister


app = ManegerPersister()

def main():
    while True:
        app.run_persister_service()


if __name__ == '__main__':
    main()