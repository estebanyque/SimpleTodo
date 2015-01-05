class Task:

    """
    Task should

    to create get the next parameters
    id: autoincrement by sql engine
    date: default current date
    time: default empty NOT IMPLEMENTED
    task: default Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    alarm: default no
    status: pending|overdue|completed

    to list get the next parameters
    all
    specific date
    specific time
    today's tasks (DEFAULT)'

    pending|completed|overdue|all

    SQLite file created with table
    task(id int primary key autoincrement, date date, desc text, alarm text)
    """
    from datetime import date
    import sqlite3

    DEFAULT_DATE = date.today()
    DEFAULT_DESC = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
    DEFAULT_ALARM = "N"

    task_db = sqlite3.connect("db/tasks.db")
    db = task_db.cursor()

    def __init__(self, task_id=None):
        print("***", task_id)
        if (task_id is not None):
            t = self.db.execute(
                "select id as 'unique_id', date as 'date', desc as 'desc',\
                alarm as 'alarm' from task where id = ?",
                task_id
                )
            print(("***", t.fetchone()[0]))
            self.task = {
                'unique_id': t.fetchone()['unique_id'],
                'date': t.fetchone()['date'],
                'desc': t.fetchone()['desc'],
                'alarm': t.fetchone()['alarm'],
                }
        else:
            self.task = {
                'date': self.DEFAULT_DATE,
                'desc': self.DEFAULT_DESC,
                'alarm': self.DEFAULT_ALARM,
                }

    def set_unique_id(self, unique_id):
        self.task['unique_id'] = unique_id

    def set_date(self, date):
        self.task['date'] = date

    def set_desc(self, desc):
        self.task['desc'] = desc

    def set_alarm(self, alarm):
        self.task['alarm'] = alarm

    def save_task(self):
        self.db.execute(
            "insert into task(date, desc, alarm) values (?,?,?)",
            (self.get_date(), self.get_desc(), self.get_alarm()))
        self.task_db.commit()

        last_id = self.db.execute("select last_insert_rowid()")
        last_id.fetchone()

        return self.get_task(last_id)

    def get_task(self, unique_id):
        self.db.execute("select from task where id = ?", unique_id)
        Task()

    def get_unique_id(self):
        return self.task['unique_id']

    def get_date(self):
        return str(self.task['date'])

    def get_desc(self):
        return self.task['desc']

    def get_alarm(self):
        return self.task['alarm']


