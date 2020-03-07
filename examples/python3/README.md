Plenty of code to clean up still. Still migrating stuff over.
The idea is to have a developer API for creating and automating database creation, but also have the public facing api that developers can take advantage of to actually create apps, websites, wigits, etc.

The public facing api strives to create purely-pythonic classes from the SQL database, so that everything behaves as one would expect. It also gives the developer access to a pandas dataframe containing the relevant data, as most people are familiar with pandas and may want to work with it that way.

The data api will create a sqllite database with all the relevant tables, so that developers can, if they want, create their own implementations.

requirements:
sqlalchemy
sqlite3
pandas
