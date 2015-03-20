# xyz-to-obj
If you want to embed a set of points aka a point cloud in 3D-PDF it is not possible because 3D-PDF only supports faces.

This Script creates a cube at each point of a given point cloud in XYZ-format and outputs it in Wavefront OBJ.

One way to create a PDF out of the resulting OBJ file is to open it up in MeshLab an export it to U3D. MeshLab will create a TEX file along the U3D which you can compile using pdflatex.


## Usage
	xyz-to-obj.py input_file edge_length

where input_file is the point cloud and edge_length the lenghth of the edge of the cubes

## Example
	python xyz-to-obj.py example.xyz 0.1
