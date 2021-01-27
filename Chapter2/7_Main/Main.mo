/*
 Use the Main class as the *top* of the instantiation hierarchy.
 Main is implicitly instantiated, this implies that its variables are 
 instantiated, and that the variables of those variables are instantiated and 
 so forth.

 In the following example the class `Point` and `Triangle` are instantiated.
 
*/
class Point "Point in a three-dimensional space"
  public
    Real x;
    Real y, z;
end Point;

class Triangle
  Point point1;
  Point Point2;
  Point point3;
end Triangle;

class Main
  Triangle pts;
end Main;
