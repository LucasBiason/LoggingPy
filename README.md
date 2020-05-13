# Microservice for logging information


**Teremos 2 APIs:** 1 serviço para LOGGING e outro para manuseio de dados de usuário.


O objetivo é fazer com que cada API seja um micro-serviço. 

Cada micro-serviço será executado de forma independente pode receber requisições entre os mesmos 
ou requisições de terceiros.


**Definição de recursos:**


Serviço de Logging: Pode receber requisições de outro micro-serviço 
ou de ferramentas terceiras como por exemplo o software de requisições HTTP postman.


Serviço de User: Possui as mesmas características do serviço de logging 
e ainda pode fazer requisições para outros micro-serviços