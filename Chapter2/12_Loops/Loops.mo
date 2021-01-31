/*
  Consider an equation for a polynomial expression:
  y = a[1]+a[2]*x + a[3]*xˆ2 + ... + a[n+1]*xˆn

  Expressed using equations:
  xpowers[1] = 1;
  xpowers[2] = xpowers[1]*x;
  ...
  xpowers[n+1] = xpowers[n]*x;
  y=a* xpowers;

  This can be expressed more conveniently using the `for` loop notation as follows.
*/
class Loops
  // Using for loop notation
  for i in i:n loop
    xpowers[i+1] = xpowers[i]*x;
  end for;

  // Using vector equation:
  xpowers[2:n+1] = xpowers[1:n]*x;
end Loops;
