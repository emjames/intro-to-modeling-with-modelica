/* 
  Assume we want to connect two filter models with different time constatns in series.
  Instead of creating two separate filter classes, define a common filter class
  and create two appropriately modified instances of this class, which are connected.
*/
model LowPassFilter
  parameter Real T=1  " Time constant of filter";
  Real u, y(start=1);
equation
  T*der(y) + y = u;
end LowPassFilter;

model FiltersInSeries
  LowPassFilter F1(T=2), F2(T=3);  // "modifiers" that modify the time constant
equation
  F1.u = sin(time);
  F2.u = F1.y;  // Connect them together by this equation
end FiltersInSeries;

model ModifiedFiltersInSeries
  LowPassFilter F1(T=2);
  /* FiltersInSeries F12(F1(T=6), F2.T=11); */
end ModifiedFiltersInSeries;
