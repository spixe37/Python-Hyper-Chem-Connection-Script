import pyhcs

def main():
    if not pyhcs.connect():
        return

    # pyhcs.exec_text("window-color black")
    pyhcs.exec_text("open-file " + "D:\\C60.HIN")


    pyhcs.exec_text("menu-select-molecules")
    pyhcs.exec_text("select-atom 1,1")
    pyhcs.exec_text("translate-selection 0,0,0")

    r = 2
    v = 5

    z = 4

    for i in range(z):
        for j in range(z):
            for k in range(z):
                # text = "select-atom 1, {0}".format(i+1+j)
                pyhcs.exec_text("menu-edit-copy")
                pyhcs.exec_text("menu-edit-paste")
                pyhcs.exec_text("select-none")
                pyhcs.exec_text("select-atom 1,{0}".format(r))
                pyhcs.exec_text("translate-selection {0},{1},{2}".format(i*v, j*v, k*v))
                r += 1

    
    pyhcs.disconnect()

if __name__ == '__main__':
    main()