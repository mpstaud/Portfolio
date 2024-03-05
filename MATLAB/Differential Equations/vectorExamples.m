%The colon operator iterates through the specified values
vec = 2:6;

%The second vector follows the format (first:step:last)
%Step is the step value, so it iterates through every other number
nv = 1:2:9;

%linspace function

ls = linspace(3,15,5);

% format is linspace(x,y,n)
% Creates a vector with n values in the inclusive range from x to y
% The default value is 100 if n is omitted



% logspace function
% Creates a logarithmically spaced vector

logspace(1,4,4)

% Format is logspace(x,y,n)
% default value is 50 if n is omitted



%Creating vector variable with existing variables

newvec = [nv ls];
%new vector with all values from nv and ls
