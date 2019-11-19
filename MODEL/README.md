# Model for predictions

## Usage:
```
from joblib import load
model = load('model.joblib')

prediction = model.predict(['neighbourhood_group', 
                            'neighbourhood', 
                            'room_type', 
                            'minimum_nights', 
                            'calculated_host_listings_count', 
                            'availability_365', 
                            'bathrooms', 
                            'bedrooms'])
```
