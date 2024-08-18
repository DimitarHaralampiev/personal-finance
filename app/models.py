import datetime

from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    budgets = relationship('Budget', back_populates='user')
    expenses = relationship('Expense', back_populates='user')


class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    category = Column(String, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates="expenses")


class Budget(Base):
    __tablename__ = 'budgets'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='budgets')
