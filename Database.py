from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
import os


if os.path.exists("Database.db"):
    os.remove("Database.db")

engine = create_engine("sqlite:///Database.db")
metadata = MetaData()

Customer_table = Table('Customer', metadata,
               Column('Customer_ID', Integer, primary_key=True, unique=True, nullable=False),
               Column('First_Name', String, nullable=False),
               Column('Second_Name', String, nullable=False),
               Column('Email', String, nullable=False),
               Column('Phone_Number',String,unique=True),
               Column('Password', String, nullable=False)
             )

Burber_table = Table('Burber', metadata,
               Column('Burber_ID', Integer, primary_key=True, unique=True, nullable=False),
               Column('First_Name', String, nullable=False),
               Column('Second_Name', String, nullable=False),
               Column('Email', String, nullable=False),
               Column('Phone_Number',String,unique=True)
			 )
			 
Schedule_table = Table('Schedule', metadata,
               Column('Customer_ID', Integer, nullable=False),
               Column('Burber_ID', Integer, nullable=False),
               Column('Time', Date, nullable=False),
               Column('Haircut_ID', Integer, nullable=False)
			 )

Haircut_table = Table('Haircut', metadata,
               Column('Haircut_ID', Integer, primary_key=True, nullable=False),
               Column('Name', String, nullable=False),
               Column('Work_Duration', Date, nullable=False)
			 )

Price_table = Table('Price', metadata,
               Column('Haircut_ID', Integer, primary_key=True, nullable=False),
               Column('Price', Integer, nullable=False)
			 )

Photo_table = Table('Photo', metadata,
               Column('Haircut_ID', Integer, primary_key=True, nullable=False),
               Column('Photo_ID', Integer, nullable=False, unique=True),
			 )			 
