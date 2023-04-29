number = float(input())
what_are_we_converting = str(input())
converted = str(input())

if what_are_we_converting == 'm' and converted == 'cm':
    number = number * 100
    print(f'{number:.3f}')
elif what_are_we_converting == 'm' and converted == 'mm':
    number = number * 1000
    print(f'{number:.3f}')
elif what_are_we_converting == 'cm' and converted == 'mm':
    number = number * 10
    print(f'{number:.3f}')
elif what_are_we_converting == 'cm' and converted == 'm':
    number = number / 100
    print(f'{number:.3f}')
elif what_are_we_converting == 'mm' and converted == 'cm':
    number = number / 10
    print(f'{number:.3f}')
elif what_are_we_converting == 'mm' and converted == 'm':
    number = number / 1000
    print(f'{number:.3f}')