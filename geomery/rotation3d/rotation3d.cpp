#include <cmath>
#include <Eigen/eigen>

extern Parameter par;

const double RAD = 180./M_PI;
const double PI = M_PI;
// default vector
const Eigen::Vector3d DIR(0., 0., 1.);

namespace Rotation3d{
// computation operators //
Eigen::MatrixXd rotationX(const double alpha_x){
	Eigen::MatrixXd Rx(3,3);
	Rx(0,0) = 1.; 			 Rx(0,1) = 0.; 		      Rx(0,2) = 0.;
	Rx(1,0) = 0.; 			 Rx(1,1) =  cos(alpha_x); Rx(1,2) = -sin(alpha_x);
	Rx(2,0) = 0.; 			 Rx(2,1) = +sin(alpha_x); Rx(2,2) = +cos(alpha_x);
	//std::cout << "Rx = " << Rx << std::endl;
	return Rx;
}
Eigen::MatrixXd rotationY(const double alpha_y){
	Eigen::MatrixXd Ry(3,3);
	Ry(0,0) =  cos(alpha_y); Ry(0,1) = 0.; 		      Ry(0,2) = +sin(alpha_y);
	Ry(1,0) = 0.; 			 Ry(1,1) = 1.; 		      Ry(1,2) = 0.;
	Ry(2,0) = -sin(alpha_y); Ry(2,1) = 0.; 		      Ry(2,2) =  cos(alpha_y);
	//std::cout << "Ry = " << Ry << std::endl;
	return Ry;
}
Eigen::MatrixXd rotationZ(const double alpha_z){
	Eigen::MatrixXd Rz(3,3);
	Rz(0,0) =  cos(alpha_z); Rz(0,1) = -sin(alpha_z); Rz(0,2) = 0.;
	Rz(1,0) = +sin(alpha_z); Rz(1,1) =  cos(alpha_z); Rz(1,2) = 0.;
	Rz(2,0) = 0.;  			 Rz(2,1) = 0.; 			  Rz(2,2) = 1.;
	//std::cout << "Rz = " << Rz << std::endl;
	return Rz;
}
// rotate vec2 to be in the same direction of vec1
Eigen::MatrixXd rotationMatrix(const Eigen::Vector3d& vec1, const Eigen::Vector3d& vec2,
			       Eigen::Matrix3d& R){
	// find the rotation axis:
	Eigen::Vector3d axis;
	axis = vec2.cross(vec1)/(vec2.cross(vec1)).norm();
	//std::cout << "Axis is " << std::endl << axis << std::endl;

	// find the angle
	double angle = acos(vec2.dot(vec1)/vec2.norm()/vec1.norm());

	// determine rotation matrix R
	const Eigen::Matrix3d I = Eigen::Matrix3d::Identity();
	if(angle < 1e-6){
		R = I;
	}else{
		Eigen::Matrix3d A;
		A(0,0) = 0.;       A(0,1) = -axis(2); A(0,2) = axis(1);
		A(1,0) = axis(2);  A(1,1) = 0;        A(1,2) = -axis(0);
		A(2,0) = -axis(1); A(2,1) = axis(0);  A(2,2) = 0;
		R = I + sin(angle)*A + (1-cos(angle))*A*A;
	}
	return R;
	//std::cout << "Rotation matrix = " << std::endl << R << std::endl;
	//std::cout << std::endl << std::endl << "Final rotation = " << std::endl << R*vec2*length_ << std::endl << std::endl;
}

}

