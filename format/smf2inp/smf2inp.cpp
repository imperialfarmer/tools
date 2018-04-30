#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <iostream>
#include <cstring>
#include <vector>

#define dual_line std::endl << std::endl

void abaqusScript(std::string fileName, std::string loadCase){
	// input model
	std::string dir = "./data/" + fileName + "/";
	std::ifstream smf; smf.open((dir+"model.smf").c_str());
	std::string testline;
	for(int i = 0; i < 6; i++){
		smf >> testline;
	}
	smf >> testline; const int numNode = atof(testline.c_str());
	smf >> testline; const int numEle = atof(testline.c_str());

	std::vector< std::vector<double> > node(numNode, std::vector<double>(3));
	std::vector< std::vector<int> > element(numEle, std::vector<int>(2));

	std::cout << std::endl << "  -> Input data: " << std::endl;

	// input node
	for(int i = 0; i < numNode; i++){
		for(int j = 0; j < 3; j++){
			smf >> testline;
			node[i][j] = atof(testline.c_str());
		}
	}

	std::cout << "     read node data  " << std::endl;

	// input element
	for(int i = 0; i < numEle; i++){
		for(int j = 0; j < 2; j++){
			smf >> testline;
			element[i][j] = atof(testline.c_str()) + 1;
		}
	}
	std::cout << "     read element data  " << std::endl;

	smf.close();

	// input radius
	std::ifstream rad; rad.open((dir+"radius.dat").c_str());
	std::vector<double> radius(numEle);
	for(int i = 0; i < numEle; i++){
		rad >> testline;
		if(rad.fail()) radius[i] = 5;
		else radius[i] = sqrt(atof(testline.c_str())/3.1415926)*1.6;
	}
	rad.close();
	std::cout << "     read cross-section data  " << std::endl;

	// input material
	std::ifstream mat; mat.open((dir+"material.dat").c_str());
	mat >> testline; const double modulus = atof(testline.c_str());
	mat >> testline; const double poisson = atof(testline.c_str());
	mat >> testline; const double density = atof(testline.c_str());
	mat.close();
	std::cout << "     read material data  " << std::endl;
	std::cout << dual_line;

	// input BC and mark which node is boundary
	std::ifstream f; f.open((dir+"f"+loadCase+".txt").c_str());
	f >> testline; const int numNodeF = atof(testline.c_str());
	f >> testline; const int dimF = atof(testline.c_str());
	std::vector<int> indexNodeF(numNodeF);
	std::vector<std::vector<double> > nodeF(numNodeF,std::vector<double>(dimF));

	std::cout << "  -> Node Load List: " << std::endl;
	for(int i = 0; i < numNodeF; i++){
		f >> testline; indexNodeF[i] = atof(testline.c_str());
		for(int j = 0; j < dimF; j++){
			f >> testline; nodeF[i][j] = atof(testline.c_str());
		}
		std::cout << "     Node " << indexNodeF[i] << ": " << nodeF[i][0] << " " << nodeF[i][1] << " " << nodeF[i][2] << " " <<
				nodeF[i][3] << " " << nodeF[i][4] << " "  << nodeF[i][5] << std::endl;
	}
	f.close();
	std::cout << dual_line;

	std::ifstream bc; bc.open((dir+"bc.txt").c_str());
	bc >> testline; const int numNodeBC = atof(testline.c_str());
	std::vector<int> indexNodeBC(numNodeBC);

	std::cout << "  -> Node BC List: " << std::endl;
	for(int i = 0; i < numNodeBC; i++){
		bc >> testline; indexNodeBC[i] = atof(testline.c_str());
		std::cout << "     Node " << indexNodeBC[i] << " is fixed" << std::endl;
	}
	bc.close();
	std::cout << dual_line;


	// output input file
	std::ofstream inp; inp.open((dir+fileName+".inp").c_str());

	// heading
	inp << "*HEADING" << std::endl << "ROBOT ARM BEAM MODEL" << std::endl << "FILE NAME: " << fileName<< "**" << std::endl;
	// default analysis setting
	inp << "*PREPRINT,MODEL=NO,HISTORY=NO,ECHO=NO" << std::endl << "**" << std::endl;

	// -- PART -- //
	inp << "*Part, name=ROBOT_ARM" << std::endl;
	// node definition
	inp << "*NODE" << std::endl;
	for(int i = 0; i < numNode; i++){
		inp << i+1 << ", " << node[i][0] << ", " << node[i][1] << ", " << node[i][2] << std::endl;
	}
	inp << "**" << std::endl;
	// element definition set for each element
	inp << "** MATERIALS" << std::endl << "**" << std::endl;
	for(int i = 0; i < numEle; i++){
		inp << "*ELEMENT,ELSET=ELE" << i + 1 << ",TYPE=B31" << std::endl;
		inp << i+1 << "," << element[i][0] << "," << element[i][1] << std::endl;
	}
	// give a set to the whole structure
	inp << "*Elset, elset=WHOLE_ARM, generate" << std::endl <<
			"1, " << numEle << ", 1" << std::endl;
	inp << "**" << std::endl;


	// -- SECTION -- //
	for(int i = 0; i < numEle; i++){
		inp << "** Section: Section_ELE" << i + 1 << " Profile: circle" << i + 1 << std::endl;
		double dx = node[element[i][0]-1][0] - node[element[i][1]-1][0];
		double dy = node[element[i][0]-1][1] - node[element[i][1]-1][1];
		double dz = node[element[i][0]-1][2] - node[element[i][1]-1][2];
		inp << "*Beam Section, elset=ELE" << i + 1 << ", material=ALUMINUM, temperature=GRADIENTS, section=CIRC" << std::endl <<
				// radius[i] << std::endl << dx << "," << dy << "," << dz << std::endl;
				radius[i] << std::endl << "0.123, 0.456, 0.789" << std::endl;
		inp << "**" << std::endl;
	}
	inp << "*End Part" << std::endl << "**" << std::endl;

	// -- ASSEMBLY -- //
	inp << "*Assembly, name=Assembly" << std::endl << "**" << std::endl;
	inp << "*Instance, name=ROBOT_ARM_1, part=ROBOT_ARM" << std::endl <<
			"*End Instance" << std::endl << "**" << std::endl;
	for(int i = 0; i < numNode; i++){
		inp << "*Nset, nset=NODE" << i+1 << 
			", instance=ROBOT_ARM_1" << std::endl <<
			" " << i+1 << "," << std::endl;
	}
	inp << "*End Assembly" << std::endl;

	// -- MATERIALS -- //
	inp << "**" << std::endl;
	inp << "** MATERIALS" << std::endl << "**" << std::endl;
	inp << "*Material, name=ALUMINUM" << std::endl <<
			"*Density" << std::endl << " " << density << "," << std::endl <<
			"*Elastic" << std::endl << " " << modulus << "," << poisson << std::endl;
	inp << "**" << std::endl;

	// -- BOUNDARY CONDITIONS -- //
	inp << "** BOUNDARY CONDITIONS **" << std::endl;
	inp << "**" << std::endl;
	inp << "** " << std::endl;
	for(int i = 0; i < numNodeBC; i++){
		inp << "** Name: BC-" << i+1 << " Type: Displacement/Rotation" << std::endl;
		inp << "*Boundary" << std::endl;
		inp << "NODE" << indexNodeBC[i]+1 << ", 1, 1" << std::endl << 
			 "NODE" << indexNodeBC[i]+1 << ", 2, 2" << std::endl <<
			 "NODE" << indexNodeBC[i]+1 << ", 3, 3" << std::endl <<
			 "NODE" << indexNodeBC[i]+1 << ", 4, 4" << std::endl <<
			 "NODE" << indexNodeBC[i]+1 << ", 5, 5" << std::endl <<
			 "NODE" << indexNodeBC[i]+1 << ", 6, 6" << std::endl;
	}
	inp << "** -------------------------------------------------------------------" << std::endl << "**" << std::endl;

	// -- STEP -- //
	inp << "** STEP: Step-1" << std::endl << "**" << std::endl <<
			"*Step, name=Step-1, nlgeom=NO" << std::endl << "*Static" << std::endl <<
			"1., 1., 1e-05, 1." << std::endl <<
			"**" << std::endl <<
			"** LOADS" << std::endl <<
			"**" << std::endl;
	for(int i = 0; i < numNodeF; i++){
		inp << "** Name: Load-" << i+1 << " Type: Concentrated force" << std::endl <<
				"*Cload" << std::endl;
		for(int j = 0; j < dimF; j++){
			inp << "NODE" << indexNodeF[i]+1 << ", " << j+1 << ", " << nodeF[i][j] << std::endl;
		}
		inp << "**" << std::endl;
	}
	inp << "*End Step" << std::endl;

	inp.close();
}

int main(int argc, char *argv[]){

	if(argc < 3){
		std::cout << "Usage: ./smf2inp <inputFolder> <loadCase No.>" << std::endl;
		std::cout << "       <inputFolder>  put in './data/'" << std::endl;
		std::cout << "                      geometry as 'model.smf', beam size as 'radius.dat'" << std::endl;
		std::cout << "       <loadCase No.> put in './data/'" << std::endl;
		std::cout << "                      as f*.txt" << std::endl;
		exit(1);
	}

	std::cout << dual_line << " == Convert smf file of frame to ABAQUS Inp file ==" << dual_line;

	abaqusScript(argv[1],argv[2]);
	std::cout << " = Inp file completed =" << dual_line;
	return 0;
}


