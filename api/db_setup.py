import sqlite3
from models.task import *
from models.employee import *

sqlite_file = "kira.db"

def init():
    assert sqlite_file is not None
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title STRING NOT NULL, 
    description STRING, priority STRING, status STRING, creator INTEGER, assigned STRING, completionTime INTEGER, 
    blocksTasks STRING, blockedBy STRING)""")

    c.execute("""CREATE TABLE IF NOT EXISTS employee (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name STRING NOT NULL, assigned STRING, created STRING) """)

    #commit the changes to db			
    conn.commit()
    close()


def close():
    conn = get_db()
    #close the connection
    conn.close()

def get_db():
    conn = sqlite3.connect(sqlite_file)
    return conn

def createTask(t):
    conn = get_db()
    curs = conn.cursor()
    task = t
    if not task.assigned_to:
        assigned_to = ""
    else:
        assigned_to = ((" ").join(str(v) for v in task.assigned_to))
    if not task.blocked_by:
        blocked_by = ""
    else:
        blocked_by = ((" ").join(str(v) for v in task.blocked_by))
    if not task.blocks_tasks:
        blocks_tasks = ""
    else:
        blocks_tasks = ((" ").join(str(v) for v in task.blocks_tasks))
    curs.execute("INSERT INTO tasks (title, description, priority, status, creator, assigned, completionTime, blocksTasks, blockedBy) VALUES (?,?,?,?,?,?,?,?,?);", 
    (task.title, task.description, task.priority, task.status, task.creator, assigned_to, task.completion_time, blocks_tasks, blocked_by))
    
    conn.commit()

    resp = curs.execute("SELECT * FROM task WHERE id=last_insert_rowid()").fetchall()
    print(resp)
    return resp

def getTasks():
    conn = get_db()
    curs = conn.cursor()
    # curs.execute()
    rows = curs.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    print(rows)

def createEmployee(e):
    conn = get_db()
    curs = conn.cursor()
    # employee = Employee(**e)
    employee = e
    if not employee.tasks_assigned:
        assigned = ""
    else:
        assigned = ((" ").join(str(v) for v in employee.tasks_assigned))
    if not employee.tasks_created:
        created = ""
    else:
        created = ((" ").join(str(v) for v in employee.tasks_created))

    curs.execute("INSERT INTO employee (name, assigned, created) VALUES (?,?,?)", (employee.name, assigned, created))

    conn.commit()

    resp = curs.execute("SELECT * FROM employee WHERE id=last_insert_rowid()").fetchall()
    print(resp)
    return resp

def getEmployees():
    conn = get_db()
    curs = conn.cursor()
    rows = curs.execute("SELECT * FROM employee ORDER BY id").fetchall()
    print(rows)



task1 = {'task_id': '1', 'title': 'Task 1', 'description': 'A description', 'priority': 'MED', 'status': 'In Progress', 'creator': '1', 'assigned_to': [1,2], 'completion_time': 4, 'blocked_by': [2,4]}
employee1 = {'employee_id': '1', 'name': 'John Smith'}

if __name__ == "__main__":
    # init()
    # createTask(task1)
    getTasks()
    # createEmployee(Employee(**employee1))
    getEmployees()
    close()