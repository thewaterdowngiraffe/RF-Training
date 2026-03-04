"""
update your vehicle classes to include a `get_speed()` function that returns the current speed
use


create your vehicles within the racers list and hit play.
This is so you can see the impact of what you have made as well as the config.

you will have to do some physics


(a*t) + vi = vf
f/m = a


time will be constant. each time i call the function 0.25 seconds will have passed
define the mass of each vehicle and give it a force
lets assume the mass for cars is 1000, motorcycle: 227 and plane 5670
lets assume the force for cars is 3000, motorcycle: 2500 and plane 10000
define a mass for each and use this fomula to calclate the speed

```python
self.speed = min((self.force/self.mass)*0.25+self.speed, self.top_speed)
return self.speed
```

you will reqire `self.speed` and `self.done` to be added along with any of the
requred var for the above function.

you will also need to create a __str__ function for the print.
"""
from race import race
from vehicles import *


racers = [
    car(),
    motorcycle(),
    plane()
]
race(*racers)
