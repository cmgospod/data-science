# AirBnB Optimal Price Flask App

## Usage

Send a POST request to https://hostify.herokuapp.com/input passing in the following JSON object:

```
{
    "neighborhood_group":#,
    "neighborhood":#,
    "room_type":#,
    "minimum_nights":#,
    "calculated_host_listings_count":#,
    "availability_of_year":#,
    "bathroom_number":#,
    "bedroom_number":#,
}
```

Replace the #'s with relevant numbers. The `neighborhood_group`, `neighborhood`, and `room_type` values need to be expressed numerically based on [these mappings](https://github.com/bw-airbnbprice3/data-science/tree/master/MODEL).

If configured correctly, you'll receive the following string as the output, replacing `[min-price]` and `[max-price]` with the corresponding numbers.

```
Predicted price range for your listing is: €[min-price]-€[max-price]
```

## Usage (Development)

Clone the repo, then run the following terminal commands within the repo directory.

```
pipenv install
pipenv shell
FLASK_APP=HOSTIFY:APP flask run
```

To test the endpoint, create and run the following python code, replacing #'s with relevant numbers.

```
import requests
import json
dictToSend = {
    "neighborhood_group":#,
    "neighborhood":#,
    "room_type":#,
    "minimum_nights":#,
    "calculated_host_listings_count":#,
    "availability_of_year":#,
    "bathroom_number":#,
    "bedroom_number":#,
}
res = requests.post('http://127.0.0.1:5000/input', data=json.dumps(dictToSend))
print ('Response from server:',res.text)
```

