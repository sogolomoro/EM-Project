import os
import numpy as np
import KUEM as EM
import matplotlib.pyplot as plt

plt.close("all")

print("Please Enter Surface Charge Density")
SurfaceChargeDensity = int(input())
print("Please Enter Plate seperation distance")
d = float(input())


N = np.array([1, 1, 10000], dtype = int)
delta_x = np.array([2, 2, 2])
x0 = np.array([-1, -1, -1])
Boundaries = ["periodic", "periodic", ["closed", "flat"]]


Exact = True
Progress = 5
approx_n = 0.1


PlotVector = True
PlotStreams = False

StreamDensity = 2
StreamLength = 1

FilePos = "InfinitePlateCapacitor/"
Name_E_2D = "ExInfinitePlateCapacitorE.png"
Name_V_1D = "ExInfinitePlateCapacitorV.png"
Save = True


def J(dx, N, x0, c, mu0):

    Grid = np.zeros(tuple(N) + (4,))
    
    
    Grid[:, :, int(N[2] * (1 + d) / 2), 0] = -c * SurfaceChargeDensity / dx[2]
    Grid[:, :, int(N[2] * (1 - d) / 2), 0] = c * SurfaceChargeDensity / dx[2]
    
    
    J_Vector = EM.to_vector(Grid, N)
    
    
    def get_J(t):
        return J_Vector
    
    return get_J

Sim = EM.sim(N, delta_x = delta_x, x0 = x0, approx_n = approx_n, J = J, boundaries = Boundaries)


x_hat = np.array([1, 0, 0])
y_hat = np.array([0, 0, 1])

Res_line = 1000
Res_vector = 30


extent = [0, delta_x[2], 0, delta_x[2]]
PointsSize = np.array([delta_x[2], delta_x[2]])
x1 = np.array([0, 0, -delta_x[2] / 2])
x2 = np.array([0, 0, delta_x[2] / 2])

Points_line = EM.sample_points_line(x1, x2, Res_line)
Points_vector = EM.sample_points_plane(x_hat, y_hat, np.array([0, 0, 0]), PointsSize, np.array([Res_vector, Res_vector]))

Sampler_E_2D = EM.sampler_E_vector(Sim, Points_vector, x_hat, y_hat)
Sampler_V_1D = EM.sampler_V_line(Sim, Points_line)

print("Solving")
StaticTime = Sim.solve(exact = Exact, progress = Progress)
print(f"Solved in {StaticTime:.2g} s")


if Save is True and not os.path.exists(FilePos):
    os.mkdir(FilePos)

fig_E_2D, _, _ = Sampler_E_2D.plot(0, extent = extent, cutoff = 0.01, use_vector = PlotVector, use_streams = PlotStreams, density = StreamDensity, length = StreamLength)
if Save is True:
    fig_E_2D.savefig(FilePos + Name_E_2D)

fig_V_1D, _, _ = Sampler_V_1D.plot(0)
if Save is True:
    fig_V_1D.savefig(FilePos + Name_V_1D)
plt.show()