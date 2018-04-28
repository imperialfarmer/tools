from FreeCAD import Base
import Part
App.newDocument("test")
circle1 = Part.makeCircle(4,Base.Vector(-35.5,262.5,86.5),Base.Vector(0,0,-15),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-35.5,262.5,71.5),Base.Vector(0,0,-15),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft0 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft0")
loft0= Part.makeLoft(section,True)
Loft0.Shape = loft0
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-35.5,262.5,86.5),Base.Vector(3,-21,6),0,360)
circle2 = Part.makeCircle(4.58705,Base.Vector(-32.5,241.5,92.5),Base.Vector(3,-21,6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft1 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft1")
loft1= Part.makeLoft(section,True)
Loft1.Shape = loft1
section.remove
circle1 = Part.makeCircle(4.55966,Base.Vector(-31.75,224.25,95.5),Base.Vector(-0.75,17.25,-3),0,360)
circle2 = Part.makeCircle(4.58705,Base.Vector(-32.5,241.5,92.5),Base.Vector(-0.75,17.25,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft2 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft2")
loft2= Part.makeLoft(section,True)
Loft2.Shape = loft2
section.remove
circle1 = Part.makeCircle(4.55966,Base.Vector(-31.75,224.25,95.5),Base.Vector(-3.75,38.25,-24),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-35.5,262.5,71.5),Base.Vector(-3.75,38.25,-24),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft3 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft3")
loft3= Part.makeLoft(section,True)
Loft3.Shape = loft3
section.remove
circle1 = Part.makeCircle(4.55966,Base.Vector(-31.75,224.25,95.5),Base.Vector(5.25,-17.25,-4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-26.5,207,91),Base.Vector(5.25,-17.25,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft4 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft4")
loft4= Part.makeLoft(section,True)
Loft4.Shape = loft4
section.remove
circle1 = Part.makeCircle(4.58705,Base.Vector(-32.5,241.5,92.5),Base.Vector(9,6,-6),0,360)
circle2 = Part.makeCircle(6.3477,Base.Vector(-23.5,247.5,86.5),Base.Vector(9,6,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft5 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft5")
loft5= Part.makeLoft(section,True)
Loft5.Shape = loft5
section.remove
circle1 = Part.makeCircle(4.55966,Base.Vector(-31.75,224.25,95.5),Base.Vector(11.25,-9.75,0),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-20.5,214.5,95.5),Base.Vector(11.25,-9.75,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft6 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft6")
loft6= Part.makeLoft(section,True)
Loft6.Shape = loft6
section.remove
circle1 = Part.makeCircle(4.55966,Base.Vector(-31.75,224.25,95.5),Base.Vector(20.25,0.75,-4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-11.5,225,91),Base.Vector(20.25,0.75,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft7 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft7")
loft7= Part.makeLoft(section,True)
Loft7.Shape = loft7
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-26.5,207,91),Base.Vector(23.25,-8.25,1.5),0,360)
circle2 = Part.makeCircle(5.62268,Base.Vector(-3.25,198.75,92.5),Base.Vector(23.25,-8.25,1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft8 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft8")
loft8= Part.makeLoft(section,True)
Loft8.Shape = loft8
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-26.5,207,91),Base.Vector(6,4.5,-19.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-20.5,211.5,71.5),Base.Vector(6,4.5,-19.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft9 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft9")
loft9= Part.makeLoft(section,True)
Loft9.Shape = loft9
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-26.5,207,91),Base.Vector(6,7.5,4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-20.5,214.5,95.5),Base.Vector(6,7.5,4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft10 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft10")
loft10= Part.makeLoft(section,True)
Loft10.Shape = loft10
section.remove
circle1 = Part.makeCircle(6.3477,Base.Vector(-23.5,247.5,86.5),Base.Vector(12,-12,-6),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,235.5,80.5),Base.Vector(12,-12,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft11 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft11")
loft11= Part.makeLoft(section,True)
Loft11.Shape = loft11
section.remove
circle1 = Part.makeCircle(6.3477,Base.Vector(-23.5,247.5,86.5),Base.Vector(-3,15,-12),0,360)
circle2 = Part.makeCircle(7.85803,Base.Vector(-26.5,262.5,74.5),Base.Vector(-3,15,-12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft12 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft12")
loft12= Part.makeLoft(section,True)
Loft12.Shape = loft12
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-20.5,211.5,71.5),Base.Vector(9,-15,-6),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,196.5,65.5),Base.Vector(9,-15,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft13 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft13")
loft13= Part.makeLoft(section,True)
Loft13.Shape = loft13
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-20.5,211.5,71.5),Base.Vector(9,24,9),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,235.5,80.5),Base.Vector(9,24,9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft14 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft14")
loft14= Part.makeLoft(section,True)
Loft14.Shape = loft14
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-20.5,214.5,95.5),Base.Vector(9,10.5,-4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-11.5,225,91),Base.Vector(9,10.5,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft15 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft15")
loft15= Part.makeLoft(section,True)
Loft15.Shape = loft15
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-17.5,121.5,32.5),Base.Vector(9.75,-7.5,17.25),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-7.75,114,49.75),Base.Vector(9.75,-7.5,17.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft16 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft16")
loft16= Part.makeLoft(section,True)
Loft16.Shape = loft16
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-17.5,121.5,32.5),Base.Vector(3,22.5,-42),0,360)
circle2 = Part.makeCircle(8.92186,Base.Vector(-14.5,144,-9.5),Base.Vector(3,22.5,-42),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft17 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft17")
loft17= Part.makeLoft(section,True)
Loft17.Shape = loft17
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-17.5,121.5,32.5),Base.Vector(5.25,44.25,2.25),0,360)
circle2 = Part.makeCircle(8.21222,Base.Vector(-12.25,165.75,34.75),Base.Vector(5.25,44.25,2.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft18 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft18")
loft18= Part.makeLoft(section,True)
Loft18.Shape = loft18
section.remove
circle1 = Part.makeCircle(7.76068,Base.Vector(-14.5,133.5,-18.5),Base.Vector(0,10.5,9),0,360)
circle2 = Part.makeCircle(8.92186,Base.Vector(-14.5,144,-9.5),Base.Vector(0,10.5,9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft19 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft19")
loft19= Part.makeLoft(section,True)
Loft19.Shape = loft19
section.remove
circle1 = Part.makeCircle(7.76068,Base.Vector(-14.5,133.5,-18.5),Base.Vector(3,-36,-24),0,360)
circle2 = Part.makeCircle(9.99705,Base.Vector(-11.5,97.5,-42.5),Base.Vector(3,-36,-24),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft20 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft20")
loft20= Part.makeLoft(section,True)
Loft20.Shape = loft20
section.remove
circle1 = Part.makeCircle(7.76068,Base.Vector(-14.5,133.5,-18.5),Base.Vector(0,10.5,-15.75),0,360)
circle2 = Part.makeCircle(4.35996,Base.Vector(-14.5,144,-34.25),Base.Vector(0,10.5,-15.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft21 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft21")
loft21= Part.makeLoft(section,True)
Loft21.Shape = loft21
section.remove
circle1 = Part.makeCircle(4.35996,Base.Vector(-14.5,144,-34.25),Base.Vector(27,-28.5,-11.25),0,360)
circle2 = Part.makeCircle(4,Base.Vector(12.5,115.5,-45.5),Base.Vector(27,-28.5,-11.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft22 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft22")
loft22= Part.makeLoft(section,True)
Loft22.Shape = loft22
section.remove
circle1 = Part.makeCircle(4.35996,Base.Vector(-14.5,144,-34.25),Base.Vector(0,15,-2.25),0,360)
circle2 = Part.makeCircle(4.35996,Base.Vector(-14.5,159,-36.5),Base.Vector(0,15,-2.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft23 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft23")
loft23= Part.makeLoft(section,True)
Loft23.Shape = loft23
section.remove
circle1 = Part.makeCircle(8.92186,Base.Vector(-14.5,144,-9.5),Base.Vector(0,22.5,24),0,360)
circle2 = Part.makeCircle(8.92186,Base.Vector(-14.5,166.5,14.5),Base.Vector(0,22.5,24),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft24 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft24")
loft24= Part.makeLoft(section,True)
Loft24.Shape = loft24
section.remove
circle1 = Part.makeCircle(8.92186,Base.Vector(-14.5,166.5,14.5),Base.Vector(2.25,-0.75,20.25),0,360)
circle2 = Part.makeCircle(8.21222,Base.Vector(-12.25,165.75,34.75),Base.Vector(2.25,-0.75,20.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft25 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft25")
loft25= Part.makeLoft(section,True)
Loft25.Shape = loft25
section.remove
circle1 = Part.makeCircle(8.92186,Base.Vector(-14.5,166.5,14.5),Base.Vector(12,28.5,-9),0,360)
circle2 = Part.makeCircle(7.52885,Base.Vector(-2.5,195,5.5),Base.Vector(12,28.5,-9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft26 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft26")
loft26= Part.makeLoft(section,True)
Loft26.Shape = loft26
section.remove
circle1 = Part.makeCircle(8.21222,Base.Vector(-12.25,165.75,34.75),Base.Vector(9.75,29.25,-29.25),0,360)
circle2 = Part.makeCircle(7.52885,Base.Vector(-2.5,195,5.5),Base.Vector(9.75,29.25,-29.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft27 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft27")
loft27= Part.makeLoft(section,True)
Loft27.Shape = loft27
section.remove
circle1 = Part.makeCircle(9.99705,Base.Vector(-11.5,97.5,-42.5),Base.Vector(-3,-15,-3),0,360)
circle2 = Part.makeCircle(9.99705,Base.Vector(-14.5,82.5,-45.5),Base.Vector(-3,-15,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft28 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft28")
loft28= Part.makeLoft(section,True)
Loft28.Shape = loft28
section.remove
circle1 = Part.makeCircle(9.99705,Base.Vector(-11.5,97.5,-42.5),Base.Vector(24,18,-3),0,360)
circle2 = Part.makeCircle(4,Base.Vector(12.5,115.5,-45.5),Base.Vector(24,18,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft29 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft29")
loft29= Part.makeLoft(section,True)
Loft29.Shape = loft29
section.remove
circle1 = Part.makeCircle(8.21222,Base.Vector(-12.25,165.75,34.75),Base.Vector(0.75,-2.25,18.75),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,163.5,53.5),Base.Vector(0.75,-2.25,18.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft30 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft30")
loft30= Part.makeLoft(section,True)
Loft30.Shape = loft30
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,163.5,53.5),Base.Vector(3,-33,3),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-8.5,130.5,56.5),Base.Vector(3,-33,3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft31 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft31")
loft31= Part.makeLoft(section,True)
Loft31.Shape = loft31
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,163.5,53.5),Base.Vector(6,18,16.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-5.5,181.5,70),Base.Vector(6,18,16.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft32 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft32")
loft32= Part.makeLoft(section,True)
Loft32.Shape = loft32
section.remove
circle1 = Part.makeCircle(4.35996,Base.Vector(-14.5,159,-36.5),Base.Vector(37.5,36,4.5),0,360)
circle2 = Part.makeCircle(5.10432,Base.Vector(23,195,-32),Base.Vector(37.5,36,4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft33 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft33")
loft33= Part.makeLoft(section,True)
Loft33.Shape = loft33
section.remove
circle1 = Part.makeCircle(8.21222,Base.Vector(-12.25,165.75,34.75),Base.Vector(12.75,32.25,0.75),0,360)
circle2 = Part.makeCircle(6.87477,Base.Vector(0.5,198,35.5),Base.Vector(12.75,32.25,0.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft34 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft34")
loft34= Part.makeLoft(section,True)
Loft34.Shape = loft34
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,196.5,65.5),Base.Vector(27,3.75,-25.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(15.5,200.25,40),Base.Vector(27,3.75,-25.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft35 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft35")
loft35= Part.makeLoft(section,True)
Loft35.Shape = loft35
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-11.5,225,91),Base.Vector(8.25,-26.25,1.5),0,360)
circle2 = Part.makeCircle(5.62268,Base.Vector(-3.25,198.75,92.5),Base.Vector(8.25,-26.25,1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft36 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft36")
loft36= Part.makeLoft(section,True)
Loft36.Shape = loft36
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-11.5,225,91),Base.Vector(0,10.5,-10.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,235.5,80.5),Base.Vector(0,10.5,-10.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft37 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft37")
loft37= Part.makeLoft(section,True)
Loft37.Shape = loft37
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,235.5,80.5),Base.Vector(0,27,-6),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,262.5,74.5),Base.Vector(0,27,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft38 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft38")
loft38= Part.makeLoft(section,True)
Loft38.Shape = loft38
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-7.75,114,49.75),Base.Vector(-0.75,16.5,6.75),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-8.5,130.5,56.5),Base.Vector(-0.75,16.5,6.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft39 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft39")
loft39= Part.makeLoft(section,True)
Loft39.Shape = loft39
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-8.5,130.5,56.5),Base.Vector(33,-18,0),0,360)
circle2 = Part.makeCircle(5.8377,Base.Vector(24.5,112.5,56.5),Base.Vector(33,-18,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft40 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft40")
loft40= Part.makeLoft(section,True)
Loft40.Shape = loft40
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-7.75,114,49.75),Base.Vector(5.25,-10.5,3.75),0,360)
circle2 = Part.makeCircle(9.97843,Base.Vector(-2.5,103.5,53.5),Base.Vector(5.25,-10.5,3.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft41 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft41")
loft41= Part.makeLoft(section,True)
Loft41.Shape = loft41
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-5.5,181.5,70),Base.Vector(15,18,-7.5),0,360)
circle2 = Part.makeCircle(4.64611,Base.Vector(9.5,199.5,62.5),Base.Vector(15,18,-7.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft42 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft42")
loft42= Part.makeLoft(section,True)
Loft42.Shape = loft42
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-5.5,181.5,70),Base.Vector(9,3,18),0,360)
circle2 = Part.makeCircle(5.86684,Base.Vector(3.5,184.5,88),Base.Vector(9,3,18),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft43 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft43")
loft43= Part.makeLoft(section,True)
Loft43.Shape = loft43
section.remove
circle1 = Part.makeCircle(9.97843,Base.Vector(-2.5,103.5,53.5),Base.Vector(27,9,3),0,360)
circle2 = Part.makeCircle(5.8377,Base.Vector(24.5,112.5,56.5),Base.Vector(27,9,3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft44 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft44")
loft44= Part.makeLoft(section,True)
Loft44.Shape = loft44
section.remove
circle1 = Part.makeCircle(9.97843,Base.Vector(-2.5,103.5,53.5),Base.Vector(-6,-21,-9),0,360)
circle2 = Part.makeCircle(9.29645,Base.Vector(-8.5,82.5,44.5),Base.Vector(-6,-21,-9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft45 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft45")
loft45= Part.makeLoft(section,True)
Loft45.Shape = loft45
section.remove
circle1 = Part.makeCircle(7.52885,Base.Vector(-2.5,195,5.5),Base.Vector(25.5,0,-37.5),0,360)
circle2 = Part.makeCircle(5.10432,Base.Vector(23,195,-32),Base.Vector(25.5,0,-37.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft46 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft46")
loft46= Part.makeLoft(section,True)
Loft46.Shape = loft46
section.remove
circle1 = Part.makeCircle(5.62268,Base.Vector(-3.25,198.75,92.5),Base.Vector(6.75,-14.25,-4.5),0,360)
circle2 = Part.makeCircle(5.86684,Base.Vector(3.5,184.5,88),Base.Vector(6.75,-14.25,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft47 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft47")
loft47= Part.makeLoft(section,True)
Loft47.Shape = loft47
section.remove
circle1 = Part.makeCircle(5.62268,Base.Vector(-3.25,198.75,92.5),Base.Vector(21.75,30.75,-19.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(18.5,229.5,73),Base.Vector(21.75,30.75,-19.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft48 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft48")
loft48= Part.makeLoft(section,True)
Loft48.Shape = loft48
section.remove
circle1 = Part.makeCircle(7.52885,Base.Vector(-2.5,195,5.5),Base.Vector(17.25,4.5,13.875),0,360)
circle2 = Part.makeCircle(7.95985,Base.Vector(14.75,199.5,19.375),Base.Vector(17.25,4.5,13.875),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft49 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft49")
loft49= Part.makeLoft(section,True)
Loft49.Shape = loft49
section.remove
circle1 = Part.makeCircle(6.87477,Base.Vector(0.5,198,35.5),Base.Vector(15,2.25,4.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(15.5,200.25,40),Base.Vector(15,2.25,4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft50 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft50")
loft50= Part.makeLoft(section,True)
Loft50.Shape = loft50
section.remove
circle1 = Part.makeCircle(5.62268,Base.Vector(-3.25,198.75,92.5),Base.Vector(15.75,18.75,0),0,360)
circle2 = Part.makeCircle(4.48275,Base.Vector(12.5,217.5,92.5),Base.Vector(15.75,18.75,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft51 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft51")
loft51= Part.makeLoft(section,True)
Loft51.Shape = loft51
section.remove
circle1 = Part.makeCircle(6.87477,Base.Vector(0.5,198,35.5),Base.Vector(14.25,1.5,-16.125),0,360)
circle2 = Part.makeCircle(7.95985,Base.Vector(14.75,199.5,19.375),Base.Vector(14.25,1.5,-16.125),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft52 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft52")
loft52= Part.makeLoft(section,True)
Loft52.Shape = loft52
section.remove
circle1 = Part.makeCircle(5.86684,Base.Vector(3.5,184.5,88),Base.Vector(27,15,-28.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(30.5,199.5,59.5),Base.Vector(27,15,-28.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft53 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft53")
loft53= Part.makeLoft(section,True)
Loft53.Shape = loft53
section.remove
circle1 = Part.makeCircle(5.86684,Base.Vector(3.5,184.5,88),Base.Vector(6,15,-25.5),0,360)
circle2 = Part.makeCircle(4.64611,Base.Vector(9.5,199.5,62.5),Base.Vector(6,15,-25.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft54 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft54")
loft54= Part.makeLoft(section,True)
Loft54.Shape = loft54
section.remove
circle1 = Part.makeCircle(4.64611,Base.Vector(9.5,199.5,62.5),Base.Vector(21,24,9),0,360)
circle2 = Part.makeCircle(10,Base.Vector(30.5,223.5,71.5),Base.Vector(21,24,9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft55 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft55")
loft55= Part.makeLoft(section,True)
Loft55.Shape = loft55
section.remove
circle1 = Part.makeCircle(4,Base.Vector(12.5,115.5,-45.5),Base.Vector(49.5,37.5,-3),0,360)
circle2 = Part.makeCircle(4.85043,Base.Vector(62,153,-48.5),Base.Vector(49.5,37.5,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft56 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft56")
loft56= Part.makeLoft(section,True)
Loft56.Shape = loft56
section.remove
circle1 = Part.makeCircle(4.48275,Base.Vector(12.5,217.5,92.5),Base.Vector(12,6,0),0,360)
circle2 = Part.makeCircle(4,Base.Vector(24.5,223.5,92.5),Base.Vector(12,6,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft57 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft57")
loft57= Part.makeLoft(section,True)
Loft57.Shape = loft57
section.remove
circle1 = Part.makeCircle(4.48275,Base.Vector(12.5,217.5,92.5),Base.Vector(3,15,-1.5),0,360)
circle2 = Part.makeCircle(4.58657,Base.Vector(15.5,232.5,91),Base.Vector(3,15,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft58 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft58")
loft58= Part.makeLoft(section,True)
Loft58.Shape = loft58
section.remove
circle1 = Part.makeCircle(7.95985,Base.Vector(14.75,199.5,19.375),Base.Vector(15.75,-9,-16.875),0,360)
circle2 = Part.makeCircle(6.45669,Base.Vector(30.5,190.5,2.5),Base.Vector(15.75,-9,-16.875),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft59 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft59")
loft59= Part.makeLoft(section,True)
Loft59.Shape = loft59
section.remove
circle1 = Part.makeCircle(7.95985,Base.Vector(14.75,199.5,19.375),Base.Vector(0.75,0.75,20.625),0,360)
circle2 = Part.makeCircle(10,Base.Vector(15.5,200.25,40),Base.Vector(0.75,0.75,20.625),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft60 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft60")
loft60= Part.makeLoft(section,True)
Loft60.Shape = loft60
section.remove
circle1 = Part.makeCircle(10,Base.Vector(18.5,229.5,73),Base.Vector(-3,3,18),0,360)
circle2 = Part.makeCircle(4.58657,Base.Vector(15.5,232.5,91),Base.Vector(-3,3,18),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft61 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft61")
loft61= Part.makeLoft(section,True)
Loft61.Shape = loft61
section.remove
circle1 = Part.makeCircle(4.58657,Base.Vector(15.5,232.5,91),Base.Vector(9,-9,1.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(24.5,223.5,92.5),Base.Vector(9,-9,1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft62 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft62")
loft62= Part.makeLoft(section,True)
Loft62.Shape = loft62
section.remove
circle1 = Part.makeCircle(4.58657,Base.Vector(15.5,232.5,91),Base.Vector(6,13.5,-3),0,360)
circle2 = Part.makeCircle(4.35493,Base.Vector(21.5,246,88),Base.Vector(6,13.5,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft63 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft63")
loft63= Part.makeLoft(section,True)
Loft63.Shape = loft63
section.remove
circle1 = Part.makeCircle(10,Base.Vector(15.5,200.25,40),Base.Vector(15,-0.75,19.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(30.5,199.5,59.5),Base.Vector(15,-0.75,19.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft64 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft64")
loft64= Part.makeLoft(section,True)
Loft64.Shape = loft64
section.remove
circle1 = Part.makeCircle(10,Base.Vector(18.5,229.5,73),Base.Vector(12,-6,-1.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(30.5,223.5,71.5),Base.Vector(12,-6,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft65 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft65")
loft65= Part.makeLoft(section,True)
Loft65.Shape = loft65
section.remove
circle1 = Part.makeCircle(10,Base.Vector(18.5,229.5,73),Base.Vector(-18,33,-1.5),0,360)
circle2 = Part.makeCircle(7.98308,Base.Vector(0.5,262.5,71.5),Base.Vector(-18,33,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft66 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft66")
loft66= Part.makeLoft(section,True)
Loft66.Shape = loft66
section.remove
circle1 = Part.makeCircle(4.35493,Base.Vector(21.5,246,88),Base.Vector(12,-13.5,4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(33.5,232.5,92.5),Base.Vector(12,-13.5,4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft67 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft67")
loft67= Part.makeLoft(section,True)
Loft67.Shape = loft67
section.remove
circle1 = Part.makeCircle(4.35493,Base.Vector(21.5,246,88),Base.Vector(9,16.5,-4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(30.5,262.5,83.5),Base.Vector(9,16.5,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft68 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft68")
loft68= Part.makeLoft(section,True)
Loft68.Shape = loft68
section.remove
circle1 = Part.makeCircle(4.35493,Base.Vector(21.5,246,88),Base.Vector(-3,16.5,-4.5),0,360)
circle2 = Part.makeCircle(4,Base.Vector(18.5,262.5,83.5),Base.Vector(-3,16.5,-4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft69 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft69")
loft69= Part.makeLoft(section,True)
Loft69.Shape = loft69
section.remove
circle1 = Part.makeCircle(5.8377,Base.Vector(24.5,112.5,56.5),Base.Vector(19.5,-1.5,-1.5),0,360)
circle2 = Part.makeCircle(7.44688,Base.Vector(44,111,55),Base.Vector(19.5,-1.5,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft70 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft70")
loft70= Part.makeLoft(section,True)
Loft70.Shape = loft70
section.remove
circle1 = Part.makeCircle(5.10432,Base.Vector(23,195,-32),Base.Vector(10.5,-4.5,7.5),0,360)
circle2 = Part.makeCircle(4.49109,Base.Vector(33.5,190.5,-24.5),Base.Vector(10.5,-4.5,7.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft71 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft71")
loft71= Part.makeLoft(section,True)
Loft71.Shape = loft71
section.remove
circle1 = Part.makeCircle(5.10432,Base.Vector(23,195,-32),Base.Vector(15.75,-12,-12.75),0,360)
circle2 = Part.makeCircle(5.10432,Base.Vector(38.75,183,-44.75),Base.Vector(15.75,-12,-12.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft72 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft72")
loft72= Part.makeLoft(section,True)
Loft72.Shape = loft72
section.remove
circle1 = Part.makeCircle(4,Base.Vector(24.5,223.5,92.5),Base.Vector(9,9,0),0,360)
circle2 = Part.makeCircle(4,Base.Vector(33.5,232.5,92.5),Base.Vector(9,9,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft73 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft73")
loft73= Part.makeLoft(section,True)
Loft73.Shape = loft73
section.remove
circle1 = Part.makeCircle(6.45669,Base.Vector(30.5,190.5,2.5),Base.Vector(20.25,-9.75,-12.75),0,360)
circle2 = Part.makeCircle(4,Base.Vector(50.75,180.75,-10.25),Base.Vector(20.25,-9.75,-12.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft74 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft74")
loft74= Part.makeLoft(section,True)
Loft74.Shape = loft74
section.remove
circle1 = Part.makeCircle(6.45669,Base.Vector(30.5,190.5,2.5),Base.Vector(3,0,-27),0,360)
circle2 = Part.makeCircle(4.49109,Base.Vector(33.5,190.5,-24.5),Base.Vector(3,0,-27),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft75 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft75")
loft75= Part.makeLoft(section,True)
Loft75.Shape = loft75
section.remove
circle1 = Part.makeCircle(10,Base.Vector(30.5,199.5,59.5),Base.Vector(0,24,12),0,360)
circle2 = Part.makeCircle(10,Base.Vector(30.5,223.5,71.5),Base.Vector(0,24,12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft76 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft76")
loft76= Part.makeLoft(section,True)
Loft76.Shape = loft76
section.remove
circle1 = Part.makeCircle(4.49109,Base.Vector(33.5,190.5,-24.5),Base.Vector(17.25,-9.75,14.25),0,360)
circle2 = Part.makeCircle(4,Base.Vector(50.75,180.75,-10.25),Base.Vector(17.25,-9.75,14.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft77 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft77")
loft77= Part.makeLoft(section,True)
Loft77.Shape = loft77
section.remove
circle1 = Part.makeCircle(10,Base.Vector(30.5,223.5,71.5),Base.Vector(12,-9,0),0,360)
circle2 = Part.makeCircle(10,Base.Vector(42.5,214.5,71.5),Base.Vector(12,-9,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft78 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft78")
loft78= Part.makeLoft(section,True)
Loft78.Shape = loft78
section.remove
circle1 = Part.makeCircle(4,Base.Vector(33.5,232.5,92.5),Base.Vector(27,30,0),0,360)
circle2 = Part.makeCircle(5.13174,Base.Vector(60.5,262.5,92.5),Base.Vector(27,30,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft79 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft79")
loft79= Part.makeLoft(section,True)
Loft79.Shape = loft79
section.remove
circle1 = Part.makeCircle(5.10432,Base.Vector(38.75,183,-44.75),Base.Vector(18.75,-7.5,29.25),0,360)
circle2 = Part.makeCircle(4,Base.Vector(57.5,175.5,-15.5),Base.Vector(18.75,-7.5,29.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft80 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft80")
loft80= Part.makeLoft(section,True)
Loft80.Shape = loft80
section.remove
circle1 = Part.makeCircle(7.44688,Base.Vector(44,111,55),Base.Vector(19.5,13.5,1.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(63.5,124.5,56.5),Base.Vector(19.5,13.5,1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft81 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft81")
loft81= Part.makeLoft(section,True)
Loft81.Shape = loft81
section.remove
circle1 = Part.makeCircle(10,Base.Vector(42.5,214.5,71.5),Base.Vector(9,-9,0),0,360)
circle2 = Part.makeCircle(10,Base.Vector(51.5,205.5,71.5),Base.Vector(9,-9,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft82 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft82")
loft82= Part.makeLoft(section,True)
Loft82.Shape = loft82
section.remove
circle1 = Part.makeCircle(10,Base.Vector(42.5,214.5,71.5),Base.Vector(30,36,6),0,360)
circle2 = Part.makeCircle(8.32407,Base.Vector(72.5,250.5,77.5),Base.Vector(30,36,6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft83 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft83")
loft83= Part.makeLoft(section,True)
Loft83.Shape = loft83
section.remove
circle1 = Part.makeCircle(7.44688,Base.Vector(44,111,55),Base.Vector(19.5,-4.5,-1.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(63.5,106.5,53.5),Base.Vector(19.5,-4.5,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft84 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft84")
loft84= Part.makeLoft(section,True)
Loft84.Shape = loft84
section.remove
circle1 = Part.makeCircle(7.44688,Base.Vector(44,111,55),Base.Vector(-7.5,-28.5,-1.5),0,360)
circle2 = Part.makeCircle(4.00726,Base.Vector(36.5,82.5,53.5),Base.Vector(-7.5,-28.5,-1.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft85 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft85")
loft85= Part.makeLoft(section,True)
Loft85.Shape = loft85
section.remove
circle1 = Part.makeCircle(10,Base.Vector(51.5,205.5,71.5),Base.Vector(9,-15,18),0,360)
circle2 = Part.makeCircle(7.4113,Base.Vector(60.5,190.5,89.5),Base.Vector(9,-15,18),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft86 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft86")
loft86= Part.makeLoft(section,True)
Loft86.Shape = loft86
section.remove
circle1 = Part.makeCircle(10,Base.Vector(51.5,205.5,71.5),Base.Vector(7.5,-36,-9),0,360)
circle2 = Part.makeCircle(10,Base.Vector(59,169.5,62.5),Base.Vector(7.5,-36,-9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft87 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft87")
loft87= Part.makeLoft(section,True)
Loft87.Shape = loft87
section.remove
circle1 = Part.makeCircle(4,Base.Vector(50.75,180.75,-10.25),Base.Vector(6.75,-5.25,-5.25),0,360)
circle2 = Part.makeCircle(4,Base.Vector(57.5,175.5,-15.5),Base.Vector(6.75,-5.25,-5.25),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft88 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft88")
loft88= Part.makeLoft(section,True)
Loft88.Shape = loft88
section.remove
circle1 = Part.makeCircle(4,Base.Vector(50.75,180.75,-10.25),Base.Vector(8.25,-11.25,72.75),0,360)
circle2 = Part.makeCircle(10,Base.Vector(59,169.5,62.5),Base.Vector(8.25,-11.25,72.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft89 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft89")
loft89= Part.makeLoft(section,True)
Loft89.Shape = loft89
section.remove
circle1 = Part.makeCircle(10,Base.Vector(59,169.5,62.5),Base.Vector(1.5,21,27),0,360)
circle2 = Part.makeCircle(7.4113,Base.Vector(60.5,190.5,89.5),Base.Vector(1.5,21,27),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft90 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft90")
loft90= Part.makeLoft(section,True)
Loft90.Shape = loft90
section.remove
circle1 = Part.makeCircle(4,Base.Vector(57.5,175.5,-15.5),Base.Vector(10.5,-34.5,-27),0,360)
circle2 = Part.makeCircle(4.49802,Base.Vector(68,141,-42.5),Base.Vector(10.5,-34.5,-27),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft91 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft91")
loft91= Part.makeLoft(section,True)
Loft91.Shape = loft91
section.remove
circle1 = Part.makeCircle(10,Base.Vector(59,169.5,62.5),Base.Vector(4.5,-45,-6),0,360)
circle2 = Part.makeCircle(10,Base.Vector(63.5,124.5,56.5),Base.Vector(4.5,-45,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft92 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft92")
loft92= Part.makeLoft(section,True)
Loft92.Shape = loft92
section.remove
circle1 = Part.makeCircle(7.4113,Base.Vector(60.5,190.5,89.5),Base.Vector(0,72,3),0,360)
circle2 = Part.makeCircle(5.13174,Base.Vector(60.5,262.5,92.5),Base.Vector(0,72,3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft93 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft93")
loft93= Part.makeLoft(section,True)
Loft93.Shape = loft93
section.remove
circle1 = Part.makeCircle(10,Base.Vector(63.5,106.5,53.5),Base.Vector(3,-24,-6),0,360)
circle2 = Part.makeCircle(10,Base.Vector(66.5,82.5,47.5),Base.Vector(3,-24,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft94 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft94")
loft94= Part.makeLoft(section,True)
Loft94.Shape = loft94
section.remove
circle1 = Part.makeCircle(10,Base.Vector(63.5,106.5,53.5),Base.Vector(0,18,3),0,360)
circle2 = Part.makeCircle(10,Base.Vector(63.5,124.5,56.5),Base.Vector(0,18,3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft95 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft95")
loft95= Part.makeLoft(section,True)
Loft95.Shape = loft95
section.remove
circle1 = Part.makeCircle(4.85043,Base.Vector(62,153,-48.5),Base.Vector(6,-12,6),0,360)
circle2 = Part.makeCircle(4.49802,Base.Vector(68,141,-42.5),Base.Vector(6,-12,6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft96 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft96")
loft96= Part.makeLoft(section,True)
Loft96.Shape = loft96
section.remove
circle1 = Part.makeCircle(4.49802,Base.Vector(68,141,-42.5),Base.Vector(1.5,-58.5,-6),0,360)
circle2 = Part.makeCircle(4.3929,Base.Vector(69.5,82.5,-48.5),Base.Vector(1.5,-58.5,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft97 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft97")
loft97= Part.makeLoft(section,True)
Loft97.Shape = loft97
section.remove
circle1 = Part.makeCircle(8.32407,Base.Vector(72.5,250.5,77.5),Base.Vector(-3,12,15),0,360)
circle2 = Part.makeCircle(4.99191,Base.Vector(69.5,262.5,92.5),Base.Vector(-3,12,15),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft98 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft98")
loft98= Part.makeLoft(section,True)
Loft98.Shape = loft98
section.remove
circle1 = Part.makeCircle(8.32407,Base.Vector(72.5,250.5,77.5),Base.Vector(-6,12,-6),0,360)
circle2 = Part.makeCircle(6.25379,Base.Vector(66.5,262.5,71.5),Base.Vector(-6,12,-6),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft99 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft99")
loft99= Part.makeLoft(section,True)
Loft99.Shape = loft99
section.remove
circle1 = Part.makeCircle(8.92186,Base.Vector(-14.5,144,-9.5),Base.Vector(0,15,-27),0,360)
circle2 = Part.makeCircle(4.35996,Base.Vector(-14.5,159,-36.5),Base.Vector(0,15,-27),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft100 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft100")
loft100= Part.makeLoft(section,True)
Loft100.Shape = loft100
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,196.5,65.5),Base.Vector(6,-15,4.5),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-5.5,181.5,70),Base.Vector(6,-15,4.5),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft101 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft101")
loft101= Part.makeLoft(section,True)
Loft101.Shape = loft101
section.remove
circle1 = Part.makeCircle(4.85043,Base.Vector(62,153,-48.5),Base.Vector(-23.25,30,3.75),0,360)
circle2 = Part.makeCircle(5.10432,Base.Vector(38.75,183,-44.75),Base.Vector(-23.25,30,3.75),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft102 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft102")
loft102= Part.makeLoft(section,True)
Loft102.Shape = loft102
section.remove
circle1 = Part.makeCircle(5.13174,Base.Vector(60.5,262.5,92.5),Base.Vector(9,0,0),0,360)
circle2 = Part.makeCircle(4.99191,Base.Vector(69.5,262.5,92.5),Base.Vector(9,0,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft103 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft103")
loft103= Part.makeLoft(section,True)
Loft103.Shape = loft103
section.remove
circle1 = Part.makeCircle(4.99191,Base.Vector(69.5,262.5,92.5),Base.Vector(-3,0,-21),0,360)
circle2 = Part.makeCircle(6.25379,Base.Vector(66.5,262.5,71.5),Base.Vector(-3,0,-21),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft104 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft104")
loft104= Part.makeLoft(section,True)
Loft104.Shape = loft104
section.remove
circle1 = Part.makeCircle(6.25379,Base.Vector(66.5,262.5,71.5),Base.Vector(-66,0,0),0,360)
circle2 = Part.makeCircle(7.98308,Base.Vector(0.5,262.5,71.5),Base.Vector(-66,0,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft105 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft105")
loft105= Part.makeLoft(section,True)
Loft105.Shape = loft105
section.remove
circle1 = Part.makeCircle(7.98308,Base.Vector(0.5,262.5,71.5),Base.Vector(-12,0,3),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,262.5,74.5),Base.Vector(-12,0,3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft106 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft106")
loft106= Part.makeLoft(section,True)
Loft106.Shape = loft106
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,262.5,74.5),Base.Vector(-15,0,0),0,360)
circle2 = Part.makeCircle(7.85803,Base.Vector(-26.5,262.5,74.5),Base.Vector(-15,0,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft107 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft107")
loft107= Part.makeLoft(section,True)
Loft107.Shape = loft107
section.remove
circle1 = Part.makeCircle(7.85803,Base.Vector(-26.5,262.5,74.5),Base.Vector(-9,0,-3),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-35.5,262.5,71.5),Base.Vector(-9,0,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft108 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft108")
loft108= Part.makeLoft(section,True)
Loft108.Shape = loft108
section.remove
circle1 = Part.makeCircle(4,Base.Vector(-35.5,262.5,86.5),Base.Vector(54,0,-3),0,360)
circle2 = Part.makeCircle(4,Base.Vector(18.5,262.5,83.5),Base.Vector(54,0,-3),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft109 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft109")
loft109= Part.makeLoft(section,True)
Loft109.Shape = loft109
section.remove
circle1 = Part.makeCircle(4,Base.Vector(18.5,262.5,83.5),Base.Vector(12,0,0),0,360)
circle2 = Part.makeCircle(4,Base.Vector(30.5,262.5,83.5),Base.Vector(12,0,0),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft110 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft110")
loft110= Part.makeLoft(section,True)
Loft110.Shape = loft110
section.remove
circle1 = Part.makeCircle(4,Base.Vector(30.5,262.5,83.5),Base.Vector(30,0,9),0,360)
circle2 = Part.makeCircle(5.13174,Base.Vector(60.5,262.5,92.5),Base.Vector(30,0,9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft111 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft111")
loft111= Part.makeLoft(section,True)
Loft111.Shape = loft111
section.remove
circle1 = Part.makeCircle(5.13174,Base.Vector(60.5,262.5,92.5),Base.Vector(6,0,-21),0,360)
circle2 = Part.makeCircle(6.25379,Base.Vector(66.5,262.5,71.5),Base.Vector(6,0,-21),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft112 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft112")
loft112= Part.makeLoft(section,True)
Loft112.Shape = loft112
section.remove
circle1 = Part.makeCircle(6.25379,Base.Vector(66.5,262.5,71.5),Base.Vector(-36,0,12),0,360)
circle2 = Part.makeCircle(4,Base.Vector(30.5,262.5,83.5),Base.Vector(-36,0,12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft113 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft113")
loft113= Part.makeLoft(section,True)
Loft113.Shape = loft113
section.remove
circle1 = Part.makeCircle(4,Base.Vector(30.5,262.5,83.5),Base.Vector(-30,0,-12),0,360)
circle2 = Part.makeCircle(7.98308,Base.Vector(0.5,262.5,71.5),Base.Vector(-30,0,-12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft114 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft114")
loft114= Part.makeLoft(section,True)
Loft114.Shape = loft114
section.remove
circle1 = Part.makeCircle(4,Base.Vector(18.5,262.5,83.5),Base.Vector(-18,0,-12),0,360)
circle2 = Part.makeCircle(7.98308,Base.Vector(0.5,262.5,71.5),Base.Vector(-18,0,-12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft115 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft115")
loft115= Part.makeLoft(section,True)
Loft115.Shape = loft115
section.remove
circle1 = Part.makeCircle(4,Base.Vector(18.5,262.5,83.5),Base.Vector(-30,0,-9),0,360)
circle2 = Part.makeCircle(10,Base.Vector(-11.5,262.5,74.5),Base.Vector(-30,0,-9),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft116 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft116")
loft116= Part.makeLoft(section,True)
Loft116.Shape = loft116
section.remove
circle1 = Part.makeCircle(10,Base.Vector(-11.5,262.5,74.5),Base.Vector(-24,0,12),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-35.5,262.5,86.5),Base.Vector(-24,0,12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft117 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft117")
loft117= Part.makeLoft(section,True)
Loft117.Shape = loft117
section.remove
circle1 = Part.makeCircle(7.85803,Base.Vector(-26.5,262.5,74.5),Base.Vector(-9,0,12),0,360)
circle2 = Part.makeCircle(4,Base.Vector(-35.5,262.5,86.5),Base.Vector(-9,0,12),0,360)
section = []
section.append(circle1)
section.append(circle2)
Loft118 = FreeCAD.ActiveDocument.addObject("Part::Loft","Loft118")
loft118= Part.makeLoft(section,True)
Loft118.Shape = loft118
section.remove
Sphere0 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere0")
ball0 = Part.makeSphere(4.2,Base.Vector(-35.5,262.5,86.5),Base.Vector(0,0,1),-90,90,360)
Sphere0.Shape = ball0
Sphere1 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere1")
ball1 = Part.makeSphere(4.2,Base.Vector(-35.5,262.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere1.Shape = ball1
Sphere2 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere2")
ball2 = Part.makeSphere(4.8164,Base.Vector(-32.5,241.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere2.Shape = ball2
Sphere3 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere3")
ball3 = Part.makeSphere(4.78764,Base.Vector(-31.75,224.25,95.5),Base.Vector(0,0,1),-90,90,360)
Sphere3.Shape = ball3
Sphere4 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere4")
ball4 = Part.makeSphere(4.2,Base.Vector(-26.5,207,91),Base.Vector(0,0,1),-90,90,360)
Sphere4.Shape = ball4
Sphere5 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere5")
ball5 = Part.makeSphere(6.66509,Base.Vector(-23.5,247.5,86.5),Base.Vector(0,0,1),-90,90,360)
Sphere5.Shape = ball5
Sphere6 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere6")
ball6 = Part.makeSphere(4.2,Base.Vector(-20.5,214.5,95.5),Base.Vector(0,0,1),-90,90,360)
Sphere6.Shape = ball6
Sphere7 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere7")
ball7 = Part.makeSphere(4.2,Base.Vector(-11.5,225,91),Base.Vector(0,0,1),-90,90,360)
Sphere7.Shape = ball7
Sphere8 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere8")
ball8 = Part.makeSphere(5.90381,Base.Vector(-3.25,198.75,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere8.Shape = ball8
Sphere9 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere9")
ball9 = Part.makeSphere(10.5,Base.Vector(-20.5,211.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere9.Shape = ball9
Sphere10 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere10")
ball10 = Part.makeSphere(10.5,Base.Vector(-11.5,235.5,80.5),Base.Vector(0,0,1),-90,90,360)
Sphere10.Shape = ball10
Sphere11 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere11")
ball11 = Part.makeSphere(8.25093,Base.Vector(-26.5,262.5,74.5),Base.Vector(0,0,1),-90,90,360)
Sphere11.Shape = ball11
Sphere12 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere12")
ball12 = Part.makeSphere(10.5,Base.Vector(-11.5,196.5,65.5),Base.Vector(0,0,1),-90,90,360)
Sphere12.Shape = ball12
Sphere13 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere13")
ball13 = Part.makeSphere(4.2,Base.Vector(-17.5,121.5,32.5),Base.Vector(0,0,1),-90,90,360)
Sphere13.Shape = ball13
Sphere14 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere14")
ball14 = Part.makeSphere(10.5,Base.Vector(-7.75,114,49.75),Base.Vector(0,0,1),-90,90,360)
Sphere14.Shape = ball14
Sphere15 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere15")
ball15 = Part.makeSphere(9.36795,Base.Vector(-14.5,144,-9.5),Base.Vector(0,0,1),-90,90,360)
Sphere15.Shape = ball15
Sphere16 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere16")
ball16 = Part.makeSphere(8.62283,Base.Vector(-12.25,165.75,34.75),Base.Vector(0,0,1),-90,90,360)
Sphere16.Shape = ball16
Sphere17 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere17")
ball17 = Part.makeSphere(8.14872,Base.Vector(-14.5,133.5,-18.5),Base.Vector(0,0,1),-90,90,360)
Sphere17.Shape = ball17
Sphere18 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere18")
ball18 = Part.makeSphere(10.4969,Base.Vector(-11.5,97.5,-42.5),Base.Vector(0,0,1),-90,90,360)
Sphere18.Shape = ball18
Sphere19 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere19")
ball19 = Part.makeSphere(4.57795,Base.Vector(-14.5,144,-34.25),Base.Vector(0,0,1),-90,90,360)
Sphere19.Shape = ball19
Sphere20 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere20")
ball20 = Part.makeSphere(4.2,Base.Vector(12.5,115.5,-45.5),Base.Vector(0,0,1),-90,90,360)
Sphere20.Shape = ball20
Sphere21 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere21")
ball21 = Part.makeSphere(4.57795,Base.Vector(-14.5,159,-36.5),Base.Vector(0,0,1),-90,90,360)
Sphere21.Shape = ball21
Sphere22 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere22")
ball22 = Part.makeSphere(9.36795,Base.Vector(-14.5,166.5,14.5),Base.Vector(0,0,1),-90,90,360)
Sphere22.Shape = ball22
Sphere23 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere23")
ball23 = Part.makeSphere(7.90529,Base.Vector(-2.5,195,5.5),Base.Vector(0,0,1),-90,90,360)
Sphere23.Shape = ball23
Sphere24 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere24")
ball24 = Part.makeSphere(10.4969,Base.Vector(-14.5,82.5,-45.5),Base.Vector(0,0,1),-90,90,360)
Sphere24.Shape = ball24
Sphere25 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere25")
ball25 = Part.makeSphere(10.5,Base.Vector(-11.5,163.5,53.5),Base.Vector(0,0,1),-90,90,360)
Sphere25.Shape = ball25
Sphere26 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere26")
ball26 = Part.makeSphere(10.5,Base.Vector(-8.5,130.5,56.5),Base.Vector(0,0,1),-90,90,360)
Sphere26.Shape = ball26
Sphere27 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere27")
ball27 = Part.makeSphere(10.5,Base.Vector(-5.5,181.5,70),Base.Vector(0,0,1),-90,90,360)
Sphere27.Shape = ball27
Sphere28 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere28")
ball28 = Part.makeSphere(5.35953,Base.Vector(23,195,-32),Base.Vector(0,0,1),-90,90,360)
Sphere28.Shape = ball28
Sphere29 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere29")
ball29 = Part.makeSphere(7.2185,Base.Vector(0.5,198,35.5),Base.Vector(0,0,1),-90,90,360)
Sphere29.Shape = ball29
Sphere30 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere30")
ball30 = Part.makeSphere(10.5,Base.Vector(15.5,200.25,40),Base.Vector(0,0,1),-90,90,360)
Sphere30.Shape = ball30
Sphere31 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere31")
ball31 = Part.makeSphere(10.5,Base.Vector(-11.5,262.5,74.5),Base.Vector(0,0,1),-90,90,360)
Sphere31.Shape = ball31
Sphere32 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere32")
ball32 = Part.makeSphere(6.12959,Base.Vector(24.5,112.5,56.5),Base.Vector(0,0,1),-90,90,360)
Sphere32.Shape = ball32
Sphere33 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere33")
ball33 = Part.makeSphere(10.4774,Base.Vector(-2.5,103.5,53.5),Base.Vector(0,0,1),-90,90,360)
Sphere33.Shape = ball33
Sphere34 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere34")
ball34 = Part.makeSphere(4.87842,Base.Vector(9.5,199.5,62.5),Base.Vector(0,0,1),-90,90,360)
Sphere34.Shape = ball34
Sphere35 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere35")
ball35 = Part.makeSphere(6.16019,Base.Vector(3.5,184.5,88),Base.Vector(0,0,1),-90,90,360)
Sphere35.Shape = ball35
Sphere36 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere36")
ball36 = Part.makeSphere(9.76128,Base.Vector(-8.5,82.5,44.5),Base.Vector(0,0,1),-90,90,360)
Sphere36.Shape = ball36
Sphere37 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere37")
ball37 = Part.makeSphere(10.5,Base.Vector(18.5,229.5,73),Base.Vector(0,0,1),-90,90,360)
Sphere37.Shape = ball37
Sphere38 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere38")
ball38 = Part.makeSphere(8.35784,Base.Vector(14.75,199.5,19.375),Base.Vector(0,0,1),-90,90,360)
Sphere38.Shape = ball38
Sphere39 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere39")
ball39 = Part.makeSphere(4.70689,Base.Vector(12.5,217.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere39.Shape = ball39
Sphere40 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere40")
ball40 = Part.makeSphere(10.5,Base.Vector(30.5,199.5,59.5),Base.Vector(0,0,1),-90,90,360)
Sphere40.Shape = ball40
Sphere41 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere41")
ball41 = Part.makeSphere(10.5,Base.Vector(30.5,223.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere41.Shape = ball41
Sphere42 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere42")
ball42 = Part.makeSphere(5.09295,Base.Vector(62,153,-48.5),Base.Vector(0,0,1),-90,90,360)
Sphere42.Shape = ball42
Sphere43 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere43")
ball43 = Part.makeSphere(4.2,Base.Vector(24.5,223.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere43.Shape = ball43
Sphere44 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere44")
ball44 = Part.makeSphere(4.81589,Base.Vector(15.5,232.5,91),Base.Vector(0,0,1),-90,90,360)
Sphere44.Shape = ball44
Sphere45 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere45")
ball45 = Part.makeSphere(6.77952,Base.Vector(30.5,190.5,2.5),Base.Vector(0,0,1),-90,90,360)
Sphere45.Shape = ball45
Sphere46 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere46")
ball46 = Part.makeSphere(4.57268,Base.Vector(21.5,246,88),Base.Vector(0,0,1),-90,90,360)
Sphere46.Shape = ball46
Sphere47 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere47")
ball47 = Part.makeSphere(8.38224,Base.Vector(0.5,262.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere47.Shape = ball47
Sphere48 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere48")
ball48 = Part.makeSphere(4.2,Base.Vector(33.5,232.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere48.Shape = ball48
Sphere49 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere49")
ball49 = Part.makeSphere(4.2,Base.Vector(30.5,262.5,83.5),Base.Vector(0,0,1),-90,90,360)
Sphere49.Shape = ball49
Sphere50 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere50")
ball50 = Part.makeSphere(4.2,Base.Vector(18.5,262.5,83.5),Base.Vector(0,0,1),-90,90,360)
Sphere50.Shape = ball50
Sphere51 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere51")
ball51 = Part.makeSphere(7.81923,Base.Vector(44,111,55),Base.Vector(0,0,1),-90,90,360)
Sphere51.Shape = ball51
Sphere52 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere52")
ball52 = Part.makeSphere(4.71565,Base.Vector(33.5,190.5,-24.5),Base.Vector(0,0,1),-90,90,360)
Sphere52.Shape = ball52
Sphere53 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere53")
ball53 = Part.makeSphere(5.35953,Base.Vector(38.75,183,-44.75),Base.Vector(0,0,1),-90,90,360)
Sphere53.Shape = ball53
Sphere54 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere54")
ball54 = Part.makeSphere(4.2,Base.Vector(50.75,180.75,-10.25),Base.Vector(0,0,1),-90,90,360)
Sphere54.Shape = ball54
Sphere55 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere55")
ball55 = Part.makeSphere(10.5,Base.Vector(42.5,214.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere55.Shape = ball55
Sphere56 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere56")
ball56 = Part.makeSphere(5.38833,Base.Vector(60.5,262.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere56.Shape = ball56
Sphere57 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere57")
ball57 = Part.makeSphere(4.2,Base.Vector(57.5,175.5,-15.5),Base.Vector(0,0,1),-90,90,360)
Sphere57.Shape = ball57
Sphere58 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere58")
ball58 = Part.makeSphere(10.5,Base.Vector(63.5,124.5,56.5),Base.Vector(0,0,1),-90,90,360)
Sphere58.Shape = ball58
Sphere59 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere59")
ball59 = Part.makeSphere(10.5,Base.Vector(51.5,205.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere59.Shape = ball59
Sphere60 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere60")
ball60 = Part.makeSphere(8.74027,Base.Vector(72.5,250.5,77.5),Base.Vector(0,0,1),-90,90,360)
Sphere60.Shape = ball60
Sphere61 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere61")
ball61 = Part.makeSphere(10.5,Base.Vector(63.5,106.5,53.5),Base.Vector(0,0,1),-90,90,360)
Sphere61.Shape = ball61
Sphere62 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere62")
ball62 = Part.makeSphere(4.20762,Base.Vector(36.5,82.5,53.5),Base.Vector(0,0,1),-90,90,360)
Sphere62.Shape = ball62
Sphere63 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere63")
ball63 = Part.makeSphere(7.78187,Base.Vector(60.5,190.5,89.5),Base.Vector(0,0,1),-90,90,360)
Sphere63.Shape = ball63
Sphere64 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere64")
ball64 = Part.makeSphere(10.5,Base.Vector(59,169.5,62.5),Base.Vector(0,0,1),-90,90,360)
Sphere64.Shape = ball64
Sphere65 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere65")
ball65 = Part.makeSphere(4.72292,Base.Vector(68,141,-42.5),Base.Vector(0,0,1),-90,90,360)
Sphere65.Shape = ball65
Sphere66 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere66")
ball66 = Part.makeSphere(10.5,Base.Vector(66.5,82.5,47.5),Base.Vector(0,0,1),-90,90,360)
Sphere66.Shape = ball66
Sphere67 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere67")
ball67 = Part.makeSphere(4.61255,Base.Vector(69.5,82.5,-48.5),Base.Vector(0,0,1),-90,90,360)
Sphere67.Shape = ball67
Sphere68 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere68")
ball68 = Part.makeSphere(5.24151,Base.Vector(69.5,262.5,92.5),Base.Vector(0,0,1),-90,90,360)
Sphere68.Shape = ball68
Sphere69 = FreeCAD.ActiveDocument.addObject("Part::Sphere","Sphere69")
ball69 = Part.makeSphere(6.56648,Base.Vector(66.5,262.5,71.5),Base.Vector(0,0,1),-90,90,360)
Sphere69.Shape = ball69

