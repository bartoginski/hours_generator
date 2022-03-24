from openpyxl import load_workbook


def get_hours(workbook_name, spreadsheet_name, cells_range):
    """
    Gets hours from spreadsheet

    Args:
        workbook_name (string): Excel Workbook name.
        spreadsheet_name (string): Workbook's spreadsheet name.
        cells_range (string): Cells range in format <start_cell>:<end_cell.

    Returns:
        time: list of hours
        total: sum of hours
    """
    # gets workbook
    wb = load_workbook(workbook_name)
    # gets spreadsheet
    sheet = wb[spreadsheet_name]
    # gets rows range e.g. C2:C32
    hours_cells = sheet[cells_range]
    time = []
    total = 0

    for cell in hours_cells:
        hours = cell[0].value

        if hours is not None:
            time.append(float(hours))
            total += float(hours)

    total = round(total, 2)
    print(f"Total time: {total} hours")
    return time, total
