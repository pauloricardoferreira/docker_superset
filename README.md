Excluir a pasta node_modules do diretório superset-websocket assim que o container super pela primeira vez

comando antes de iniciar

criar as redes: superset e postgres-superset
criar os volumes superset e postgres-superset

docker container exec -ti ID_DO_CONTAINER /bin/bash

    command: 
      - /bin/bash
      - -c
      - |
          #atualizada o banco interno
          superset db upgrade &
          # cria usuário admin
          superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin
          #iniciar o superset
          superset init