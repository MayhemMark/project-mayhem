from calculation import get_weight_for_input
import sys


class WeightUnit:
    def __init__(self, label, unitPerKilo, abbreviations):
        self.label = label
        self.unitPerKilo = unitPerKilo
        self.abbreviations = abbreviations

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.label)


list_options = (
    WeightUnit("Kilos", 1, ("kg", "kg.", "kilos", "kilo")),
    WeightUnit("Gram", 1000, ("gr", "gram", "gr.", "grm")),
    WeightUnit("Pounds", (1/0.45), ("p", "pd", "pds", "lbs", "lb")),
    WeightUnit("Stone", 25, ("s", "st", "stone")),

    # Sexagsimal table of units
    WeightUnit("Talent", 1/30.24, ("t", "tlt", "tl", "tlnt")),
    WeightUnit("Mina", 1/0.504, ("m", "mina")),
    WeightUnit("Karsa", 1/0.084, ("k", "karsa")),
    WeightUnit("zwz", 1/0.0042, ("z", "zwz")),
    WeightUnit("Danake", 1/0.00139, ("d", "danake")),
    WeightUnit("Halluru", 1/0.00021, ("h")),

    # Need to keep the "shekel" alias or this entry is not going to work for "sh" for some reason
    WeightUnit("Shekel", 1/0.0084, ("sh")),
)

if (len(sys.argv) >= 3):
    raw_input_str = sys.argv[1] + ' ' + sys.argv[2]
elif (len(sys.argv) >= 2):
    raw_input_str = sys.argv[1]
else:
    raw_input_str = input("Weight:")

input = get_weight_for_input(list_options, raw_input_str)
input_type = input[1]
input_quantity = input[0]

print(f"{input_quantity} {input_type.label} is the same as:")
for item in list_options:
    input_quantity_calculated = (
        input_quantity/input_type.unitPerKilo) * item.unitPerKilo
    print(f'  {input_quantity_calculated} {item.label}')
