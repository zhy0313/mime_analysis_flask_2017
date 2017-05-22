from flask_script import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from app import create_app
from app.models import db

app = create_app('development')

migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print('Hello Flask!')


if __name__ == "__main__":
    manager.run()
