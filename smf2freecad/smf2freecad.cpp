#include <stdlib>
#include <iomanip>
#include <vector>
#include <cstring>
#include <iostream>
#include <fstream>

int main(int argc, char *argv[]){

	if(argc < 5){
		std::cout << "Usage: ./smf2freecad <inputFolder> <cylinderRadiusFactor> <sphereRadiusFactor> <mode>" << std::endl;
		std::cout << "      <inputFolder> put in './data/'" << std::endl;
		std::cout << "                    geometry as 'model.smf', cylinder size as 'radius.dat'" << std::endl;
		std::cout << "      <mode>        0 all loft, no flat edge" << std::endl;
		std::cout << "      <mode>        1 all loft, flat edge" << std::endl;
		std::cout << "      <mode>        2 all loft, no flat edge" << std::endl;
	}

	std::string dir1 = argv[1];
	std::string factorString1 = argv[2];
	std::string factorString2 = argv[3];
	std::string mode = argv[4];

	const double defaultRadius = 80.;
	const int debug = 0;
	const double factor1 = atof(factorString1.c_str());
	const double factor2 = atof(factorString2.c_str());


	std::string dir = "./" + dir1 + "/";

	std::string smfDir = dir + "model.smf";
	std::string rDir = dir + "radius.dat";

	// open model file
	std::string testline;
	std::ifstream smfFile; smfFile.open(smfDir.c_str());
	if(smfFile.fail()){
		std::cout << "* ERROR: NO input model file" << std::endl;
		exit(1);
	}

	// read node coordinates
	for(int i = 0; i < 6; i++){
		smfFile >> testline;
	}
	smfFile >> testline; const int nodeNum = atof(testline.c_str());
	smfFile >> testline; const int eleNum = atof(testline.c_str());
	std::cout << "  * Node Number = " << nodeNum << " Element Number = " << eleNum << std::endl;
	std::vector< std::vector<double> > node(nodeNum,std::vector<double>(3));
	if(debug == 1) std::cout << std::endl;
	for(int indexNode = 0; indexNode < nodeNum; indexNode++){
		if(debug == 1) std::cout << "    -> ";
		for(int indexDim = 0; indexDim < 3; indexDim++){
			smfFile >> testline;
			node[indexNode][indexDim] = atof(testline.c_str());
			if(debug == 1) std::cout << node[indexNode][indexDim] << " ";
		}
		if(debug == 1) std::cout << std::endl;
	}

	// read element connections
	std::vector< std::vector<int> > ele(eleNum,std::vector<int>(2));
	if(debug == 1) std::cout << std::endl;
	if(debug == 1) std::cout << "  => Connetctions " << std::endl;
	for(int indexEle = 0; indexEle < eleNum; indexEle++){
		if(debug == 1) std::cout << "    -> ";
		for(int indexDim = 0; indexDim < 2; indexDim++){
			smfFile >> testline;
			ele[indexEle][indexDim] = atof(testline.c_str());
			if(debug == 1) std::cout << ele[indexEle][indexDim] << " ";
		}
		if(debug == 1) std::cout << std::endl;
	}

	smfFile.close();

	// open radius file
	std::vector<double> radiusEle(eleNum);
	std::ifstream rFile; rFile.open(rDir.c_str());
	if(rFile.fail()){
		std::cout << "  -> NO input radius file, set radius as default" << std::endl;
		std::fill(radiusEle.begin(), radiusEle.end(), defaultRadius);
	}
	else{
		for(int indexEle = 0; indexEle < eleNum; indexEle++){
			rFile >> testline;
			radiusEle[indexEle] = atof(testline.c_str());
		}
	}
	rFile.close();

	// locate which element connected to one node
	std::vector<Component> nodeLink;
	if(debug == 1) std::cout << "Node Link: " << std::endl;
	for(int indexNode = 0; indexNode < nodeNum; indexNode++){
		std::vector<int> tempLink;
		if(debug == 1) std::cout << "  -> Now checking Node " << indexNode << " shared by";
		for(int indexEle = 0; indexEle < eleNum; indexEle++){
			for(int indexDim = 0; indexDim < 2; indexDim++){
				if(ele[indexEle][indexDim] == indexNode){
					tempLink.push_back(indexEle);
					if(debug == 1) std::cout << " " << indexEle << "(" << radiusEle[indexEle] << ")";
				}
			}
		}
		if(debug == 1) std::cout << std::endl;
		Component* it = new Component(tempLink);
		nodeLink.push_back(*it);
		tempLink.clear();
	}
	if(debug == 1) std::cout << "============================" << std::endl;

	std::vector<double> radiusNode(nodeNum);
	if(debug == 1) std::cout << "Radius for nodes: " << std::endl;
	for(int indexNode = 0; indexNode < nodeNum; indexNode++){
		if(debug == 1) std::cout << "  -> Now Node " << indexNode << " ";
		const int numSharingEle = nodeLink[indexNode].giveComponent().size();
		double maxR = 0;
		for(int indexDim = 0; indexDim < numSharingEle; indexDim++){
			int indexSharingEle = nodeLink[indexNode].giveComponent()[indexDim];
			if(radiusEle[indexSharingEle] > maxR){
				maxR = radiusEle[indexSharingEle];
			}
		}
		radiusNode[indexNode] = maxR;
		if(debug == 1) std::cout << "Radius" << maxR << ": ";
	}

	std::vector<FreeCADBall> balls;
	for(int indexNode = 0; indexNode < nodeNum; indexNode++){
		//if(nodeLink[indexNode].giveComponent().size() > 2){	// junction point and end point
		std::vector<double> centre = node[indexNode];
		double radius = radiusNode[indexNode];
		FreeCADBall *it = new FreeCADBall(centre,radius);
		balls.push_back(*it);
	}

	// now, script
	std::string scriptDir = dir + "script.py";
	std::ofstream sFile; sFile.open(scriptDir.c_str());
	// first, script lofting things
	sFile << "from FreeCAD import Base" << std::endl << "import Part" << std::endl << "App.newDocument(\"test\")" << std::endl;
	for(int indexEle = 0; indexEle < eleNum; indexEle++){
		int point1Index = ele[indexEle][0];
		int point2Index = ele[indexEle][1];

		std::vector<double> point1 = node[point1Index];
		std::vector<double> point2 = node[point2Index];

		double radius1 = sqrt(radiusNode[point1Index]/3.1415926);
		double radius2 = sqrt(radiusNode[point2Index]/3.1415926);

		std::vector<double> gradient(3);
		gradient[0] = point2[0] - point1[0];
		gradient[1] = point2[1] - point1[1];
		gradient[2] = point2[2] - point1[2];
		double length = sqrt(gradient[0]*gradient[0] + gradient[1]*gradient[1] + gradient[2]*gradient[2]);
		gradient[0] /= length; gradient[1] /= length; gradient[2] /= length;
		if(mode == "0"){
			sFile << "circle1 = Part.makeCircle(" << radius1*factor1 << ",Base.Vector(" << point1[0] << "," << point1[1] << "," << point1[2] <<
					"),Base.Vector(" << gradient[0] << "," << gradient[1] << "," << gradient[2] << "),0,360)" << std::endl;
			sFile << "circle2 = Part.makeCircle(" << radius2*factor1 << ",Base.Vector(" << point2[0] << "," << point2[1] << "," << point2[2] <<
					"),Base.Vector(" << gradient[0] << "," << gradient[1] << "," << gradient[2] << "),0,360)" << std::endl;
			sFile << "section = []" << std::endl << "section.append(circle1)" << std::endl << "section.append(circle2)" << std::endl;
			sFile << "loft" << indexEle << " = Part.makeLoft(section,True)" << std::endl << "section.remove" << std::endl;
			sFile << "Loft" << indexEle << " = FreeCAD.ActiveDocument.addObject(\"Part::Loft\",\"Loft" << indexEle<< "\")" << std::endl <<
					"loft" << indexEle << "= Part.makeLoft(section,True)" << std::endl <<
					"Loft" << indexEle << ".Shape = loft" << indexEle << std::endl <<
					"section.remove" << std::endl;
			//sFile << "Part.show(loft" << indexEle << ")" << std::endl;
		}
		if(mode == "1"){
			if(point1[1] < 183 && point1[1] > 180)
				sFile << "circle" << indexEle << indexEle << "1 = Part.makeCircle(" << radius1*factor1 << ",Base.Vector(" << point1[0] << "," << point1[1] << "," << point1[2] <<
				"),Base.Vector(0,-1,0),0,360)" << std::endl;
			else if(point1[1] < 3 && point1[1] > -3)
				sFile << "circle" << indexEle << indexEle << "1 = Part.makeCircle(" << radius1*factor1 << ",Base.Vector(" << point1[0] << "," << point1[1] << "," << point1[2] <<
				"),Base.Vector(0,1,0),0,360)" << std::endl;
			else
				sFile << "circle" << indexEle << indexEle << "1 = Part.makeCircle(" << radius1*factor1 << ",Base.Vector(" << point1[0] << "," << point1[1] << "," << point1[2] <<
				"),Base.Vector(" << gradient[0] << "," << gradient[1] << "," << gradient[2] << "),0,360)" << std::endl;

			if(point2[1] < 183 && point2[1] > 180)
				sFile << "circle" << indexEle << indexEle << "2 = Part.makeCircle(" << radius2*factor1 << ",Base.Vector(" << point2[0] << "," << point2[1] << "," << point2[2] <<
				"),Base.Vector(0,1,0),0,360)" << std::endl;
			else if(point2[1] < 3 && point2[1] > -3)
				sFile << "circle" << indexEle << indexEle << "2 = Part.makeCircle(" << radius2*factor1 << ",Base.Vector(" << point2[0] << "," << point2[1] << "," << point2[2] <<
				"),Base.Vector(0,-1,0),0,360)" << std::endl;
			else
				sFile << "circle" << indexEle << indexEle << "2 = Part.makeCircle(" << radius2*factor1 << ",Base.Vector(" << point2[0] << "," << point2[1] << "," << point2[2] <<
				"),Base.Vector(" << gradient[0] << "," << gradient[1] << "," << gradient[2] << "),0,360)" << std::endl;

			sFile << "section = []" << std::endl << "section.append(circle" << indexEle << indexEle << "1)" << std::endl <<
					"section.append(circle" << indexEle << indexEle << "2)" << std::endl;
			sFile << "loft" << indexEle << " = Part.makeLoft(section,True,False)" << std::endl;
			sFile << "Loft" << indexEle << " = FreeCAD.ActiveDocument.addObject(\"Part::Loft\",\"Loft" << indexEle<< "\")" << std::endl <<
					"loft" << indexEle << "= Part.makeLoft(section,True)" << std::endl <<
					"Loft" << indexEle << ".Shape = loft" << indexEle << std::endl <<
					"section.remove" << std::endl;
			sFile << "Part.show(loft" << indexEle << ")" << std::endl;
			sFile << "App.getDocument(\"test\").removeObject(\"Loft" << indexEle << "\")" << std::endl;
		}
		else if(mode == "2"){
			sFile << "Cyn" << indexEle << " = FreeCAD.ActiveDocument.addObject(\"Part::Cylinder\",\"Cylinder" << indexEle << "\")" << std::endl;
			sFile << "cylinder" << indexEle << " = Part.makeCylinder(" << sqrt(radiusEle[indexEle]/3.1415926)*factor1 << "," << length <<
					",Base.Vector(" << point1[0] << "," << point1[1] << "," << point1[2] <<
					"),Base.Vector(" << gradient[0]*length << "," << gradient[1]*length << "," << gradient[2]*length << "),360)" << std::endl;
			sFile << "Cyn" << indexEle << ".Shape = cylinder" << indexEle << std::endl;
			sFile << "Part.show(cylinder" << indexEle << ")" << std::endl;
			sFile << "App.getDocument(\"test\").removeObject(\"Cylinder" << indexEle << "\")" << std::endl;
		}
	}

	//second, place balls
	for(int indexBall = 0; indexBall < balls.size(); indexBall++){
		std::vector<double> centre = balls[indexBall].giveCentre();
		double radius = balls[indexBall].giveRadius();
		sFile << "Sphere" << indexBall << " = FreeCAD.ActiveDocument.addObject(\"Part::Sphere\",\"Sphere" << indexBall << "\")" << std::endl <<
				"ball" << indexBall << " = Part.makeSphere(" << sqrt(radius/3.1415926)*factor2 << ")" << std::endl;
		sFile << "ball" << indexBall << ".translate(Base.Vector(" << centre[0] << "," << centre[1] << "," << centre[2] << "))" << std::endl;
		sFile << "Sphere" << indexBall << ".Shape = ball" << indexBall << std::endl;

		sFile << "Part.show(ball" << indexBall << ")" << std::endl;
		sFile << "App.getDocument(\"test\").removeObject(\"Sphere" << indexBall << "\")" << std::endl;
	}

	sFile << "Gui.SendMsgToActiveView(\"ViewFit\")" << std::endl;
	sFile << std::endl;


	std::cout << "  -> Script done" << std::endl;
	sFile.close();

	return 0;
}

