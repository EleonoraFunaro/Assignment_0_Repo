# -*- coding: utf-8 -*-
#assignment 0
#EXAMPLE B

height=0.8            #m
wide=1.5              #m
k=0.78                #W/m*°C
T_in=20               #°C
T_out=-10             #°C
thickness=0.008       #m 
h_in=10               #W/m^2*°C 
h_out=40              #W/m^2*°C

R_in=1/(h_in*height*wide)
R_out=1/(h_out*height*wide)
R_wall=thickness/(k*height*wide)

R_tot=R_in+R_out+R_wall

Q=(T_in-T_out)/R_tot

print("The value of the heat transferred is: "+str(Q))              #W

T1=T_in-(Q*R_in)
T2=(Q*R_out)+T_out

print("The temperature of the inner surface is: " +str(T1))             #°C
print("The temperature of the outer surface is: " +str(T2))             #°C

