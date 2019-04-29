# flask
from flask import Flask
from sqlalchemy import null

app = Flask(__name__)

# tietokanta
from flask_sqlalchemy import SQLAlchemy

import os

if  os.environ.get("HEROKU"):
	app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lists.db"
	app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# sovelluksen toiminnallisuus
from application import views

from application.lists import models as list_models
from application.lists import views

from application.auth import models
from application.auth import views

from application.armydata import models as army_data_models
from application.armydata import views



# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

@app.cli.command()
def drop_db():
	db.drop_all()

@app.cli.command()
def init_db():
	db.create_all()

	armies_data = [
		('Beast Herds', 'BH', [
			('Characters', 40, None, [
				('Beast Lord', 215, None, 1, 1),
				('Beast Chieftain', 120, None, 1, 1),
				('Soothsayer', 155, None, 1, 1),
				('Minotaur Warlord', 490, None, 1, 1),
				('Minotaur Chieftain', 220, None, 1, 1),
				('Centaur Chieftain', 220, None, 1, 1),
			]),
			('Core', None, 20, [
				('Wildhorn Herd', 150, 10, 15, 50),
				('Mongrel Herd', 140, 8, 20, 50),
				('Mongrel Raiders', 95, 7, 10, 20),
			]),
			('Special', None, None, [
				('Feral Hounds', 80, 8, 5, 20),
				('Longhorn Herd', 155, 23, 10, 40),
				('Minotaurs', 235, 78, 3, 10),
				('Centaurs', 165, 25, 5, 15),
				('Riding Chariot', 110, 110, 1, 3),
				('Razortusk Herd', 100, 62, 1, 10),
				('Razortusk Chariot', 230, None, 1, 1),
				('Briar Beast', 120, None, 1, 1),
				('Gargoyles', 135, 17, 5, 10),
			]),
			('Terrors of the Wild', 40, None, [
				('Cyclops', 355, None, 1, 1),
				('Goratch', 475, None, 1, 1),
				('Jabberwock', 340, None, 1, 1),
				('Beast Giant', 300, None, 1, 1),
			]),
			('Ambush Predators', 60, None, [
			])
		]),
		('Daemon Legions', 'DL', [
			('Characters', 40, None, [
				('Harbringer of Father Chaos', 150, None, 1, 1),
				('Kuulima´s Deceiver', 355, None, 1, 1),
				('Maw of Akaan', 565, None, 1, 1),
				('Miser of Suglag', 670, None, 1, 1),
				('Courtesan of Cibaresh', 575, None, 1, 1),
				('Omen of Savar', 490, None, 1, 1),
				('Sentinel of Nukuja', 620, None, 1, 1),
				('Vanadra´s Scourge', 705, None, 1, 1),
			]),
			('Core', None, 25, [
				('Imps', 215, 15, 10, 25),
				('Succubi', 205, 18, 10, 25),
				('Lemures', 200, 27, 10, 25),
				('Myrmidons', 205, 20, 10, 30),
			]),
			('Special', None, None, [
				('Eidolons', 200, 37, 5, 10),
				('Hellhounds', 165, 16, 5, 15),
				('Threshing Engine', 160, None, 1, 1),
				('Titanslayer Chariot', 220, None, 1, 1),
				('Mageblight Gremlins', 170, 39, 2, 4),
				('Clawed Fiends', 275, 96, 3, 6),
				('Hoarders', 295, 118, 3, 6),
				('Sirens', 195, 28, 5, 15),
				('Blazing Glories', 280, None, 1, 1),
				('Hope Harvester', 285, None, 1, 1),
				('Brazen Beasts', 345, 103, 3, 6),
			]),
			('Aves', 35, None, [
				('Furies', 160, 13, 5, 15),
				('Veil Serpents', 265, 58, 3, 6),
				('Bloat Flies', 290, 100, 3, 6),
			]),
		]),
		('Dread Elves', 'DE', [
			('Characters', 40, None, [
				('Dread Prince', 240, None, 1, 1),
				('Captain', 155, None, 1, 1),
				('Cult Priest', 120, None, 1, 1),
				('Oracle', 170, None, 1, 1),
				('Assassin', 155, None, 1, 1),
			]),
			('Core', None, 25, [
				('Dread Legionnaires', 165, 13, 15, 50),
				('Corsairs', 160, 17, 10, 35),
				('Blades of Nabh', 200, 20, 10, 30),
				('Repeater Auxiliaries', 190, 17, 10, 30),
				('Dark Raiders', 160, 25, 5, 15),
			]),
			('Special', None, None, [
				('Tower Guard', 210, 25, 10, 30),
				('Dread Knigths', 245, 48, 5, 12),
				('Raptor Chariot', 195, None, 1, 1),
				('Harpies', 135, 14, 5, 15),
				('Dread Judges', 230, 24, 10, 30),
				('Dancers of Yema', 200, 22, 10, 20),
				('Medusa', 125, None, 1, 1),
				('Dark Acolytes', 235, 45, 5, 10),
				('Divine Altar', 385, None, 1, 1),
			]),
			('Raiders', 30, None, [
				('Raven Cloaks', 170, 33, 5, 10),
			]),
			('Destroyers', 15, None, [
				('Hunting Chariot', 210, None, 1, 1),
				('Dread Reaper', 180, None, 1, 1),

			]),
			('The Menagerie', 30, None, [
				('Kraken', 390, None, 1, 1),
				('Hydra', 440, None, 1, 1),
			]),
		]),
		('Dwarven Holds', 'DH', [
			('Characters', 40, None, [
				('King', 225, None, 1, 1),
				('Thane', 120, None, 1, 1),
				('Dragon Seeker', 210, None, 1, 1),
				('Runic Smith', 170, None, 1, 1),
				('Engineer', 125, None, 1, 1),
				('Anvil of Power', 185, None, 1, 1),
			]),
			('Core', None, 25, [
				('Clan Warriors', 120, 13, 10, 40),
				('Greybeards', 175, 20, 10, 30),
				('Clan Marksmen', 200, 19, 10, 25),
			]),
			('Special', None, None, [
				('Deep Watch', 310, 27, 15, 30),
				('King´s Guard', 310, 27, 15, 30),
				('Miners', 185, 16, 10, 20),
				('Rangers', 140, 16, 8, 20),
				('Seekers', 110, 21, 5, 25),
				('Vengeance Seeker', 130, None, 1, 1),
				('Hold Guardians', 280, 102, 3, 8),
				('Grudge Buster', 350, None, 1, 1),
			]),
			('Clans´ Thunder', 35, None, [
				('Forge Wardens', 220, 22, 10, 20),
				('Attack Copter', 175, 130, 1, 2),
				('Steam Bomber', 210, None, 1, 1),
			]),
			('Engines of War', 20, None, [
				('Dwarf Ballista', 105, None, 1, 1),
				('Flame Cannon', 150, None, 1, 1),
				('Catapult', 210, None, 1, 1),
				('Cannon', 255, None, 1, 1),
				('Organ Gun', 270, None, 1, 1),
			]),
		]),
		('Empire of Sonnsthal', 'EoS', [
			('Characters', 40, None, [
				('Marshal', 160, None, 1, 1),
				('Knight Commander', 200, None, 1, 1),
				('Prelate', 160, None, 1, 1),
				('Wizard', 125, None, 1, 1),
				('Artificier', 125, None, 1, 1),
				('Inquisitor', 130, None, 1, 1),
			]),
			('Core', None, 25, [
				('Heavy Infantry', 145, 10, 20, 50),
				('Light Infantry', 135, 13, 10, 20),
				('State Militia', 140, 10, 10, 25),
				('Electoral Cavalry', 155, 29, 5, 15),
			]),
			('Special', None, None, [
				('Imperial Guard', 180, 19, 15, 40),
				('Knights of the Sun Griffon', 290, 95, 3, 6),
				('Arcane Engine', 290, None, 1, 1),
			]),
			('Imperial Auxiliaries', 35, None, [
				('Imperial Rangers', 90, 12, 5, 10),
				('Reiters', 150, 29, 5, 10),
			]),
			('Imperial Armoury', 20, None, [
				('Mortar', 200, None, 1, 1),
				('Volley Gun', 200, None, 1, 1),
				('Imperial Rocketeer', 160, None, 1, 1),
				('Cannon', 250, None, 1, 1),
			]),
			('Sunna´s Fury', 30, None, [
				('Flagellants', 200, 18, 15, 30),
				('Steam Tank', 475, None, 1, 1),
			])
		]),
		('Highborn Elves', 'HE', [
			('Characters', 40, None, [
				('High Prince', 250, None, 1, 1),
				('Commander', 150, None, 1, 1),
				('Mage', 225, None, 1, 1),
			]),
			('Core', None, 25, [
				('Citizen Spears', 240, 16, 20, 50),
				('Highborn Lancers', 240, 40, 5, 15),
				('Citizen Archers', 170, 18, 10, 30),
				('Sea Guard', 300, 21, 15, 30),
				('Elein Reavers', 180, 25, 5, 10),
			]),
			('Special', None, None, [
				('Sword Masters', 130, 23, 5, 30),
				('Lion Guard', 225, 28, 10, 30),
				('Flame Wardens', 360, 28, 15, 40),
				('Knights of Ryma', 340, 54, 5, 12),
				('Reaver Chariot', 110, 100, 1, 4),
				('Lion Chariot', 215, None, 1, 1),
				('Giant Eagle', 100, 35, 1, 5),
			]),
			('Queen´s Bows', 30, None, [
				('Queen´s Guard', 140, 29, 5, 20),
				('Grey Watchers', 150, 26, 5, 10),
			]),
			('Naval Ordnance', 15, None, [
				('Sea Guard Reaper', 180, None, 1, 1),
				('Sky Sloop', 265, None, 1, 1),
			]),
			('Ancient Allies', 20, None, [
				('Pheonix', 375, None, 1, 1),
			]),
		]),
		('Infernal Dwarves', 'ID', [
			('Characters', 40, None, [
				('Overlord', 270, None, 1, 1),
				('Vizier', 125, None, 1, 1),
				('Chosen of Lugar', 220, None, 1, 1),
				('Wizard', 160, None, 1, 1),
				('Engineer', 180, None, 1, 1),
				('Taurukh Subjugator', 305, None, 1, 1),
				('Hobgoblin Chieftain', 70, None, 1, 1),
			]),
			('Core', None, 25, [
				('Infernal Warriors', 185, 12, 15, 40),
				('Citadel Guard', 180, 21, 10, 30),
				('Hobgoblins', 120, 7, 20, 50),
				('Orc Slaves', 115, 8, 20, 50),
			]),
			('Special', None, None, [
				('Immortals', 290, 28, 15, 30),
				('Taurukh', 150, 24, 5, 15),
				('Taurukh Anointed', 335, 105, 3, 4),
				('Hobgoblin Wolf Raiders', 130, 14, 5, 15),
			]),
			('Hail of the Gods', 30, None, [

			]),
			('Barrage', 20, None, [
				('Rocket Battery', 285, None, 1, 1),
				('Volcano Cannon', 150, None, 1, 1),
				('Titan Mortar', 300, None, 1, 1),
				('Hobgoblin Bolt Thrower', 95, None, 1, 1),
				('Gunnery Volley Gun', 150, None, 1, 1),
				('Grenade Launcher', 150, None, 1, 1),
				('Flamethrower', 130, None, 1, 1),
			]),
			('Bound and Binders', 35, None, [
				('Disciples of Lugar', 140, 25, 5, 25),
				('Kadim Titan', 575, None, 1, 1),
				('Kadim Incarnates', 335, 120, 3, 6),
				('Infernal Engine', 145, None, 1, 1),
				('Armoured Giant', 300, None, 1, 1),
			]),
		]),
		('Kingdom of Equitaine', 'KoE', [
			('Characters', 40, None, [
				('Duke', 170, None, 1, 1),
				('Paladin', 130, None, 1, 1),
				('Damsel', 120, None, 1, 1),
				('Castellan', 80, None, 1, 1),
			]),
			('Core', None, 25, [
				('Knights Aspirant', 230, 38, 5, 15),
				('Knights of the Realm', 260, 48, 6, 15),
				('Peasant Levy', 175, 7, 30, 60),
				('Peasant Bowmen', 170, 10, 15, 30),
			]),
			('Special', None, None, [
				('Knights of the Quest', 270, 50, 6, 15),
				('Knights Forlorn', 190, 25, 10, 40),
				('Knights of the Grail', 220, 84, 3, 9),
				('The Green Knigth', 375, None, 1, 1),
				('Yeoman Outsiders', 125, 14, 5, 15),
				('Brigands', 175, 13, 10, 15),
				('Peasant Crusaders', 150, 10, 20, 40),
				('Sacred Reliquary', 150, None, 1, 1),
				('Scorpion', 120, None, 1, 1),
				('Trebuchet', 280, None, 1, 1),
			]),
			('Airborne Gallantry', 40, None, [
				('Pegasus Knights', 340, 95, 3, 6),
			])
		]),
		('Ogre Khans', 'OK', [
			('Characters', 40, None, [
				('Great Khan', 310, None, 1, 1),
				('Khan', 190, None, 1, 1),
				('Shaman', 200, None, 1, 1),
				('Mammoth Hunter', 210, None, 1, 1),
			]),
			('Core', None, 25, [
				('Tribesmen', 155, 52, 3, 10),
				('Bruisers', 185, 76, 3, 9),
				('Scraplings', 115, 5, 20, 40),
			]),
			('Special', None, None, [
				('Mercenary Veterans', 245, 100, 3, 8),
				('Tusker Cavalry', 415, 130, 3, 5),
				('Yetis', 175, 65, 2, 6),
				('Scrapling Trappers', 80, 10, 5, 10),
				('Sabertooth Tigers', 80, 25, 1, 20),
				('Kin-Eater', 175, None, 1, 1),
			]),
			('Powder Keg', 45, None, [
				('Thunder Cannon', 320, None, 1, 1),
				('Scrapapult', 245, None, 1, 1),
				('Bombardiers', 185, None, 1, 1),
			]),
			('Chained Beasts', 30, None, [
				('Rock Aurpchs', 475, None, 1, 1),
				('Frost Mammoth', 405, None, 1, 1),
				('Slave Giant', 265, None, 1, 1),
			]),
		]),
		('Orcs and Goblins', 'OG', [
			('Characters', 40, None, [
				('Common Orc Warlord', 220, None, 1, 1),
				('Feral Orc Warlord', 260, None, 1, 1),
				('Iron Orc Warlord', 285, None, 1, 1),
				('Common Orc Chief', 120, None, 1, 1),
				('Feral Orc Chief', 140, None, 1, 1),
				('Iron Orc Chief', 160, None, 1, 1),
				('Common Orc Shaman', 155, None, 1, 1),
				('Feral Orc Shaman', 170, None, 1, 1),
				('Common Goblin King', 115, None, 1, 1),
				('Cave Goblin King', 115, None, 1, 1),
				('Forest Goblin King', 140, None, 1, 1),
				('Common Goblin Chief', 70, None, 1, 1),
				('Cave Goblin Chief', 70, None, 1, 1),
				('Forest Goblin Chief', 80, None, 1, 1),
				('Common Goblin Witch Doctor', 115, None, 1, 1),
				('Cave Goblin Witch Doctor', 150, None, 1, 1),
				('Forest Goblin Witch Doctor', 115, None, 1, 1),
			]),
			('Core', None, 25, [
				('Common Orcs', 175, 11, 20, 50),
				('Feral Orcs', 215, 13, 20, 50),
				('Common Orc ´Eadbashers', 230, 17, 15, 35),
				('Feral Orc ´Eadbashers', 290, 21, 15, 35),
				('Common Orc Boar Riders', 140, 20, 5, 15),
				('Feral Orc Boar Riders', 140, 20, 5, 15),
				('Common Goblins', 120, 6, 20, 60),
				('Cave Goblins', 120, 6, 20, 60),
				('Forest Goblins', 140, 7, 20, 60),
			]),
			('Special', None, None, [
				('Iron Orcs', 295, 27, 15, 20),
				('Orc Boar Chariot', 150, None, 1, 1),
				('Common Mounted ´Eadbashers', 175, 29, 5, 15),
				('Feral Mounted ´Eadbashers', 155, 25, 5, 15),
				('Common Goblin Riders', 120, 13, 5, 20),
				('Forest Goblin Riders', 120, 13, 5, 20),
				('Goblin Wolf Chariot', 125, 100, 1, 4),
				('Gnasher Dashers', 160, 25, 5, 5),
				('Gnasher Herd', 120, 12, 10, 40),
				('Gnasher Wrecking Team', 140, None, 1, 1),
				('Common Trolls', 180, 70, 3, 10),
				('Cave Trolls', 224, 84, 3, 10),
				('Bridge Trolls', 207, 79, 3, 10),
				('Grotlings', 90, 15, 3, 6),
				('Scrap Wagon', 85, None, 1, 1),
			]),
			('Death from Above', 15, None, [
				('Skewerer', 90, None, 1, 1),
				('Splatterer', 170, None, 1, 1),
				('Git Launcher', 185, None, 1, 1),
			]),
			('Big ´n Nasty', 30, None, [
				('Gargantula', 510, None, 1, 1),
				('Great Green Idol', 365, None, 1, 1),
				('Giant', 285, None, 1, 1),
			]),
		]),
		('Saurian Ancients', 'SA', [
			('Characters', 40, None, [
				('Saurian Warlord', 260, None, 1, 1),
				('Saurian Veteran', 180, None, 1, 1),
				('Cuatl Lord', 470, None, 1, 1),
				('Skink Captain', 80, None, 1, 1),
				('Sking Priest', 115, None, 1, 1),
				('Caiman Ancient', 210, None, 1, 1),
			]),
			('Core', None, 20, [
				('Saurian Warriors', 255, 21, 15, 35),
				('Skink Braves', 140, 8, 15, 40),
			]),
			('Special', None, None, [
				('Temple Guard', 365, 32, 15, 30),
				('Raptor Riders', 270, 50, 5, 12),
				('Caimans', 210, 80, 3, 7),
				('Snake Swarms', 130, 40, 2, 4),
			]),
			('Jungle Guerillas', 30, None, [
				('Skink Hunters', 110, 14, 5, 10),
				('Chameleons', 130, 20, 5, 15),
				('Weapon Beasts', 135, 130, 1, 2),
				('Pteradon Sentries', 190, 35, 3, 5),
				('Rhamphodon Riders', 215, 62, 3, 5),
			]),
			('Thunder Lizards', 35, None, [
				('Taurosaur', 450, None, 1, 1),
				('Stygiosaur', 305, None, 1, 1),
				('Thyroscutus', 320, None, 1, 1),
			]),
		]),
		('Sylvan Elves', 'SE', [
			('Characters', 40, None, [
				('Forest Prince', 215, None, 1, 1),
				('Chieftain', 145, None, 1, 1),
				('Druid', 140, None, 1, 1),
				('Treefather Ancient', 470, None, 1, 1),
				('Avatar of Nature', 630, None, 1, 1),
				('Dryad Ancient', 110, None, 1, 1),
				('Thicket Shepherd', 250, None, 1, 1),
			]),
			('Core', None, 25, [
				('Forest Guard', 175, 15, 15, 50),
				('Sylvan Archers', 265, 24, 10, 30),
				('Heath Riders', 180, 32, 5, 15),
				('Dryads', 150, 18, 8, 26),
			]),
			('Special', None, None, [
				('Forest Rangers', 210, 20, 10, 30),
				('Thicket Beasts', 385, 105, 4, 6),
				('Forest Eagle', 100, 35, 1, 5),
				('Blade Dancers', 230, 32, 7, 15),
				('Treefather', 450, None, 1, 1),
				('Wild Huntsmen', 300, 55, 5, 12),
				('Kestrel Knights', 310, 80, 3, 6),
			]),
			('Unseen Arrows', 30, None, [
				('Briar Maidens', 200, 35, 5, 10),
				('Sylvan Sentinels', 160, 55, 5, 10),
				('Pathfinders', 210, 50, 5, 10),
			]),
		]),
		('The Vermin Swarm', 'VS', [
			('Characters', 40, None, [
				('vermin Daemon', 820, None, 1, 1),
				('Tyrant', 160, None, 1, 1),
				('Chief', 110, None, 1, 1),
				('Magister', 200, None, 1, 1),
				('Rakachit Machinist', 170, None, 1, 1),
				('Sicarra Assassin', 280, None, 1, 1),
				('Plague Patriarch', 155, None, 1, 1),
			]),
			('Core', None, 25, [
				('Rats-at-Arms', 220, 7, 25, 60),
				('Vermin Guard', 250, 16, 20, 50),
				('Plague Brotherhood', 205, 10, 20, 50),
				('Slaves', 145, 4, 30, 60),
				('Footpads', 120, 9, 10, 30),
			]),
			('Special', None, None, [
				('Giant Rats', 80, 6, 10, 60),
				('Plague Disciples', 170, 17, 8, 15),
				('Vermin Hulks', 295, 75, 4, 12),
				('Rat Swarms', 90, 30, 2, 10),
				('Meat Grinder', 150, None, 1, 1),
				('Gutter Blades', 145, 25, 5, 10),
			]),
			('Tunnel Gunners', 30, None, [
				('Weapon Team', 150, None, 1, 1),
				('Jezailes', 110, 40, 3, 6),
				('Grenadiers', 185, 21, 8, 15),
				('Plague Catapult', 170, None, 1, 1),
				('Lightning Cannon', 265, None, 1, 1),
				('Dreadmill', 305, None, 1, 1),
			]),
			('Built and Bred', 30, None, [
				('Abomination', 375, None, 1, 1),
			]),
		]),
		('Undying Dynasties', 'UD', [
			('Characters', 40, None, [
				('Pharaoh', 295, None, 1, 1),
				('Nomarch', 140, None, 1, 1),
				('Death Cult Hierarch', 125, None, 1, 1),
				('Casket of Phatep', 240, None, 1, 1),
				('Tomb Harbringer', 180, None, 1, 1),
				('Tomb Architect', 160, None, 1, 1),
			]),
			('Core', None, 25, [
				('Skeletons', 150, 10, 20, 60),
				('Skeleton Archers', 120, 12, 10, 30),
				('Skeleton Cavalry', 190, 17, 10, 24),
				('Skeleton Scouts', 130, 16, 5, 10),
				('Skeleton Chariots', 290, 65, 3, 10),
			]),
			('Special', None, None, [
				('Necropolis Guard', 190, 25, 15, 40),
				('Tomb Cataphracts', 300, 90, 3, 6),
				('Shabtis', 210, 75, 3, 8),
				('Great Vultures', 155, 25, 3, 9),
				('Scarab Swarms', 140, 50, 2, 6),
			]),
			('Ancient Ordnance', 35, None, [
				('Shabti Archers', 200, 80, 3, 8),
				('Sand Stalkers', 260, 70, 3, 7),
				('Charnel Catapult', 200, None, 1, 1),
			]),
			('Entombed', 30, None, [
				('Sand Scorpion', 160, None, 1, 1),
			]),
			('Mason´s Menagerie', 35, None, [
				('Battle Sphinx', 480, None, 1, 1),
				('Dread Sphinx', 480, None, 1, 1),
				('Tomb Reapers', 340, 180, 2, 4),
				('Colossus', 420, None, 1, 1),
			]),
		]),
		('Vampire Covenant', 'VC', [
			('Characters', 40, None, [
				('Vampire Count', 330, None, 1, 1),
				('Vampire Courtier', 160, None, 1, 1),
				('Necromancer', 125, None, 1, 1),
				('Barrow King', 175, None, 1, 1),
				('Fell Wraith', 120, None, 1, 1),
				('Banshee', 165, None, 1, 1),
			]),
			('Core', None, 25, [
				('Zombies', 115, 5, 20, 80),
				('Skeletons', 150, 10, 20, 40),
				('Ghouls', 130, 17, 10, 40),
				('Bat Swarm', 105, 30, 2, 8),
			]),
			('Special', None, None, [
				('Dire Wolves', 80, 11, 5, 15),
				('Barrow Guard', 175, 22, 15, 40),
				('Barrow Knights', 170, 48, 5, 15),
				('Ghasts', 160, 95, 3, 10),
				('Great Bats', 90, 15, 2, 9),
				('Cadaver Wagon', 350, None, 1, 1),
				('Court of hte Damned', 310, None, 1, 1),
				('Altar of Undeath', 365, None, 1, 1),
				('Dark Coach', 430, None, 1, 1),
			]),
			('The Suffering', 20, None, [
				('Phantom Host', 160, 75, 2, 5),
				('Wraiths', 180, 40, 5, 10),
				('Spectral Hunters', 190, 38, 5, 10),
			]),
			('Swift Death', 30, None, [
				('Shrieking Horror', 490, None, 1, 1),
				('Vampire Knights', 240, 90, 3, 6),
				('Winged Reapers', 320, 180, 2, 2),
				('Varkolak', 335, None, 1, 1),
				('Vampire Spawn', 240, 80, 5, 10),
			]),
		]),
		('Warriors of the Dark Gods', 'WDK', [
			('Characters', 45, None, [
				('Exalted Herald', 850, None, 1, 1),
				('Chosen Lord', 295, None, 1, 1),
				('Doomlord', 360, None, 1, 1),
				('Sorcerer', 145, None, 1, 1),
				('Barbarian Chief', 115, None, 1, 1),
				('Feldrak Ancestor', 685, None, 1, 1),
			]),
			('Core', None, 20, [
				('Warriors', 210, 24, 10, 25),
				('Fallen', 150, 19, 5, 15),
				('Barbarians', 130, 7, 15, 40),
			]),
			('Special', None, None, [
				('Warrior Knights', 245, 44, 5, 10),
				('Warrior Chariot', 225, None, 1, 1),
				('Chosen', 265, 60, 5, 10),
				('Chosen Knights', 435, 125, 3, 5),
				('Chosen Chariot', 345, None, 1, 1),
				('Forsworn', 180, 60, 3, 9),
				('Wrecthed One', 105, 90, 1, 6),
				('Battleshrine', 290, None, 1, 1),
				('Flayers', 145, 19, 5, 10),
				('Barbarian Horsemen', 135, 20, 5, 15),
				('Warhounds', 90, 10, 5, 15),
				('Chimera', 200, None, 1, 1),
				('Feldraks', 340, 105, 3, 6),
			]),
			('Legendary Beasts', 35, None, [
				('Hellmaw', 280, None, 1, 1),
				('Forsaken One', 400, None, 1, 1),
				('Marauding Giant', 260, None, 1, 1),
				('Feldrak Elder', 430, None, 1, 1),
			]),
		])
	]

	for d_name, d_tag, d_unittypes in armies_data:
		data_to_insert = army_data_models.ArmyType(name=d_name, tag=d_tag)
		db.session.add(data_to_insert)

		for ut_name, ut_max, ut_min, ut_units in d_unittypes:
			unit_type_data_to_insert = army_data_models.UnitType(
				name=ut_name,
				army_type=data_to_insert,
				MaxPoints=ut_max,
				MinPoints=ut_min
			)
			db.session.add(unit_type_data_to_insert)

			for u_name, u_start_cost, u_cost_per, u_start_amount, u_max_amount in ut_units:
				unit_data_to_insert = army_data_models.Unit(
					army_type=data_to_insert,
					unit_type=unit_type_data_to_insert,
					name=u_name,
					start_cost=u_start_cost,
					cost_per=u_cost_per,
					start_number=u_start_amount,
					max_amount=u_max_amount
				)
				db.session.add(unit_data_to_insert)

	db.session.commit()


@app.cli.command()
def init_db_test2():
	db.create_all()

	data = ('Dwarven Holds', 'DH', [
			('Characters', 40, None, [
				('King', 225, None, 1, 1, False, [
					('Holdstone', 35, False),
					('Rune of Resonance', 50, False),
					('Ancestral Memory', 60, False),
					('Shield', 15, False),
					('Pistol', 5, False),
					('Guild-Crafted Handgun', 10, False),
					('Crossbow', 10, False),
					('Great Weapon', 20, False),
					('Shield Bearers', 115, False),
					('War Throne', 245, False),
				]),
				('Thane', 120, None, 1, 1, False, [
					('Battle Standard Bearer', 50, False),
					('Holdstone', 30, False),
					('Rune of Resonance', 50, False),
					('Ancestral Memory', 40, False),
					('Shield', 10, False),
					('Pistol', 5, False),
					('Guild-Crafted Handgun', 10, False),
					('Crossbow', 10, False),
					('Great Weapon', 10, False),
					('Shield Bearers', 95, False),
				]),
				('Dragon Seeker', 210, None, 1, 1, False, [
					('Monster Seeker', 60, False),
					('Grim Resolve', 80, False),
				]),
				('Runic Smith', 170, None, 1, 1, False, [
					('Ancestral Memory', 45, False),
					('Rune of Resonance', 50, False),
					('Shield', 5, False),
					('Great Weapon', 10, False),
					('Battle Rune #1', 20, False),
					('Battle Rune #2', 20, False),
					('Battle Rune #3', 20, False),
				]),
				('Engineer', 125, None, 1, 1, False, [
					('Ancestral Memory', 55, False),
					('Rune of Resonance', 50, False),
					('Shield', 5, False),
					('Great Weapon', 5, False),
					('Pistol', 5, False),
					('Guild-Crafted Handgun', 5, False),
					('Crossbow', 5, False),
					('Forge Repeater', 20, False),
					('Wyrn-Slayer Rocket', 30, False),
				]),
				('Anvil of Power', 185, None, 1, 1, False, None),
			]),
			('Core', None, 25, [
				('Clan Warriors', 120, 13, 10, 40, True, [
					('Vanguard', 2, True),
					('Shield', 2, True),
					('Throwing Weapons', 2, True),
					('Paired Weapons', 0, True),
					('Spear & Shield', 3, True),
					('Great Weapon', 3, True),
				]),
				('Greybeards', 175, 20, 10, 30, True, [
					('Vanguard', 2, True),
					('Shield', 2, True),
					('Throwing Weapons', 4, True),
					('Great Weapon', 4, True),
				]),
				('Clan Marksmen', 200, 19, 10, 25, True, [
					('Great Weapon', 4, True),
					('Guild-Crafted Handgun', 4, True),
					('Shield', 2, True),
				]),
			]),
			('Special', None, None, [
				('Deep Watch', 310, 27, 15, 30, True, None),
				('King´s Guard', 310, 27, 15, 30, True, None),
				('Miners', 185, 16, 10, 20, False, [
					('Place Holder', 250, False),
				]),
				('Rangers', 140, 16, 8, 20, False, [
					('Place Holder', 250, False),
				]),
				('Seekers', 110, 21, 5, 25, False, [
					('Place Holder', 250, False),
				]),
				('Vengeance Seeker', 130, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
				('Hold Guardians', 280, 102, 3, 8, False, [
					('Place Holder', 250, False),
				]),
				('Grudge Buster', 350, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
			]),
			('Clans´ Thunder', 35, None, [
				('Forge Wardens', 220, 22, 10, 20, False, [
					('Place Holder', 250, False),
				]),
				('Attack Copter', 175, 130, 1, 2, False, [
					('Place Holder', 250, False),
				]),
				('Steam Bomber', 210, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
			]),
			('Engines of War', 20, None, [
				('Dwarf Ballista', 105, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
				('Flame Cannon', 150, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
				('Catapult', 210, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
				('Cannon', 255, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
				('Organ Gun', 270, None, 1, 1, False, [
					('Place Holder', 250, False),
				]),
			]),
		]),

	for d_name, d_tag, d_unittypes in data:
		data_to_insert = army_data_models.ArmyType(
			name=d_name,
			tag=d_tag
		)
		db.session.add(data_to_insert)

		for ut_name, ut_max, ut_min, ut_units in d_unittypes:
			unit_type_data_to_insert = army_data_models.UnitType(
				name=ut_name,
				army_type=data_to_insert,
				MaxPoints=ut_max,
				MinPoints=ut_min
			)
			db.session.add(unit_type_data_to_insert)

			for u_name, u_start_cost, u_cost_per, u_start_amount, u_max_amount, u_default_updates, u_updates in ut_units:
				unit_data_to_insert = army_data_models.Unit(
					army_type=data_to_insert,
					unit_type=unit_type_data_to_insert,
					name=u_name,
					start_cost=u_start_cost,
					cost_per=u_cost_per,
					start_number=u_start_amount,
					max_amount=u_max_amount,
					default_updates=u_default_updates
				)
				db.session.add(unit_data_to_insert)
				if u_updates:
					for upd_name, upd_cost, upd_per in u_updates:
						update_data_to_insert = army_data_models.UnitUpdates(
							unit=unit_data_to_insert,
							name=upd_name,
							cost=upd_cost,
							per=upd_per
						)
						db.session.add(update_data_to_insert)

	db.session.commit()