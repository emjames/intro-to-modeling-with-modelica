// Record class only holds data
record ColorData
  Real red;
  Real blue;
  Real green;
end ColorData;

// Extends `ColorData` and adds an equation as constraint
class Color
  extends ColorData;
equation
  red + blue + green = 1;
end Color;

class Point
  public
    Real x;
    Real y, z;
end Point;

// Multiple inheritance
// Get the position variables from `Point` and the color variables and eq. from `Color`
class ColoredPoint
  extends Point;
  extends Color;
end ColoredPoint;
