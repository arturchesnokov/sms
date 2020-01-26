def only_numbers(st):
    return ''.join(n for n in st if n.isdigit())


print(only_numbers('098-kdsjfh-fs34234'))
