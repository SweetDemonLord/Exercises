def months():
    yield 'January'
    yield 'February'
    yield 'March'
    yield 'April'
    yield 'May'
    yield 'June'
    yield 'July'
    yield 'August'
    yield 'September'
    yield 'October'
    yield 'November'
    yield 'December'
generator_months=months()
for month in generator_months:
    print(month)