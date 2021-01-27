/* 
  A more general way of initializing a set of variables according to some 
  constraints is to specify an equation system to be solved to obtain the 
  initial values of these variables.

  Use the `initial equation` construct.
*/
model Controller
  Real y, a, b, u;
equation
  der(y) = a*y + b*u;
initial equation
  der(y) = 0;
end Controller;
