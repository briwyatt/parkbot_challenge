### ParkBot

ParkBot is a command line utility program that provides AirGarage users
with information about various different parking options available to them.

By default, this program will return information on *all* currently available parking spot data --

In other words, a user who wants to "select all" parking data options
will simply input:

$ python main.py

ParkBot also accepts multiple options for filtering by important criteria such as location --

For example, a user who needs to narrow down their search to find parking optioms within the state of Arizona
use the `locale` parameter like so:

$ python main.py --locale="AZ"

