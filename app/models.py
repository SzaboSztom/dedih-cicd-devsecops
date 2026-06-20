from pydantic import BaseModel, Field

# Pydantic modell a bemenet validálásához.
# A defense in depth elv szerint a backend sosem bízza meg a frontendet,
# hanem újra ellenőrzi a bemenő adatokat.


class Greeting(BaseModel):
    # A keresztnév 1 és 50 karakter közé esik.
    # Ez a Pydantic validáció a "defense in depth" réteg: a bemeneti adatot
    # nem bízzuk a frontendre, a backend újra ellenőrzi.
    name: str = Field(min_length=1, max_length=50)
