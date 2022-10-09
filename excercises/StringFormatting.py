def print_formatted(number):
    n_length = len(bin(n)[2:])
    for i in range (1, (n+1)):
            octa = str(oct(i))[2:]
            hexa = str(hex(i))[2:].upper()
            bina = str(bin(i))[2:]
            print( str(i).rjust(n_length), octa.rjust(n_length), hexa.rjust(n_length), bina.rjust(n_length))

    
