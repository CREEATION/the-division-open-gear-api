from sqlalchemy import Column, Integer, String, DateTime,Boolean
from database import Base
import uuid
import datetime
import numpy as np
from models.slots import Slots

class Brand(Base):
    __tablename__ = 'Brand'
    id = Column(String(50), primary_key=True)
    name = Column(String(50), unique=True)
    set_bonus_1 = Column(String(100), nullable= True)
    set_bonus_2 = Column(String(100), nullable= True)
    set_bonus_3 = Column(String(100), nullable= True)
    mask = Column(Boolean(False))
    backpack = Column(Boolean(False))
    vest = Column(Boolean(False))
    gloves = Column(Boolean(False))
    holster = Column(Boolean(False))
    kneepads = Column(Boolean(False))

    def __init__(self, name,
                 set_bonus_1,
                 set_bonus_2,
                 set_bonus_3,
                 slots):
        self.id = str(uuid.uuid4())
        self.name = name
        self.set_bonus_1 = set_bonus_1
        self.set_bonus_2 =  set_bonus_2
        self.set_bonus_3 = set_bonus_3
        self.make_slots(slots)

    def __repr__(self):
        return '<Brand %r>' % (self.name)

    def make_slots(self,slots):
        if Slots.mask in slots:
            self.mask = True
        else:
            self.mask = False
        if Slots.backpack in slots:
            self.backpack = True

        else:
            self.backpack = False

        if Slots.vest in slots:
            self.vest = True
        else:
            self.vest = False

        if Slots.gloves in slots:
            self.gloves = True
        else:
            self.gloves = False

        if Slots.holster in slots:
            self.holster = True
        else:
            self.holster = False

        if Slots.kneepads in slots:
            self.kneepads = True
        else:
            self.kneepads = False

