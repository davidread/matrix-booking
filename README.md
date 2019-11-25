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

# or you can use a full URL
all_bookings = matrix.get_with_full_url('https://app.matrixbooking.com/api/v1/user/current/bookings?include=locations&include=visit&include=facilities&include=extras&include=bookingSettings&include=layouts')
pprint(all_bookings)
```

## API calls

API documentation: https://developers.matrixbooking.com/#introduction

Also you can work out syntax by trying an action manually on the Matrix website, and look at the XHR request it creates.

## Auth

This client uses username/password, as you would if logging into the website, which seems fine for low key personal use.

Alternatively, with the blessing of the administrators, you could [get an API key](https://developers.matrixbooking.com/#authentication). Support for this could be added to this client with a line or two of code.

## Warning

This client is intended for good purposes - e.g. analysis of booking patterns to maximize best use of resources. However it can be abused for less good purposes. Please don't.

Danger areas:

* Getting an unfair advantage when booking resources
* Use of personal data

Relevant rules:

* corporate codes of conduct
* ethical data science

Remember you are using your own credentials, so your actions are logged against you.

The Matrix Booking API is not officially documented, and whilst it's clear how to use it, and there are no technical barriers, if there is abuse then we can expect the company apply barriers to API use. So don't.
