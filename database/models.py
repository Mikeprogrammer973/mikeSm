from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import String, Column, ForeignKey, Date, Integer, Boolean, Enum


class Base(DeclarativeBase):
    pass

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    notifications = Column(Boolean)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    code = Column(String)
    email = Column(String)
    users = relationship("User", back_populates='store')
    pallets = relationship("Pallet", back_populates='store')
    verifiable_equipments = relationship("VerifiableEquipment", back_populates='store')
    backups = relationship("Backup", back_populates="store")

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
    verification_logs = relationship("VerificationLog", back_populates="user")


class ColorGroup(Base):
    __tablename__ = "color_groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    pallets = relationship("Pallet", back_populates='color_group')

class ColorNumber(Base):
    __tablename__ = "color_numbers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(Integer, unique=True)
    pallets = relationship("Pallet", back_populates='color_number')

class Pallet(Base):
    __tablename__ = "pallets"

    color_group_id = Column(String, ForeignKey("color_groups.id"), primary_key=True)
    color_group = relationship("ColorGroup", back_populates="pallets")
    color_number_id = Column(String, ForeignKey("color_numbers.id"), primary_key=True)
    color_number = relationship("ColorNumber", back_populates="pallets")
    stock = Column(Integer)
    store_id = Column(Integer, ForeignKey("stores.id"), primary_key=True)
    store = relationship("Store", back_populates="pallets")

class VerifiableEquipment(Base):
    __tablename__ = "verifiable_equipments"

    name = Column(String, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.id"), primary_key=True)
    store = relationship("Store", back_populates="verifiable_equipments")
    verification_logs = relationship("VerificationLog", back_populates="verifiable_equipment")

class VerificationLog(Base):
    __tablename__ = "verification_logs"

    verified_at = Column(Date)
    exp_at = Column(Date)
    verifiable_equipment_id = Column(Integer, ForeignKey("verifiable_equipments.name"), primary_key=True)
    verifiable_equipment = relationship("VerifiableEquipment", back_populates="verification_logs")
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    user = relationship("User", back_populates="verification_logs")

class Backup(Base):
    __tablename__ = "backups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    generated_at = Column(Date)
    store_id = Column(Integer, ForeignKey("stores.id"))
    store = relationship("Store", back_populates="backups")