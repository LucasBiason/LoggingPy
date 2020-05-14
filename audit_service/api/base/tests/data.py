from datetime import datetime
 
TEST_DATA = [{ 
    "tableName": "tb_logInfo",
    "firstRec": {
        "ID_USER": 1,
        "DATE_OF": datetime.now().strftime('%m/%d/%Y %H:%M'),
        "MESSAGE": "Test log",
        "LEVEL": 'INFO',
        "TRACE": "Empty"
    }
}, { 
    "tableName": "tb_user",
    "firstRec": {
        "ID_USER": 1,
        "EMAIL": "biasonlucky10@gmail.com",
        "NAME": "Lucas Biason"
    }
}]