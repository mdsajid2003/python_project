#Program to simuate the luck factor in anyone's life 
import numpy as np
#number of trails 
trails = 1000
# seed value to zero
np.random.seed(0)
#Random value generated from 90-95% as a workload by the employee
work_load = np.round(np.random.uniform(90,95,100),2)
# work_load = 95
# print(work_load)
#printing the maximum value of workload
print(f'The maximum work % is {max(work_load)}')
#Random value generated from 1-100% as a workload by the employee
luck_factor = np.round(np.random.uniform(1,100,100),2)
#Transforming the 100% to 5%
luck_ = np.round(luck_factor * (5 / 100),2)
# print(luck_)
print(f'The maximum luck % is {max(luck_)}')
# The sum of Both Workload and Luck
success = work_load + luck_
success_int  = np.round(success,2)
# print(success_int)
print(f'{max(work_load)} + {max(luck_)}')
# Printing the Maximum Success %
print(max(success_int))