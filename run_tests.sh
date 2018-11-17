/usr/bin/python3 ./manage.py makemigrations --settings "cog.test_settings"
/usr/bin/python3 ./manage.py migrate --settings "cog.test_settings"
/usr/bin/python3 ./manage.py test --settings "cog.test_settings"