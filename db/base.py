import sqlite3
from pathlib import Path


class Database:

    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "database1.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS anime_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                introduction_text TEXT
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS animes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                picture TEXT,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES dish_categories(id)
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO anime_categories (name, introduction_text)
                VALUES  ('Боевик', 'Вот самые популярные аниме-боевики'),
                        ('Драмы', 'Вот самые популярные аниме-драмы'),
                        ('Романтика', 'Вот самые популярные аниме-романтика')
            """
        )
        self.cursor.execute(
            """
            INSERT INTO animes (name, description, picture, category_id)  
                VALUES ('Код-Гиас', 'Пример описания', 'gias.jpeg', '1'),
                ('Ван-Пис', 'Пример описания', 'vanpis.jpeg', '1'),
                ('Этот глупый свин не понимает мечту девочки-зайки', 'Пример описания', 'svin,jpeg', '3'),
                ('Хоримия', 'Пример описания', 'horimiya.jpeg', '3'),
                ('Форма голоса', 'Пример описания', 'voice.jpeg','2'),
                ('Хочу съесть твою поджелудочную железу', 'Пример описания', 'want.jpeg', '2')
            """
        )
        self.db.commit()

    def get_category_by_name(self, name: str):
        self.cursor.execute(
            "SELECT * FROM anime_categories WHERE name = :catName",
            {"catName": name},
        )
        return self.cursor.fetchone()

    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM animes")
        return self.cursor.fetchall()

    def get_dishes_by_category(self, category_id: int):
        self.cursor.execute(
            "SELECT * FROM animes WHERE category_id = :categoryId",
            {"categoryId": category_id},
        )
        return self.cursor.fetchall()

    def get_dishes_by_cat_name(self, cat_name: str):
        self.cursor.execute(
            """
            SELECT d.* , dc.name FROM animes AS d
            JOIN anime_categories AS dc ON d.category_id = dc.id
            WHERE dc.name = :catName
            """,
            {"catName": cat_name},
        )
        return self.cursor.fetchall()



if __name__ == "__main__":
    db = Database()
    db.create_tables()
    #db.populate_tables()