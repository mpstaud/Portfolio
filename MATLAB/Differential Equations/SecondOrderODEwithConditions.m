syms y(x)
%Diff Function differentiates
Dy = diff(y);
%Differentiates y and x 2 times
ode = diff(y,x,2) == cos(2*x)-y;
cond1 = y(0) == 1;
cond2 = Dy(0) == 0;
conds = [cond1 cond2];
ySol(x) = dsolve(ode, conds);
ySol = simplify(ySol);
disp(ySol);