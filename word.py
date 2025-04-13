import sqlite3

class Word:
    db_name = 'word.db'
    
    def __init__(self):
        self.db_exec('''
            create table if not exists word (
                word_id integer primary key autoincrement,
                eng text unique not null,
                amh text not null        
            )
        ''')

    def add_word(self, eng, amh):
        return self.db_exec(f'''insert into word (eng,amh) values ('{eng}','{amh}')''')

    def update_word(self, word_id, eng, amh):
        return self.db_exec(f'''update word set eng='{eng}', amh='{amh}' where word_id='{word_id}' ''')

    def find_amh(self, eng):
        return self.db_query(f'''select amh from word where eng='{eng}' ''')

    def find_eng(self, amh):
        return self.db_query(f'''select eng from word where amh='{amh}' ''')

    def get_words(self):
        return self.db_query(f'''select * from word''')

    def get_word(self, word_id):
        return self.db_query(f'''select * from word where word_id='{word_id}' ''')

    def delete_word(self, word_id):
        return self.db_exec(f'''delete from word where word_id='{word_id}' ''')

    def clear_word(self):
        return self.db_exec(f'''delete from word''')

    def error(self, e):
        print(f'\n\n\n{e}\n\n\n')

    def db_exec(self, sql):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
    
        try:
            cursor.execute(sql)
            conn.commit()
            return True
        except Exception as e:
            self.error(e)
        finally:
            cursor.close()
            conn.close()
        
        return False

    def db_query(self, sql):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
    
        try:
            cursor.execute(sql)
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        except Exception as e:
            self.error(e)
        finally:
            cursor.close()
            conn.close()
        
        return False
