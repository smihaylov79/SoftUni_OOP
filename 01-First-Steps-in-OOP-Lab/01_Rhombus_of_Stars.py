
def print_row(spaces, stars):
    print(' ' * spaces + '* ' * stars)



def print_upper_part(n):
    for row in range(1,n+1):
        spaces= n-row
        print_row(spaces,row)

def print_lower(n):
    for row in range(1,n):
        stars= n-row
        print_row(row, stars)

def final_print(n):
    print_upper_part(n)
    print_lower(n)

n= int(input())
final_print(n)