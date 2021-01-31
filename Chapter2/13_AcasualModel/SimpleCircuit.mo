// For the meaning of the numbers, refer to simple_cicuit_model.png
model SimpleCircuit
  Resistor R1(R=10);
  Resistor R2(R=100);
  Capacitor C(C=0.01);
  Inductor L(L=0.1);
  VsourceAC AC;
  Ground G;
equation
  connect(AC.p, R1.p);  // 1
  connect(R1.n, C.p);   // 2
  connect(C.n, AC.n);   // 3 
  connect(R1.p, R2.p);  // 4
  connect(R2.n, L.p);   // 5
  connect(L.n, C.n);    // 6
  connect(AC.n, G.p);   // 7
end SimpleCircuit;
