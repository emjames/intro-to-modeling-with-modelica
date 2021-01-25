model VanDerPol   "Van der Pol oscillator model"
  Real x(start=1)   "Descriptive string for x";
    // x starts at 1
  Real y(start=1)   "Descriptive string for y";
    // y starts at 1
  parameter Real lambda = 0.3;
equation
  der(x) = y;
    // This is the first equation
  der(y) = -x + lambda * (1 - x*x) * y;
    /* The 2nd diff. equation */   
end VanDerPol;
