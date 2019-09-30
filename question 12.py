## question 12 solution ##
def convertFahrenheitToCelsius(deg_f):
    deg_f = int(deg_f)

    deg_c = (deg_f - 32) * 5/9

    return deg_c

convertFahrenheitToCelsius(1)