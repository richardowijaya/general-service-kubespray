1) default project structure
parent
--[configs]
--[controllers]
--[cruds]
--[database]
--[models]
--[repositories]
--[schemas] 
--main.py
--env
--alembic.ini

2) make sure to install alembic then run alembic init alembic to generate the migration tools
New project structure
--[controllers]
--[cruds]
--[database]
--[models]
--[schemas]
--[alembic] 
--main.py

upgrade database migration : alembic upgrade head --> execution the funtion to migrate the models to table
creation revision : alembic revision -m "nama table" --> to create new function to migrate the new models to table