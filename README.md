# Microservice for logging information

Logging Service: You can receive requests from another micro-service
or third-party tools such as HTTP postman request software.

The purpose is to store data on transactions carried out in applications

**Requirements:**
* MongoDB installed. I recommend: https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04-pt

**Install service:**
```
mkvirtualenv loggingpy
workon loggingpy
pip install -r requirements.txt
```

**Run service:**
```
cd audit_service
./startup.sh
```
Note: you can config host and port at main_logger.py


**Implements on your project:**
```python

    def create_log(self, message, kind, trace, id_user):
        try: 
            URL = 'http://0.0.0.0:5005/api/v1.0/taskLogger'
            PARAMS = { 
                "message": message, 
                "kind": kind, 
                "trace": trace, 
                "id_user": id_user 
            }
            result = requests.put(
                url=URL, json=PARAMS
            )
            self.assertEqual(result.status_code, 200)
        except AssertionError:
            logging.warning("Logging service down")

```
 And use, for example:

 ```python

    self.create_log(
        f'User data successfuly saved. {id_user}, {user_name}, {email}', 
        'INFO', '', self._id_user
    )

    # or ...

    self.create_log(
        ex.args[0], 
        'ERROR', traceback.format_exc(), 
        self._id_user
    )
 ```
