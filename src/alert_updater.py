from src.common.database import Database
from src.models.alerts.alert import Alert

Database.initialise()
alerts_needing_update = Alert.find_required_update()

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()