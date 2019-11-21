# Matrix Booking client

Python client for interacting with the Matric Booking API.

Unofficial.

## Getting started

First create your config file with your Matrix Booking username and password

```bash
cp matrix.ini.template matrix.ini
# now edit matrix.ini to insert your matrix username & password
```

Now in python you can make calls

```python
import matrix
# initializing the client logs you in
matrix = MatrixClient()

# get a list of my bookings
bookings = matrix.get_my_bookings()
print(bookings)

# check availability for a particular resource
availability = matrix.get('availability', 'bc=1&f=2019-11-13T11:00&include=locations&include=bookingSettings&include=timeslots&l=718321&status=available')
from pprint import pprint
pprint(availability).json()
```

## Warning

This client is intended for good purposes - e.g. analysis of booking patterns to maximize best use of resources. However it can be abused for less good purposes. Please don't.

Danger areas:

* Getting an unfair advantage when booking resources
* Use of personal data

Relevant rules:

* corporate codes of conduct
* ethical data science

Remember you are using your own credentials, so your actions are logged against you.

The Matrix Booking API is not officially documented, and whilst it's clear how to use it, and there are no technical barriers, if there is abuse then it would make sense for the barriers to API use the API to be chagnehave barriers put up. So don't.
