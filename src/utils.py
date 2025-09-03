import json
import dotenv
import logging

dotenv.load_dotenv()


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(readfile):
    try:
        with open(readfile, encoding="utf-8") as f:
            text = f.read().replace("\n", "")
            operations = json.loads(text)
            logger.info(f"Файл {readfile} успешно прочитан и распакован")
            return operations
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("При чтении файла возникла ошибка")
        return []
