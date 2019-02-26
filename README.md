# TIES4911 Task 7

Create apikey.txt file with keys to services.

For Google services get the json authentication file from the Cloud Console and add it to the environment path
```shell
$ export GOOGLE_APPLICATION_CREDENTIALS=[authentication json path]
```

## Install requirements
```shell
$ pipenv install
```

## Run server
```shell
$ FLASK_APP=webapp.py pipenv run flask run
```


