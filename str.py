# s= input('문자열을 입력해하시오')
# a= s.split()
# print(a)
import numpy as np
import matplotlib.pyplot as plt

# Define theta
theta = np.linspace(0, 2 * np.pi, 1000)

# Define r for both curves
r1 = np.sin(theta)
r2 = 1 - np.sin(theta)

# Create polar plot
plt.figure()
ax = plt.subplot(111, polar=True)
ax.plot(theta, r1, label=r'$r = \sin \theta$')
ax.plot(theta, r2, label=r'$r = 1 - \sin \theta$')

# Mark the intersection points
ax.plot([np.pi/6, 5*np.pi/6], [1/2, 1/2], 'ro') # Intersection points

# Add legend
plt.legend()

# Display plot
plt.show()
