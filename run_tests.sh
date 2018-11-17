python ./manage.py makemigrations --settings "test_settings"
python ./manage.py migrate --settings "test_settings"
python ./manage.py test --settings "test_settings"