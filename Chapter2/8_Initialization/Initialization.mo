/* 
  The solver will start the vaiable to a default `start` value if nothing is 
  specified. Other start values can be specified by setting the `start` 
  attribute of instance variables.

  Note: The start value only gives a suggestion for initial value, the solver
  may choose a different value unless the `fixed` attribute is true for that
  variable.

  The following is an example of a specified start value.
*/
class Triangle
  Point point1(start={1,2,3});
  Point point2;
  Point point3;
end Triangle;


/* 
  Alternatively that start value of `point1` can be specified when instatiating
  `Triangle`:
*/
class Main
  Triangle pts(point1.start={1,2,3});
end Main;
