import sys
import math 

def defBegin():
    return "<defs>\n\t<radialGradient id=\"Gradient\"\n"

def defCenter():
    return "\t\tcx=\"0.5\" cy=\"0.5\" r=\"0.2\"\n"

def defStyle(cor1, cor2):
    return "\t\tspreadMethod=\"reflect\">\n\t\t<stop offset=\"0%\" stop-color=\"{c1}\"/>\n\t\t<stop offset=\"100%\" stop-color=\"{c2}\"/>\n".format(c1 = cor1, c2 = cor2)

def valuesFX():
    list = []
    for i in range(3600):
        list.append(0.16 * math.cos(i/10) + 0.5)
    return ';'.join(map(str, list))

def defAnimateX():
    return "\t\t<animate attributeName=\"fx\" values=\"" + str(valuesFX()) + "\" dur=\"2400s\" repeatCount=\"indefinite\"/>\n" 

def valuesFY():
    list = []
    for i in range(3600):
        list.append(0.16 * math.sin(i/10) + 0.5)
    return ';'.join(map(str, list))

def defAnimateY():
    return "\t\t<animate attributeName=\"fy\" values=\"" + str(valuesFY()) + "\" dur=\"2400s\" repeatCount=\"indefinite\"/>\n" 

def defAnimate():
    return str(defAnimateX()) + str(defAnimateY())

def defEnd():
    return "\t</radialGradient>\n</defs>\n"

def svgDefs(c1, c2):
    return str(defBegin()) + str(defCenter()) + str(defStyle(c1, c2)) + str(defAnimate()) + str(defEnd())

def svgBegin(l, a):
    return "<svg width='{w}' height='{h}' xmlns='http://www.w3.org/2000/svg'>\n".format(w = l, h = a)

def svgRect(x, y, l ,a):
    return "<rect x='{X}' y='{Y}' rx='15' ry='15' width='{w}' height='{h}' fill=\"url(#Gradient)\" />\n".format(X = x, Y = y, w = l, h = a)

def svgAll(l, a, c1, c2):
    return str(svgDefs(c1, c2)) + str(svgRect(25, 25, l, a))

def svgEnd():
    return "</svg>"

def main():
    w = sys.argv[1] 
    h = sys.argv[2] 
    cor_1 = sys.argv[3] 
    cor_2 = sys.argv[4]
    string = ' '.join(map(str, [svgBegin(w, h), svgAll(w, h, cor_1, cor_2), svgEnd()]))
    print(string)

if __name__ == "__main__":
    main()