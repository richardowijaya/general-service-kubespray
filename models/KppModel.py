from sqlalchemy import Boolean, String, Integer, Column
from sqlalchemy.orm import relationship
from configs.database import Base,engine

class MtrKpp(Base):
    