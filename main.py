#import our database and gui files
import src.database.database as database_connector
import src.gui.gui as gui_connector;

database_connector.connect_to_database();
print("[debug] -> connected to our database")

#initialize our gui
gui_connector.show_gui();