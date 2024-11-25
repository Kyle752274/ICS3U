"""
1) Hypothermia
Hypothermia is defined when the body core temperature is below 35.0 °C in humans. In mild hypothermia, there is shivering and mental confusion. In moderate hypothermia, shivering stops and confusion increases.
2) Frostbite
Frostbite is the injury to body tissues caused by exposure to extreme cold, typically affecting the nose, fingers, or toes and sometimes resulting in gangrene.
"""

def wc(TdegC, windKPH):
    """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
    """
    vTemp = 0

    vTemp = 13.12 + 0.6215 * TdegC
    vTemp = vTemp - 11.37 * pow(windKPH, 0.16)
    vTemp = vTemp + 0.3965 * TdegC * pow(windKPH, 0.16)

    return vTemp

def getWarning(windChill):
    windChill = round(windChill)
    if windChill <= 0 and windChill >= -9:
        return "Low risk"
    elif windChill <= -10 and windChill >= -27:
        return "Moderate risk of hypothermia"
    elif windChill <= -28 and windChill >= -39:
        return "High risk of frostbite"
    elif windChill <= -40 and windChill >= -47:
        return "Severe risk of frostbite: exposed skin freezes in 5-10 minutes"
    elif windChill <= -48 and windChill >= -54:
        return "Severe risk of frostbite: exposed skin freezes in 2-5 minutes"
    elif windChill <= -55:
        return "Extreme risk: exposed skin freezes in under 2 minutes"

T = -5.0
W = 10.0
WC = wc(T, W)
warning = getWarning(WC)
print("WC=%8.3f T=%8.3f W=%6.3f km/h %s" % (WC, T, W, warning))

T = -20.0
W = 20.0
WC = wc(T, W)
warning = getWarning(WC)
print("WC=%8.3f T=%8.3f W=%6.3f km/h %s" % (WC, T, W, warning))

T = -45.0
W = 40.0
WC = wc(T, W)
warning = getWarning(WC)
print("WC=%8.3f T=%8.3f W=%6.3f km/h %s" % (WC, T, W, warning))
