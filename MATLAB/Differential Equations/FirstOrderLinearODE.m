syms y(t)
ordEq = diff(y,t) == t*y;
ySol(t) = dsolve(ordEq);