from typing import TypedDict


#TypedDict describes the expected 
# keys and value types in a dictionary. It helps editors and type-checking tools catch mistakes; it does not validate
#  data automatically at runtime.
class Expense(TypedDict):
    name : str
    amount :float
    categort:str