//============================================================================
// Name        : Bezier.cpp
// Author      : Ge YIN
// Version     :
// Copyright   : This is to thin 3D vtk file
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <fstream>
#include </home/gy241/library_C++/eigen/Eigen/Dense> //using Eigen library: define matrix
#include </home/gy241/library_C++/eigen/Eigen/Core>  //using MatrixXd as function parameters


class PointSet{
public:
	PointSet( std::vector<double> coordinate );
	std::vector<double> giveCoordinate();
private:
	std::vector<double> coordinate_;
};
PointSet::PointSet( std::vector<double> coordinate ){
	coordinate_ = coordinate;
}
std::vector<double> PointSet::giveCoordinate(){
	return coordinate_;
}

template< int bezier_order >
class Bezier{
public:
	Bezier( std::vector<int> line_chain, Image image );

	void showControlPoint();
	std::vector<double> giveControlPoint( int index_control_point );

private:
	std::vector<PointSet> control_point_;
	std::vector<double> basis_function( double x );
};

template< int bezier_order >
Bezier<bezier_order>::Bezier( std::vector<int> line_chain, Image image ){
	 int num_Q = line_chain.size();
	 int num_P = bezier_order + 1;

	 std::vector<double> start, end;

	 // start control point
	 start.push_back( image.giveCoordinate(line_chain[0])[0] );
	 start.push_back( image.giveCoordinate(line_chain[0])[1] );
	 start.push_back( image.giveCoordinate(line_chain[0])[2] );
	 // last control point
	 end.push_back( image.giveCoordinate(line_chain[num_Q - 1])[0] );
	 end.push_back( image.giveCoordinate(line_chain[num_Q - 1])[1] );
	 end.push_back( image.giveCoordinate(line_chain[num_Q - 1])[2] );

	 // determine arc length for isoparametric parameter u
	 std::vector<double> arc_length, u;
	 double sum_arc = 0;
	 arc_length.push_back(0.);
	 for( int i = 1; i < num_Q; i++ ){
		 double delta_x = image.giveCoordinate( line_chain[i])[0] - image.giveCoordinate(line_chain[i-1])[0];
		 double delta_y = image.giveCoordinate( line_chain[i])[1] - image.giveCoordinate(line_chain[i-1])[1];
		 double delta_z = image.giveCoordinate( line_chain[i])[2] - image.giveCoordinate(line_chain[i-1])[2];
		 double arc = sqrt(delta_x*delta_x + delta_y*delta_y + delta_z*delta_z);
		 sum_arc += arc;
		 arc_length.push_back( sum_arc );
	 }
	 for( int i = 1; i < num_Q - 1; i++ ){
		 u.push_back(arc_length[i]/arc_length[num_Q - 1]);
	 }
	 arc_length.clear();

	 // construct N
	 Eigen::MatrixXd N(num_Q - 2, num_P - 2);
	 for ( int i = 0; i < N.cols(); i ++ ){
		 for ( int j = 0; j < N.rows(); j ++ ){
			 N(i,j) = basis_function( u[i + 1] )[j];
		 }
	 }

	 // construct Rk
	 Eigen::MatrixXd Rk(num_Q - 2, 3);
	 for( int i = 0; i < Rk.cols(); i++ ){
		 for( int j = 0; j < Rk.rows(); j++ ){
			 Rk(i,j) = image.giveCoordinate(line_chain[i+1])[j] -
					 basis_function(u[i + 1])[0]*image.giveCoordinate(line_chain[0])[j] - basis_function(u[i + 1])[3]*image.giveCoordinate(line_chain[num_Q-1])[j];
		 }
	 }

	 // determine R from Rk and N
	 Eigen::MatrixXd R(num_P - 2, 3);
	 for( int i = 0; i < R.cols(); i ++ ){
		 for( int j = 0; j < R.rows(); j++ ){
			 double sum_NR = 0.;
			 for( int k = 0; k < num_Q - 1; k++ ){
				 sum_NR += basis_function(u[k+1])*Rk(k,j);
			 }
			 R(i,j) = sum_NR;
		 }
	 }

	 // solve the control point in between
	 Eigen::MatrixXd P( num_P - 2, 3);
	 P = (N.transpose()*N).inverse()*R;

	 // construct vector of point set
	 PointSet *pointer = new PointSet(start);
	 control_point_.push_back(*pointer);

	 for( int i = 0; i < num_P - 2; i ++ ){
		 std::vector<double> temp_coor;
		 for ( int j = 0; j < 3; j ++ ){
			 temp_coor.push_back( P(i,j) );
		 }
		 *pointer = new PointSet(temp_coor);
		 control_point_.push_back(*pointer);
		 temp_coor.clear();
	 }

	 *pointer = new PointSet(end);
	 control_point_.push_back(*pointer);

}

template< int bezier_order >
std::vector<double> Bezier<bezier_order>::basis_function( double x ){

	std::vector<double> n;

	if( bezier_order == 3 ){

		n.push_back( ( 1 - x )*( 1 - x )*( 1 - x ) );
		n.push_back( 3*x*( 1 - x )*( 1 - x ) );
		n.push_back( 3*x*x*( 1 - x ) );
		n.push_back( x*x*x );

	}
	return n;
}

template< int bezier_order >
std::vector<double> Bezier<bezier_order>::giveControlPoint( int index_control_point ){
	std::vector<double> control_point;
	control_point = control_point_[index_control_point].giveCoordinate();

	return control_point;
}

template< int bezier_order >
void Bezier<bezier_order>::showControlPoint(){
	std::cout << "      -> Four Control points: ";
	for ( int i = 0; i <= bezier_order; i ++ ){
		std::cout << "  ( " << control_point_[i].giveCoordinate()[0] << " , ";
		std::cout << control_point_[i].giveCoordinate()[1] << " , ";
		std::cout << control_point_[i].giveCoordinate()[2] << " )  ";
	}
	std::cout << std::endl;
}

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}
