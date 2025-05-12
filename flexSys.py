import pymysql
from urllib.request import urlopen
from PySide6.QtWidgets import QFileDialog, QMessageBox
import logging
import urllib.request
from database import DatabaseHandler
from enum import Enum, unique


# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@unique
class ThreatLevel(Enum):
    """Уровни угроз с аннотациями и описаниями"""
    LOW = (0, "Низкий уровень угрозы")
    MEDIUM = (1, "Средний уровень угрозы")
    HIGH = (2, "Высокий уровень угрозы")
    CRITICAL = (3, "Критический уровень угрозы")

    def __init__(self, id: int, description: str):
        self.id = id
        self.description = description


class ThreatObject:
    """Класс для представления объекта угрозы"""

    def __init__(self):
        self.level: ThreatLevel = ThreatLevel.LOW
        self.type: str = ''
        self.name: str = ''
        self.id: int = 0
        self.comment: str = ''
        self.data: str = ''


class FlexSystem(DatabaseHandler):
    def __init__(self, config, window):
        self.config = config
        self.window = window
        self.current_threat = ThreatObject()


    def listen_db(self) -> None:
        """Мониторинг изменений в базе данных"""
        try:
            with self.connection.cursor() as cursor:
                # Пример запроса для мониторинга
                cursor.execute("SELECT * FROM threats ORDER BY id DESC LIMIT 1")
                result = cursor.fetchone()
                if result:
                    self._process_threat_data(result)
        except pymysql.Error as e:
            logger.error(f"Database error: {e}")
            QMessageBox.critical(self.window, "Ошибка", f"Ошибка БД: {e}")

    def _process_threat_data(self, data: dict) -> None:
        """Обработка данных об угрозе"""
        self.current_threat.id = data.get('id', 0)
        self.current_threat.level = ThreatLevel(data.get('level', 0))
        self.current_threat.type = data.get('type', '')
        self.current_threat.name = data.get('name', '')
        self.current_threat.comment = data.get('comment', '')
        self.current_threat.data = data.get('data', '')

        logger.info(f"Processed threat: {self.current_threat.name}")





