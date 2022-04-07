"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730468950"

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(path, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line by line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Gets the column values from a table."""
    column: list[str] = []
    for row in table:
        for key in row:
            if key == column_name:
                column.append(row[key])
    return column


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Makes a row based table column based."""
    result: dict[str, list[str]] = dict()
    for index in table:
        current_row: dict[str, str] = index
        for key in current_row:
            result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Returns a table that only contains the first given number of rows for each column."""
    result: dict[str, list[str]] = {}
    for key in table:
        current_column: list[str] = table[key]
        if number_of_rows >= len(current_column):
            result[key] = table[key]
        else:
            i: int = 0
            values: list[str] = []
        
            while i < number_of_rows and i < len(current_column) - 1:
                values.append(current_column[i])
                i += 1
            result[key] = values
    return result


def select(table: dict[str, list[str]], included_columns: list[str]) -> dict[str, list[str]]:
    """Makes a new table that includes only certain columns."""
    selected_columns: dict[str, list[str]] = {}
    for key in table:
        if key in included_columns:
            selected_columns[key] = table[key]
    return selected_columns


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables together into one."""
    result: dict[str, list[str]] = {}
    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]
    return result


def count(wanted_counts: list[str]) -> dict[str, int]:
    """Gets the counts of the items told to count."""
    counts: dict[str, int] = {}
    for item in wanted_counts:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts