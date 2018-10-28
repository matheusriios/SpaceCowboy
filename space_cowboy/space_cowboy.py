__all__ = ('main',)


from configs import CONFIG as config
from core.main import start



def main():

    start(config)


if __name__ == '__main__':
    main()
