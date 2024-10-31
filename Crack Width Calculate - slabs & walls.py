# inputs
# ===========
# fy in psi
fy = 60000
# diameter of rebar closest to tension face, inch
dia = 5/8
# rebar area of cross section
Ab = 0.3
# bar spacing, inches
spacing = 5
# required steel
Asr = 0.49
# clear concrete cover, inch
cc = 1.5


# Calculation
# ===========

# provided steel
Asp = Ab*12/spacing

# stress in steel
fs = 0.6 * fy
# reduce fs by ratio of required and provided reinforcement
fs = fs * Asr/Asp

# concrete cover from the tension face to center of closest bar, inch
dc = cc + dia / 2

# Effective tension concrete area
# centroid of perpendicular reinforcement layer from the tension face, inch
a = cc + dia/2
# width of section, inch
b = 12
# total number of bars
n = 12/spacing
A = b * (2*a) / n

W = 0.076 * 1.35 * fs * ((A * dc) ** (1/3)) * 1e-6
S = 540000/fs - 2.5 * cc


# output
# ========

print("Estimated crack width as per ACI 318-95 approach = %.4f inch (%.4f mm)" % (W, W*25.4))
print("Maximum spacing as per ACI 318-99 approach = %.2f inch (%.0f mm)" % (S, S*25.4))
print()
