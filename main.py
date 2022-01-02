import stockfish, random

def main():
    import configparser

    config = configparser.ConfigParser()
    config.read('consts.ini')
    api_key = config['lichess']['API_KEY']
    stockfish = config['lichess']['STOCKFISH']

    bot = stockfish(stockfish, level=1, api_key=api_key)
    # bot = RandomBot(api_key=api_key)
    bot.run()


if __name__ == '__main__':
    main()

