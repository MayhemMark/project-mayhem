from calculation import get_weight_for_input
class WeightUnit:
    def __init__(self, label, unitPerKilo, abbreviations):
        self.label = label
        self.unitPerKilo = unitPerKilo
        self.abbreviations = abbreviations

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.label)

list_options = (
    WeightUnit(
        "Pounds",
        (1/0.45),
        ("p", "pd", "pds", "lbs", "lb")
    ),
    WeightUnit(
        "Stone",
        25,
        ("s", "st", "stone")
    ),

    WeightUnit("Kilos", 1, ("kg", "kg.", "kilos", "kilo")),
    WeightUnit("Gram", 1000, ("gr","gram","gr.","grm")),

    # Sexagsimal table of units
    WeightUnit("Talent", 1/30.24, ("t", "tlt", "tl", "tlnt")),
    WeightUnit("Mina", 1/0.504, ("m", "mina")),
    WeightUnit("Karsa", 1/0.084, ("k", "karsa")),
    WeightUnit("Shekel", 1/0.0084, ("sh")),
    WeightUnit("zwz", 1/0.0042, ("z")),
    WeightUnit("Danake", 1/0.00139, ("d")),
    WeightUnit("Halluru", 1/0.00021, ("x")),
)

input = get_weight_for_input(list_options, input("Weight:"))
print(input)
input_type = input[1]

input_quantity = float(input[0])
print(f"{input_quantity} {input_type.label} is the same as:")

for item in list_options:
    input_quantity_calculated = (input_quantity/input_type.unitPerKilo) * item.unitPerKilo
    print(f'  {input_quantity_calculated} {item.label}')