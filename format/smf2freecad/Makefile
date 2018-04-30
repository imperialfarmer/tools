CXX = g++ -std=c++11

CXXFLAGS = -w

INCLUDES  =

CXXFLAGS += $(INCLUDES)

OBJS = smf2freecad.o

LIBS =

TARGET = smf2freecad

$(TARGET): $(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LIBS)

smf2freecad.o : ./smf2freecad.cpp
	$(CXX) $(CXXFLAGS) -c ./smf2freecad.cpp

all:    $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)
