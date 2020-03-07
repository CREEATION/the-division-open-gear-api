from models.brand import Brand
from models.slots import Slots
import database

database.init_db()

brands = [
Brand('5.11 tactical',
               "+5% Protection from elites",
               "+10% Extra Incoming Healing",
               "+10% Weapon Handling",
               [Slots.backpack,Slots.vest,Slots.gloves]),
Brand('Airaldi Holdings',
               "+10.0% Accuracy",
               "+10.0% Headshot Damage",
               "+10.0% Marksman Rifle Damage",
               [Slots.backpack,Slots.holster,Slots.gloves]),
Brand('Alps Summit Armament',
               "+10.0% Cooldown Reduction",
               "+5.0% Skill Power",
               "+15% Hive Skill Power",
               [Slots.backpack,Slots.holster,Slots.gloves]),
Brand('Badger Tuff',
               "+7.0% Damage to Elites",
               "+15.0% Armor % on Kill",
               "+15% Chem Launcher Skill Power",
               [Slots.backpack,Slots.mask,Slots.gloves]),
Brand('China Light Industries Coporation',
               "+10.0% Explosive Damage",
               "+10.0% Shotgun Damage",
               "+10.0% Cooldown Reduction",
               [Slots.kneepads,Slots.mask,Slots.gloves]),
Brand('Douglas & Harding',
               "+5.0% Accuracy",
               "+10.0% Critical Hit Damage",
               "+7.0% Critical Hit Chance",
               [Slots.kneepads,Slots.mask,Slots.holster]),
Brand('Fenris Group AB',
               "+10.0% Assault Rifle Damage",
               "+10% Protection from Elites",
               "+20.0% Health on Kill",
               [Slots.vest,Slots.kneepads,Slots.holster]),
Brand('Gila Guard',
               "+5.0% Total Armor",
               "+20.0% Hazard Protection",
               "+15% Pulse Skill Power",
               [Slots.vest,Slots.kneepads,Slots.holster,Slots.mask,Slots.backpack,Slots.gloves]),
Brand('Murakami Industries',
               "+8.0% Health",
               "+10.0% Hazard Protection",
               "+15% Firefly Skill Power",
               [Slots.vest,Slots.kneepads,Slots.holster,Slots.mask,Slots.backpack,Slots.gloves]),
Brand('Overlord Armaments',
               "+10.0% Rifle Damage",
               "+7.5% Total Armor",
               "+7.0% Damage to Elites",
               [Slots.vest,Slots.gloves,Slots.kneepads]),
Brand('Petrov Defense Group',
               "+10.0% LMG Damage",
               "+15.0% Turret Skill Power",
               "+10.0% Cooldown Reduction",
               [Slots.backpack,Slots.vest,Slots.holster]),
Brand('Providence Defense',
               "+10.0% Skill Power",
               "+8.0% Health",
               "+5.0% Weapon Damage",
               [Slots.vest,Slots.kneepads,Slots.holster,Slots.mask,Slots.backpack,Slots.gloves]),
Brand('Richter & Kaiser GmbH',
               "+10.0 Hazard Protection",
               "+20% Pistol Damage",
               "+15% Shield Skill Power",
               [Slots.mask,Slots.backpack,Slots.holster]),
Brand('Sokolov Concern',
               "+10.0% SMG Damage",
               "+8.0% Critical Hit Damage",
               "+15% Seeker Skill Power",
               [Slots.mask,Slots.vest,Slots.kneepads]),
Brand('Wyvern Wear',
               "+7.0% Critical Hit Damage",
               "+15% Drone Skill Power",
               "+10.0% Critical Hit Chance",
               [Slots.mask,Slots.backpack,Slots.kneepads,Slots.holster]),
Brand('Yaahl Gear',
               "+10.0% Weapon Handling",
               "+8.0% Hazard Protection",
               "+5.0% Weapon Damage",
               [Slots.mask,Slots.vest,Slots.gloves]),
Brand('Golan Gear Ltd(PTS 3.0)',
               "+10.0% Hazard Protection",
               "+10% Protection from Elites",
               "+8.0% Total Armor",
               [Slots.vest,Slots.kneepads,Slots.holster,Slots.mask,Slots.backpack,Slots.gloves]),


]
for brand in brands:
    database.db_session.add(brand)

database.db_session.commit()




class Slot:


    def __init__(self):
        self.name = ''
        self.talents = []
        self.attributes = []


class Talent:

    def __init__(self):
        self.name = ''
        self.type = TalentType()
        self.slots = []
        self.description = ''
        self.requirements = []

class TalentType:

    def __init__(self):
        self.type = ''
        self.color = ''
        self.active = True


class Attribute:


    def __init__(self):
        self.name = ''
        self.type = ''
        self.slots = []

mask = Slot()
mask.name = 'mask'
backpack = Slot()
backpack.name = 'backpack'
vest = Slot()
vest.name = 'vest'
gloves = Slot()
gloves.name = 'gloves'
holster = Slot()
holster.name = 'holster'
kneepads = Slot()
kneepads.name = 'kneepads'


five_11 = Brand()
five_11.name = "5.11 Tactical"
five_11.set_bonus_1 = "+5% Protection From Elites"
five_11.set_bonus_2 = "+10% Incoming Healing"
five_11.set_bonus_3 = "+10% Weapon Handling"
five_11.slots = [backpack,vest,gloves]