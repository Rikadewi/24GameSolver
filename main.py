from display import *

deck_maker()
randomize_card()
if __name__ == "__main__":
    hasil = []
    if len(sys.argv)==1:
        
        Solver24App().run()

    elif len(sys.argv)==3 :
        file_input = sys.argv[1]
        file_output = sys.argv[2]

        f = open(file_input, "r")
        contents = f.read()
        f.close()
        sorted_list = sorting(contents.split())
    else :
        print("Wrong input format")

    if len(sys.argv)==3 :
        s = calculate()
        
        # if len(sys.argv)==3 :
        f = open(file_output, "w+")
        f.write(s)
        f.close()
        contents = contents.split()
        contents[0]=int(contents[0])
        contents[1]=int(contents[1])
        contents[2]=int(contents[2])
        contents[3]=int(contents[3])

    print(score)