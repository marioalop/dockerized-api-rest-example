import os
import time
from django.core.management import  ManagementUtility
from django.db import connections
from django.db.utils import OperationalError
import django
from datetime import datetime

APP = "anniversaries"
DATAFILE = "2019.txt"
print("START SETUP")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()


def database_connection():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        connected = False
    else:
        connected = True
    return connected


def create_admin():
    from django.contrib.auth.models import User
    name = os.environ.get("DJANGO_ADMIN_USER", "admin")
    passwd = os.environ.get("DJANGO_ADMIN_PASSWORD", "marioalop789!!!")
    mail = os.environ.get("DJANGO_ADMIN_MAIL", "mario.lopez.dev@gmail.com")
    exists = User.objects.filter(username=name)
    if not exists:
        print("#########################################################\n"
              "CREATE ADMIN USER\n"
              "#########################################################")
        User.objects.create_superuser(name, mail, passwd)


def initial_data():
    from anniversaries.models import Efemeride
    import re
    import datetime
    if Efemeride.objects.count() == 0:
        regex = r"(?P<month>\d+)-(?P<day>\d+) (?P<quote>[0-9a-zA-Z _áéíóúü]+)"
        year = int(DATAFILE.replace(".txt", "").strip())
        print(year)
        anniversaries = []
        for line in open(DATAFILE).readlines():
            l = re.search(regex, line)
            data = l.groupdict()
            print(data)
            anniversaries.append(Efemeride(dia=datetime.datetime(year=year,
                                                                 month=int(data["month"]),
                                                                 day=int(data["day"]),
                                                                ),
                                            cita=data["quote"]))
        Efemeride.objects.bulk_create(anniversaries)


while not database_connection():
    print("Waiting for database connection...")
    time.sleep(5)


print("DATABASE CONNECTED!")
mkmigrations = ManagementUtility(["", "makemigrations"])
mkmigrations.execute()
appmigrations = ManagementUtility(["", "makemigrations", APP])
appmigrations.execute()
migrate = ManagementUtility(["", "migrate"])
migrate.execute()
migrate = ManagementUtility(["", "collectstatic", "--noinput"])
migrate.execute()
# initialdata = ManagementUtility(["", "loaddata", "initialdata"])
# initialdata.execute()
django.setup(set_prefix=False)
create_admin()
initial_data()
print("DONE!")

