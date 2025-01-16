import sqlalchemy
from sqlalchemy.orm import sessionmaker
from . import models

class Database:
    _connection_string = "sqlitecloud://cgmxzylvhz.g2.sqlite.cloud:8860/mikeSm_db?apikey=C2GK3JpEIbGzeOt5EpcQRFWNculSMM0rc7wbew14AQk"

    def __init__(self):
        self._engine = sqlalchemy.create_engine(self._connection_string)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()
        self.struct()


    def struct(self):
        models.Base.metadata.create_all(self._engine)

    def create_test_u(self):
        query = sqlalchemy.insert(models.Store).values(name="Betonel Lasalle", location="Lasalle", code="8483", manager=None)
        return self._session.execute(query)


    def get_session(self):
        return self._session