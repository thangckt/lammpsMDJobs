import numpy as np
from scipy.interpolate import interp1d

'''
Interatomic potential for uranium in a
wide range of pressures and temperatures
D E Smirnova1 , S V Starikov1,2 and V V Stegailov1,2,3

Journal of Physics: Condensed Matter, 24(1):015702, 2012. 
'''


rij = [0, 1.90000, 2.12777, 2.35555, 2.58333, 2.81111, 3.03888,\
    3.26666, 3.49444, 3.72222, 3.95000, 4.17777, 4.40555, 4.63333,\
    4.86111, 5.08888, 5.31666, 5.54444, 5.77222, 6.00000, 6.25, 6.5,\
    6.75, 7.0, 7.25, 7.5, 7.75, 8.0]

rhoj =[0.000000, 0.075017, 0.190640, 0.306263, 0.421886,\
      0.537509, 0.653132, 0.768754, 0.884377, 1.000000, 1.353]

phi_rij = [15, 7.548735419793804800, 3.027262284620461300,0.932256757441457200,\
           0.241865209658825880,-0.052129863767814630, -0.234471524509781090,\
          -0.293405670917844590, -0.252497357178855960, -0.191608768374650930,\
          -0.120662870486473710, -0.042920121382967677, -0.005607540432113615,\
          0.013340387444210934, 0.032297818096560113, 0.042144521168244332,
          0.035553638079349650, 0.014891148455440949, -0.004642055500075333,
          -0.020000000000000000, -0.025, -0.02, -0.01, -0.005, -0.0025,\
          -0.00125,-0.0006, 0.0000 ]
           
rho_rij = [7.5, 0.54486568991306, 0.26238377745872, 0.15880407477249, 0.10349032348983,\
          0.05934252327280, 0.03190206213611, 0.02023582727383, 0.01514662392170,\
          0.01084747896164, 0.01051157902966, 0.00548838766427, -0.00203919214385,\
          -0.00489696313858, -0.00533732701887, -0.00427662406133,\
          -0.00459518852457,-0.00405115149015, -0.00277655219169,\
          -0.00100000000000, -0.0005, -0.00025, -0.000125, -0.0000625,\
          -0.0000312, -0.00001506, -0.0000007, 0.0] 

F_rhoj= [0.0000000000000, -1.4210874399504, -2.4675048993797,\
       -3.0000029746112, -3.2408830654253, -3.2465755532375,\
       -3.1124010647774, -2.8573309798021, -2.5050424392625,\
       -1.9823005839202, 0]

phi = interp1d(rij, phi_rij,  kind='cubic') # potUU
rho = interp1d(rij, rho_rij,  kind='cubic') #density
F = interp1d(rhoj, F_rhoj,  kind='cubic') #embed

