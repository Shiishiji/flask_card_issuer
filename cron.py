from datetime import datetime
from application import Application

application = Application()

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    # application.debug = True

    print("Running planned job " + (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
    application.handle_ordered_card()
    print("Finished " + (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
