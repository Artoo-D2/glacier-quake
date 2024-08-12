from math import pi, cos, sin, tan, log10, pow, atan
import matplotlib.pyplot as plt

g = 3.72 #acceleration due to gravity on mars
density = 1600 #density of dry ice on mars
coeff_fric = 0.06 #coefficient of friction between basalt and ice
theta_c = atan(coeff_fric) #critical angle of slide
d=0.01 #distance of slide

area = [] #list of areas

#calculates the mass of Ice from the area of the GLF
def massCalc(a):
    k = 1.12*log10(a) - 0.978
    v = pow(10,k) #calculates the volume from the area
    m = v*density
    return m

#calculates the frictional force that needs to be overcome
def fricForce(a, t):
    t = t*pi/180 #degrees to radians
    f = tan(theta_c)*massCalc(a)*g*cos(t)
    return f

#calculates the potential force due to gravity component
def potential(a, t):
    t = t*pi/180 #degrees to radians
    p = massCalc(a)*g*sin(t)
    return p

fig = plt.figure(figsize = (10, 10))

x = 1

#for loop to increment the area by 1000000 sq. meters after every iteration
for area in range (1000000, 10000001, 1000000):
    c = 0
    theta = [] #list to store the angles of slope
    energy = [] #list to store the energies for each angle of slope

    while(c<30):
        theta.append(c) 
        e = (potential(area, c) - fricForce(area, c))*d #calculates the energy generated for each angle of slope
        energy.append(e)
        c = c + 0.1
    
    plt.plot(theta, energy, label = 'Glacier {}'.format(x))
    x = x+1

plt.ylim([0, 100000000]) #to only display the positive energy values
plt.xlabel('Angle')
plt.ylabel('Energy')
plt.axvline(x = 5, color = 'k', label = 'Theta = 5 degrees', linestyle = 'dashed')
plt.axvline(x = 15, color = 'k', label = 'Theta = 15 degrees', linestyle = 'dashed')
plt.axvline(x = 25, color = 'k', label = 'Theta = 25 degrees', linestyle = 'dashed')
leg = plt.legend(loc='upper left')
plt.grid()
plt.show()