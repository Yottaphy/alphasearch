import numpy as np
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})

superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"
elements    = {0:"n", 1:"H", 2:"He", 3:"Li", 4:"Be", 5:"B", 6:"C", 7:"N", 8:"O", 9:"F", 10:"Ne", 11:"Na", 12:"Mg", 13:"Al", 14:"Si", 15:"P", 16:"S", 17:"Cl", 18:"Ar", 19:"K", 20:"Ca", 21:"Sc", 22:"Ti", 23:"V", 24:"Cr", 25:"Mn", 26:"Fe", 27:"Co", 28:"Ni", 29:"Cu", 30:"Zn", 31:"Ga", 32:"Ge", 33:"As", 34:"Se", 35:"Br", 36:"Kr", 37:"Rb", 38:"Sr", 39:"Y", 40:"Zr", 41:"Nb", 42:"Mo", 43:"Tc", 44:"Ru", 45:"Rh", 46:"Pd", 47:"Ag", 48:"Cd", 49:"In", 50:"Sn", 51:"Sb", 52:"Te", 53:"I", 54:"Xe", 55:"Cs", 56:"Ba", 57:"La", 58:"Ce", 59:"Pr", 60:"Nd", 61:"Pm", 62:"Sm", 63:"Eu", 64:"Gd", 65:"Tb", 66:"Dy", 67:"Ho", 68:"Er", 69:"Tm", 70:"Yb", 71:"Lu", 72:"Hf", 73:"Ta", 74:"W", 75:"Re", 76:"Os", 77:"Ir", 78:"Pt", 79:"Au", 80:"Hg", 81:"Tl", 82:"Pb", 83:"Bi", 84:"Po", 85:"At", 86:"Rn", 87:"Fr", 88:"Ra", 89:"Ac", 90:"Th", 91:"Pa", 92:"U", 93:"Np", 94:"Pu", 95:"Am", 96:"Cm", 97:"Bk", 98:"Cf", 99:"Es", 100:"Fm", 101:"Md", 102:"No", 103:"Lr", 104:"Rf", 105:"Db", 106:"Sg", 107:"Bh", 108:"Hs", 109:"Mt", 110:"Ds", 111:"Rg", 112:"Cn", 113:"Nh", 114:"Fl", 115:"Mc", 116:"Lv", 117:"Ts", 118:"Og"}

def makeSuperscript(number):
    result = ''
    if number >=100:
        cent   = int(number/100)
        number = number%100
        result += superscript[cent]
        if number < 10: result += superscript[0]
    if number >= 10: 
        dec    = int(number/10)
        number = number%10
        result += superscript[dec]
    
    result += superscript[number]
    return result


l, n, z, e, d = np.genfromtxt( "alphas.txt", unpack=True, skip_header=1, skip_footer=0, autostrip=True)

for i in range(0,6655):
    if n[i] > 126 and n[i] < 156 and z[i] > 83 and z[i] < 103:
        print(n[i], z[i], e[i], d[i])
        
class Nucleus:
    def __init__(self, n, z):
        self.n           = n         
        self.z           = z         
        self.a           = n+z       
        #self.alpha       =         
        #self.delta_alpha =          

    def daughter(self):
        return Nucleus(self.n-2, self.z-2)

    def print(self):
        a = makeSuperscript(self.a)
        z = self.z
        symbol = elements[z]
        print(a+symbol)
        
if __name__ == '__main__':
    
    Bi209 = Nucleus(83, 126)
    Bi209.print()
