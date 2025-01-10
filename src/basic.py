import open3d as o3d

# Just create and display the coordinate frame
axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0, 0, 0])