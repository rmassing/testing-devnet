import xlrd

def hostlist(xls_file):
    sheet = open_xlsxfile(xls_file)
    rows = sheet.nrows
    hostsdict = {}
    for row_index in range(2, rows):
        name, ipaddress = sheet.row_values(row_index)

        # hostsdict[row_index] = {}
        hostsdict[name] = ipaddress

    return hostsdict

def open_xlsxfile(xls_file):
    """
    makes given xlsx spreadsheet readable

    Returns: book, sheet and sheet2

    """
    try:
        book = xlrd.open_workbook(file_contents=xls_file.read())
    except Exception:
        try:
            book = xlrd.open_workbook(xls_file)
        except Exception:
            warning = "error"
            return False, warning

    try:
        sheet = book.sheet_by_name("Sheet1")
    except Exception:
        warning = "error"
        return False, warning

    return sheet

if __name__ == '__main__':
    output = hostlist('hosts.xlsx')
    print(output)
    # print(output)
    # for row in output:
    #     print(row)
    # output = get_hosts_2_dict('content-hosts.csv')
    # for row in output:
    #     print(row)
    # for row in output:
    #     print(row)