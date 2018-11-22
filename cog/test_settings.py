from cog.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
standard_packages = ['django', 'rest_framework']
test_packages = []
for package in INSTALLED_APPS:
    standard_package = False
    for standard in standard_packages:
        if standard in package:
            standard_package = True
    if not standard_package:
        test_packages.append(package)

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package={}'.format(','.join(test_packages)),
    '--with-doctest',
    '--cover-min-percentage=80'
]
