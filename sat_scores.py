import school_scores
import matplotlib.pyplot as plt
import numpy as np


list_of_record = school_scores.get_all()
print(len(list_of_record))


hun = []
e_h = []
s_e = []
f_s = []
t_f = []
less_than_20 = []


for l in list_of_record:
    hun.append(l["Family Income"]["More than 100k"]["Math"])
    e_h.append(l["Family Income"]["Between 80-100k"]["Math"])
    s_e.append(l["Family Income"]["Between 60-80k"]["Math"])
    f_s.append(l["Family Income"]["Between 40-60k"]["Math"])
    t_f.append(l["Family Income"]["Between 20-40k"]["Math"])
    less_than_20.append(l["Family Income"]["Less than 20k"]["Math"])
    

def display():
    # Data for plotting

    t = np.arange(0, 600)

    # Note that using plt.subplots below is equivalent to using
    # fig = plt.figure() and then ax = fig.add_subplot(111)
    fig, ax = plt.subplots()
    plt.xlim(0, 100)

    ax.plot(hun)
    ax.plot(e_h)
    ax.plot(s_e)
    ax.plot(f_s)
    ax.plot(t_f)
    ax.plot(less_than_20)

    ax.set(xlabel='Income', ylabel='SAT scores',
           title='How income affects SAT scores')
    ax.grid()

    fig.savefig("test.png")
    plt.show()


display()


























    #print(item["GPA"]["B"]["Verbal"])



    #print(item["State"]["Code"], item["Year"])
