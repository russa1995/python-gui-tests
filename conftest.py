import pytest
from fixture.application import Application
import importlib
import xlrd
import os.path


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\pyauto\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdatas = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdatas, ids=(str(x) for x in testdatas))
        elif fixture.startswith("xlsx_"):
            excel_column = load_from_excel(fixture[5:])
            metafunc.parametrize(fixture, excel_column, ids=(str(x) for x in excel_column))

def load_from_module(module):
     return importlib.import_module("data.%s" % module).testdatas


def load_from_excel(file):
    excel = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "python-gui-tests\\%s.xlsx" % file))
    sheet = excel.sheet_by_index(0)
    excel_column = []
    row_number = sheet.nrows
    for row in range(0,row_number):
        excel_column.append(str(sheet.row(row)[0]).replace("text:", "").replace("'", "").replace(":", " ").replace(".", " "))
    return excel_column