import logging

import gui as gui


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/process.log"),
        logging.StreamHandler()
    ],
    encoding="utf-8"
)

if __name__ == "__main__":
    gui.execute()