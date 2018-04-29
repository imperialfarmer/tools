CXX = g++ -std=c++11

CXXFLAGS = -w

INCLUDES  =

CXXFLAGS += $(INCLUDES)

OBJS = smf2inp.o

LIBS =

TARGET = smf2inp

$(TARGET): $(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) $(LIBS)

smf2freecad.o : ./smf2inp.cpp
	$(CXX) $(CXXFLAGS) -c ./smf2inp.cpp

all:    $(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)


