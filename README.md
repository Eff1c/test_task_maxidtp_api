# test_task_maxidtp_api
This program was developed as a test task!
## Installation
1. Create venv `python3 -m venv env`
2. Its activate `source env/bin/activate`
3. Install requirements `pip install -r requirements.txt`
4. Set environment variables in .env file.
5. Create table
```
CREATE TABLE illia_orders (
    id UNIQUEIDENTIFIER PRIMARY KEY default NEWID(),
    sum FLOAT NOT NULL,
    name VARCHAR (255),
    created DATETIME
);
```

And if you want to run test server `flask run`