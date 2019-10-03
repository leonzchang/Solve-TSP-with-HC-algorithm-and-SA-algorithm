#Import library
from founction import *
import matplotlib.pyplot as plt





#initial variable
num_cities =51
seq = init(num_cities)
dic = {}
readfile(dic)

HC_minVal=0
HC_best_seq=[]
HC_Xis_sequence=[]
HC_temp = []
HC_history=[]
HC_Average_history=[]

iter_num = input('Please enter the iteration:')
iter_num = int(iter_num)
n_round = 10 #execute 10 rounds

SA_Xis_sequence=[]
SA_history = []
SA_seq_current = []
SA_seq_best = []
SA_seq_current = seq
SA_seq_best = seq


#Execute HC
for k in range(iter_num):
    HC_Xis_sequence.append(k+1)
    
for j in range(n_round):                #execute 10 rounds iteration
    iteration_history=[]
    HC_best_seq = seq
    for i in range(iter_num):    
        HC_temp = transform(HC_best_seq)
        (HC_best_seq, HC_minVal)= HC_determine(HC_temp,HC_best_seq,dic)
        print('HC_seq_best =',HC_best_seq)
        print('HC_seq_best evalution =',HC_minVal)
        iteration_history.append(TotalDistance(HC_best_seq,dic)) #record iteration history
    HC_history.append(iteration_history) #record n rounds iteration history

for i in range(iter_num):         #average the iteration set
    sum = 0
    for j in range(n_round):
        sum += HC_history[j][i]
    HC_Average_history.append(sum/n_round)


    
    
#Execute SA
for i in range(iter_num):
    print('iteration =',i+1,' --->')
    neighbor = []
    count = 0
    t_max = 100 #set init temperature
    t_min = 10  #set min temperature
    SA_Xis_sequence.append(i+1)
    while t_max > t_min:
        best_value = TotalDistance(SA_seq_best,dic)
        neighbors = neighbors_generator(SA_seq_current,10)
        (SA_seq_current,SA_seq_best)= SA_determine(neighbors,SA_seq_current,dic,t_max,SA_seq_best)
        t_max *= 0.9
       
    print('SA_seq_best  =',SA_seq_best)        
    print('SA_seq_best evalution =',TotalDistance(SA_seq_best,dic))
    SA_history.append(TotalDistance(SA_seq_best,dic))


#Output
plt.xlabel('iteration')
plt.ylabel('distance')
plt.plot(HC_Xis_sequence, HC_Average_history, label='HC')
plt.plot(SA_Xis_sequence, SA_history, label='SA')
plt.legend()
plt.show()
