from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from application import app, db

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

if __name__ == '__main__':
    manager.run()
