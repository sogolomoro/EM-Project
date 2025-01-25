import os
import numpy as np
import KUEM as EM
import matplotlib.pyplot as plt

plt.close("all")

print("Please Enter Surface Charge Density")
SurfaceChargeDensity = int(input())
print("Please Enter Plate seperation distance")
d = float(input())
print("Please Enter the Length of plate")
L = float(input())


N = np.array([49, 49, 49], dtype = int)
delta_x = np.array([2, 2, 2])
x0 = np.array([-1, -1, -1])
Boundaries = [["closed", "closed"], ["closed", "closed"], ["closed", "closed"]]

Exact = False
Progress = 5
approx_n = 0.1

PlotScalar = True
PlotContour = True
PlotVector = False
PlotStreams = True

StreamDensity = 2
StreamLength = 1
ContourLevels = 10
ContourLim = (-0.1, 0.1)


FilePos = "FinitePlateCapacitor/"
Name_E_2D = "ExFinitePlateCapacitorE.png"
Name_V_2D = "ExFinitePlateCapacitorV.png"
Name_Rho_2D = "ExFinitePlateCapacitorRho.png"
Save = True


def J(dx, N, x0, c, mu0):

    Grid = np.zeros(tuple(N) + (4,))
    
   
    Grid[int(N[0] * (1 - L) / 2):int(N[0] * (1 + L) / 2), int(N[1] * (1 - L) / 2):int(N[1] * (1 + L) / 2), int(N[2] * (1 + d) / 2), 0] = -c * SurfaceChargeDensity / dx[2]
    Grid[int(N[0] * (1 - L) / 2):int(N[0] * (1 + L) / 2), int(N[1] * (1 - L) / 2):int(N[1] * (1 + L) / 2), int(N[2] * (1 - d) / 2), 0] = c * SurfaceChargeDensity / dx[2]
    
  
    J_Vector = EM.to_vector(Grid, N)
  
    def get_J(t):
        return J_Vector
    
    return get_J


Sim = EM.sim(N, delta_x = delta_x, x0 = x0, approx_n = approx_n, J = J, boundaries = Boundaries)

x_hat = np.array([1, 0, 0])
y_hat = np.array([0, 0, 1])

Res_scalar = 1000
Res_vector = 30


extent = [0, delta_x[0], 0, delta_x[2]]
PointsSize = np.array([delta_x[0], delta_x[2]])

Points_scalar = EM.sample_points_plane(x_hat, y_hat, np.array([0, 0, 0]), PointsSize, np.array([Res_scalar, Res_scalar]))
Points_vector = EM.sample_points_plane(x_hat, y_hat, np.array([0, 0, 0]), PointsSize, np.array([Res_vector, Res_vector]))


Sampler_E_2D = EM.sampler_E_vector(Sim, Points_vector, x_hat, y_hat)
Sampler_V_2D = EM.sampler_V_scalar(Sim, Points_scalar)
Sampler_Rho_2D = EM.sampler_Rho_scalar(Sim, Points_scalar)


print("Solving")
StaticTime = Sim.solve(exact = Exact, progress = Progress)
print(f"Solved in {StaticTime:.2g} s")


if Save is True and not os.path.exists(FilePos):
    os.mkdir(FilePos)

fig_E_2D, _, _ = Sampler_E_2D.plot(0, extent = extent, use_vector = PlotVector, use_streams = PlotStreams, density = StreamDensity, length = StreamLength)
if Save is True:
    fig_E_2D.savefig(FilePos + Name_E_2D)

fig_V_2D, _, _ = Sampler_V_2D.plot(0, extent = extent, contour_lim = ContourLim, use_scalar = PlotScalar, use_contour = PlotContour)
if Save is True:
    fig_V_2D.savefig(FilePos + Name_V_2D)

fig_Rho_2D, _, _ = Sampler_Rho_2D.plot(0, extent = extent)
if Save is True:
    fig_Rho_2D.savefig(FilePos + Name_Rho_2D)
plt.show()