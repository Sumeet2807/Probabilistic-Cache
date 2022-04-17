from parameters import *
from cache import *
from infra import *
from events import *
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



cache_types = [Cache,LFU_Cache,LRU_Cache,MRU_Cache]
for cache_type in cache_types:
    total_times = []
    queue_delays = []
    req_served = []
    for iteration in range(SIMULATOR_ITERATIONS):

        # initialize simulator environment
        # np.random.seed(11)
        files = Files()
        cache = cache_type(files)
        # cache = Cache(files)

        sim = Simulator_Env(files,cache)

        #initialize new req events to be processed at every second
        for i in range(TOTAL_TIME_TO_RUN):
            E_get_new_reqs(sim,i)


        #Main simulator loop
        while(len(sim.sim_q.q)):

            e = sim.sim_q.pop()
            e.process()    


        total_times.append(np.mean(sim.get_total_times_for_reqs()))
        queue_delays.append(np.mean(sim.queue_delays))
        req_served.append(sim.req_count)

    print("Cache system - " + cache.__class__.__name__)
    print('Average number of req served during simulations - ' + str(np.mean(req_served)))
    print('Average Response rate for the requests - ' + str(np.mean(total_times)))
    print('Average Queue delay in the process - ' + str(np.mean(queue_delays)))
    p = sns.histplot(data=total_times,kde=True)
    p.set_xlabel('time(sec)')
    # p.set_xlim(0,10)

    plt.show()
    print('\n')
    print('*********************XXXXXXXXXXXXXX*********************')
    print('\n')
