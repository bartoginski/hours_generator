
# Hours Table Generator

A script that generates a text document with a table of hours, designed to automate a boring task
## Run Locally

Clone the project

```bash
  $ git clone https://github.com/bartoginski/hours_generator
```

Go to the project directory

```bash
  $ cd hour_generator
```

Create and activate venv

```bash
  $ python3 -m venv venv
  $ source ./venv/bin/activate
```

Install dependencies

```bash
  pip install -r ./requirements.txt
```

Edit main.py

```python
...

# change path to workbook, spreadsheet name, cells range
hours, total = get_hours("../Expenses/Expenses_2022.xlsx", "Marzec", "C2:C32")

#change output filename, contract date, programmer
# hours and total variables are from excel file
generate_doc("marzec_podpisy", "01.03.2022", "Bartosz Ogiński", hours, total)
```

Run main.py
```bash
  $ python3 main.py
```

