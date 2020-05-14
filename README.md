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
**-- Versão inicial apenas simula a busca e adição para fins de teste da logging. Terei outro serviço para usuários**.  


**Instalação:**


mkvirtaulenv logging_service
pip install -r requirements.txt


**Para Executar:**

python user_service/main_user.py
python audit_service/main_logger.py


**Utilização:**


Importe o arquivo LoggingPy.postman_collection.json no Postman e execute os endpoints que preferir.

