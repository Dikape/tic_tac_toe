# Tic-tac-toe game server
To run server on local machine, follow next step:
1. clone project
2. ```cd``` to <project_dir>
3. Copy docker-compose.sample.yml to docker-compose.yml and change if you need.
4. run command: ```docker-compose up --build -d```
5. Assume your project has name 'tic_tac_toe', then run command: ```docker exec -it tictactoe_web_1 sh```
6. run command: ```flask db upgrade```
7. run command: ```exit```
### Maybe it will not work, because I can't check it with my too bad internet