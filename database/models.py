from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import String, Column, ForeignKey, Date, Integer, Boolean, Enum


class Base(DeclarativeBase):
    pass

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    notifications = Column(Boolean)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    code = Column(String)
    email = Column(String)
    manager = Column(Integer, ForeignKey("users.id"))
    users = relationship("User", back_populates='store')
    pallets = relationship("Pallet", back_populates='store')
    v_equipments = relationship("VerifiableEquipment", back_populates='store')

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String)
    role = Column(Enum("user", "admin"))
    notifications = Column(Boolean)
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="users")


class ColorGroup(Base):
    __tablename__ = "color_groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

class ColorNumber(Base):
    __tablename__ = "color_numbers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Integer, unique=True)

class Pallet(Base):
    __tablename__ = "pallets"

    group = Column(String, ForeignKey("color_groups.id"), primary_key=True)
    number = Column(Integer, ForeignKey("color_numbers.id"),primary_key=True)
    stock = Column(Integer)
    store_id = Column(Integer, ForeignKey("stores.id"), primary_key=True)
    store = relationship("Store", back_populates="pallets")

class VerifiableEquipment(Base):
    __tablename__ = "v_equipments"

    name = Column(String, primary_key=True)
    last_verification_at = Column(Date, ForeignKey("verification_logs.id"))
    store_id = Column(Integer, ForeignKey("stores.id"), primary_key=True)
    store = relationship("Store", back_populates="v_equipments")
    logs = relationship("VerificationLog", back_populates="v_equipment")

class VerificationLog(Base):
    __tablename__ = "verification_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    verified_at = Column(Date)
    exp_at = Column(Date)
    v_equipment = relationship("VerifiableEquipment", back_populates="verification_logs")
    verified_by = Column(Integer, ForeignKey("users.id"))
