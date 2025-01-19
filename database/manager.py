from sqlalchemy import Insert, Select, Update, Delete, create_engine, Result
from sqlalchemy.orm import sessionmaker
from . import models

class Database:
    _connection_string = "sqlitecloud://cgmxzylvhz.g2.sqlite.cloud:8860/mikeSm_db?apikey=C2GK3JpEIbGzeOt5EpcQRFWNculSMM0rc7wbew14AQk"

    def __init__(self):
        self._engine = create_engine(self._connection_string)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()
        self.struct()


    def struct(self):
        # models.Base.metadata.drop_all(self._engine)
        models.Base.metadata.create_all(self._engine)

    def execute(self, query: Insert | Select | Update | Delete) -> Result:
        return self._session.execute(query)
    
    def close(self):
        self._session.close_all()

    def get_session(self):
        return self._session