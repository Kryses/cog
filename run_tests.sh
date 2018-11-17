/usr/bin/python3 ./manage.py makemigrations --settings "test_settings"
/usr/bin/python3 ./manage.py migrate --settings "test_settings"
/usr/bin/python3 ./manage.py test --settings "test_settings"