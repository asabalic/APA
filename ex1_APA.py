import math
import matplotlib.pyplot as plt

def plotting_functions(mylist):
    """Plots factorial, power of two, quadratic, linear, square root and log function for given list"""

    result_A=[]
    result_B=[]
    result_C=[]
    result_D=[]
    result_E=[]
    result_F=[]
    for i in mylist:
        a = math.factorial(i)
        result_A.append(a)
        b = 2**i
        result_B.append(b)
        c = i**2
        result_C.append(c)
        d = i
        result_D.append(d)
        e = math.sqrt(i)
        result_E.append(e)
        f = math.log(i)
        result_F.append(f)


    fig,ax=plt.subplots()
    figsize= (15,10)
    plt.xlim(0,60)
    plt.ylim(0,350)

    plot1, = ax.plot(mylist, result_A, "red", label="data1")
    plot2, = ax.plot(mylist, result_B, "skyblue")
    plot3, = ax.plot(mylist, result_C, "green")
    plot4, = ax.plot(mylist, result_D, "black")
    plot5, = ax.plot(mylist, result_E, "orange")
    plot6, = ax.plot(mylist, result_F, "blue")

    plt.legend([plot1,plot2, plot3, plot4, plot5, plot6],["n!", "2^n","n^2", "n", "sqrt(n)", "log(n)"])

    plt.show()




if __name__ == "__main__":
    test_list= [1,10,50,100]
    plotting_functions(test_list)