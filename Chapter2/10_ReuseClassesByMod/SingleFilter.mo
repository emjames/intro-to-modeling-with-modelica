model LowPassFilter
  parameter Real T=1  " Time constant of filter";
  Real u, y(start=1);
equation
  T*der(y) + y = u;
end LowPassFilter;

model SingleFilter
  LowPassFilter F1(T=2);
equation
  F1.u = sin(time);
end SingleFilter;
