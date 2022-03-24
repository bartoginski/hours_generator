from get_expenses import get_hours
from generate_doc import generate_doc

# change path, spreadsheet, cells range
hours, total = get_hours("../Expenses/Expenses_2022.xlsx", "Marzec", "C2:C32")

generate_doc("marzec_podpisy", "01.03.2022", "Bartosz Ogiński", hours, total)
