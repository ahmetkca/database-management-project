# database-management-project



> :warning: You must have installed docker (version 20.10.10, build b485636), docker-compose (version v2.1.1) and git (version 2.34) on your machine. (https://docs.docker.com/)
 
> if you are on windows10 it is better if you keep Docker Desktop open.

> if you are on ubuntu 20.04 you have to run the script file with sudo otherwise docker and docker-compose will not work

> If this is first time you are cloning this repo and running the project you need to run populate_database.sh and create_database_views.sh shell scripts in order to populate database with data and create the views.

> run these commands one by one on your terminal (linux environment wsl2 or bash).

```bash
~$ git clone https://github.com/ahmetkca/database-management-project.git
~$ cd database-management-project
~$ chmod +x ./run-clean.sh ./populate_database.sh ./create_database_views.sh
~$ ./run-clean.sh               # if on ubuntu 20.04 run with sudo
# once you execute the above command make sure all the services are running and db is healthy
~$ docker-compose ps
# this is what the output should look like if everything is working fine.
NAME                COMMAND                  SERVICE             STATUS              PORTS
backend             "/docker-entrypoint.…"   backend             running             0.0.0.0:8000->8000/tcp
db                  "docker-entrypoint.s…"   db                  running (healthy)   0.0.0.0:5432->5432/tcp
frontend            "docker-entrypoint.s…"   frontend            running             0.0.0.0:3000->3000/tcp
~$ ./populate_database.sh       # if on ubuntu 20.04 run with sudo
# this is the output for above command
Populating  Product_Type Table...
INSERT 0 6
Product_Type table successfully populated.
Populating  Product_Specification Table...
INSERT 0 63
Product_Specification table successfully populated.
Populating  Product Table...
INSERT 0 23
Product table successfully populated.
Populating  Store Table...
INSERT 0 6
Store table successfully populated.
Populating  Customer Table...
INSERT 0 6
Customer table successfully populated.
Populating  Employee Table...
INSERT 0 18
Employee table successfully populated.
Populating  Inventory Table...
INSERT 0 6
Inventory table successfully populated.
Populating  Storage_Rack Table...
INSERT 0 138
Storage_Rack table successfully populated.
Populating  Order Table...
INSERT 0 6
Order table successfully populated.
Populating  Transaction Table...
INSERT 0 9
Transaction table successfully populated.
Populating  Fired_Employee Table...
INSERT 0 7
Fired_Employee table successfully populated.
 setval
--------
     23
(1 row)

 setval
--------
      6
(1 row)
~$ ./create_database_views.sh   # if on ubuntu 20.04 run with sudo
# this is the output for above command
 ... Create Views ...
CREATE VIEW
View1 has been successfully created
CREATE VIEW
View2 has been successfully created
CREATE VIEW
View3 has been successfully created
CREATE VIEW
View4 has been successfully created
CREATE VIEW
View5 has been successfully created
CREATE VIEW
View8 has been successfully created
CREATE VIEW
View9 has been successfully created
CREATE VIEW
View10 has been successfully created
CREATE VIEW
View11 has been successfully created
CREATE VIEW
View12 has been successfully created
CREATE VIEW
View13 has been successfully created
```

```
Backend (Django Rest Framework) runs on port 8000
Frontend (Svelte) runs on port 3000
Database (PostgreSQL) runs on port 5432
```

> locate to http://localhost:3000 to interact with frontend
