class Task:

    """
    Task should

    to create get the next parameters
    id: on development, but should be a unique value
    date: default current date
    time: default empty
    task: default Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    alarm: default no
    statys: pending|overdue|completed

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
    import sqlite3 as lite

    now = date.today()

    task_db = None
    task_db = lite.connect("db/tasks.db")

    def __init__(self):
        self.task = {
            'unique_id': 1,
            'date': self.now,
            'desc': "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            'alarm': "N"}

    def set_unique_id(self, unique_id):
        self.task['unique_id'] = unique_id

    def set_date(self, date):
        self.task['date'] = date

    def set_desc(self, desc):
        self.task['desc'] = desc

    def set_alarm(self, alarm):
        self.task['alarm'] = alarm

    def save_task(self):
        # This method should store the task in a file or DB
        self.task_db.execute(
            "insert into task(date, desc, alarm) values (?,?,?)",
            (self.get_date(), self.get_desc(), self.get_alarm()))
        self.task_db.commit()

        #select last_insert_rowid to get the last record id

        #text = "|".join([
            #str(self.get_unique_id()),
            #self.get_date(),
            #self.get_desc(),
            #self.get_alarm(),
            #])

        #f = open("tasks.csv", "a")
        #f.write(text)
        #f.write("\n")
        #f.close()

        print("Saved!")

    def get_unique_id(self):
        return self.task['unique_id']

    def get_date(self):
        return str(self.task['date'])

    def get_desc(self):
        return self.task['desc']

    def get_alarm(self):
        return self.task['alarm']


