import open3d as o3d
import numpy as np
import math
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import math
from functools import reduce

pcd = o3d.io.read_point_cloud("src/data/stockpile.ply")
o3d.visualization.draw_geometries([pcd])

axes = o3d.geometry.TriangleMesh.create_coordinate_frame()