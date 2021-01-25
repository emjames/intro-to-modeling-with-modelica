// Pendulum differential algebraic equation (DAE) without physical significance
class DAEexample
  Real x(start=0.9);
  Real y;
equation
  der(y) + (1+0.5 * sin(y)) * der(x) = sin(time);
  x-y = exp(-0.9 * x) * cos(y);
end DAEexample;
