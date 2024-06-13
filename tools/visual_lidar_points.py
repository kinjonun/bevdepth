import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
from nuscenes.utils.data_classes import LidarPointCloud


pcd_bin_file = "/media/sun/z/nuscenes/nuscenes/samples/LIDAR_TOP/n008-2018-05-21-11-06-59-0400__LIDAR_TOP__1526915243047392.pcd.bin"

# Load the .pcd.bin file.
pc = LidarPointCloud.from_file(pcd_bin_file)
pcd = pc.points.T
pcd = pcd.reshape((-1, 4))[:, 0:3]

point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(pcd)

# 可视化点云
o3d.visualization.draw_geometries([point_cloud])



