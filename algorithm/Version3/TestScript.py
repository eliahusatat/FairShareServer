import numpy as np
import sys
import datetime

# from algorithm.Version3.ConsumptionGraph import ConsumptionGraph
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem
# from algorithm.Version3.GraphGenerator import GraphGenerator



def is_envy_free(v,z):
    for i in range(len(v)):
        agent_sum = 0
        for j in range(len(v[0])):
            agent_sum += z[i][j] * v[i][j]
        anther_agent_sum = 0
        for j in range(len(v)):
            anther_agent_sum = 0
            for k in range(len(v[0])):
                anther_agent_sum += z[j][k] * v[i][k]
            if(agent_sum < anther_agent_sum):
                print("the agent {}".format(i))
                print("the anther_agent {}".format(j))
                #return False
    return True


def str_to_matrix(str,parts):
    return np.asmatrix(np.array_split(np.fromstring(str, dtype=int, sep=',').tolist(), parts)).tolist()


if __name__ == '__main__':
    v = str_to_matrix(sys.argv[1],int(sys.argv[2]))
#     print(v)
#     print("This is the name of the script:", str_to_matrix(sys.argv[1],sys.argv[2]))
#     print("Number of arguments:", len(sys.argv))
#     print("numOfAgents:" , sys.argv[2])
#     print("numOfitems:" , sys.argv[3])
#     num_of_agents = 4
#     num_of_items = 10
#     max_item_value = 100
#     v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()

#     v =  [[150., 150. ,150. ,150., 150. ,250.],
#          [150., 150. ,150. ,150., 150. ,250.],
#          [150., 150. ,150. ,150., 150. ,250.]]


    fpap = FairEnvyFreeAllocationProblem(v)
#     fpap1 =  FairProportionalAllocationProblem(m)
#     print(v)
#     start = datetime.datetime.now()
    # THE TEST EXECUTION
    ans = fpap.find_allocation_with_min_shering()
    #ans = fpap1.find_allocation_with_min_shering()
    print(ans)
#     print(is_envy_free(v, ans))
#     end = datetime.datetime.now()
    # print("the number of graph: {}".format(count))
#     print("Total time for {} agents and {} items  :{}".format(num_of_agents, num_of_items, end - start))

