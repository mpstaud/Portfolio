syms u(x)
Du = diff(u,x);
D2u = diff(u,x,2);
ode = diff(u,x,3) == u;
%declare our initial condition
cond1 = u(0) == 1;
cond2 = Du(0) == -1;
cond3 = D2u(0) == pi;
%puts the conditions into a 1x3 matrix
conds = [cond1 cond2 cond3];
uSol(x) = dsolve(ode, conds)
