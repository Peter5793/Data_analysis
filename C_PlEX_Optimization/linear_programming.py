#Using IBM Desicion Optimization CPLEX Modelling for Python
# Download the library and install the python library
import sys
try:
    import cplex
except:
    if hasattr(sys, 'real_prefix'):
        !pip install cplex
    else:
        !pip install --user cplex

#installs DOcplex if needed
try:
    import docplex.mp
except:
    if hasattr(sys, 'real_prefix'):
        !pip install docplex
    else:
        !pip install docplex

# Set up the prescriptive model
# All objects of the model belong to one model instance
# first import the Model from docplex.mp
from docplex.mp.model import Model

#create one model instance with a name
m = Model(name='telephone_production')
#define the decision variables
#continuous variables desk representts the production of desk telephones
#continuous variables cell representts the production of cell phones
desk = m.continuous_var(name= 'desk')
cell = m.continuous_var(name = 'cell')

#Set up the constraints
# desk and cell phones must be both > 100
# Assembly time is limited
# Painiting time is limited
m.add_constraint(desk >= 100)
m.add_constraint(cell >= 100)

ct_assembly = m.add_constraint(0.2 * desk + 0.4 * cell <= 400)

ct_painting = m.add_constraint(0.5 * desk + 0.4 * cell <= 490)

# Express the Objective
# To maximize the expected the revenue
m.maximize(12 * desk + 20 * cell)
#Print information about the model
m.print_information()

#solivng the model
s = m.solve()
m.print_solution()
#implement the soft contraint model using DOCplex
# extra variable for overtime with an upper bound of 40 
#ub  = upper bound
overtime = m.continuous_var(name = 'overtime', ub=40)
# assembly line constrinats is modified on RHS to accomodate the overtime
ct_assembly.rhs = 400 + overtime
# modify the ojective expression to add the penalization term 
m.maximize(12 * desk + 20 * cell - 2 * overtime)
#$2 h charged 
# revert soft constraints
ct_assembly.rhs = 440
s3 = m.solve()

# now get slack value for assembly constraint: expected value is 40
print('* slack value for assembly time constraint is: {0}'.format(ct_assembly.slack_value))
# get slack value for painting time constraint, expected value is 0.
print('* slack value for painting time constraint is: {0}'.format(ct_painting.slack_value))
m.parameters.lpmethod = 4
m.solve(log_output=True)

