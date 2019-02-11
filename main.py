from display import *

if __name__ == "__main__":
    #frontend 1
    if len(sys.argv)==1:
        deck_maker()
        randomize_card()
        Solver24App().run()
    #frontend 3
    elif len(sys.argv)==3 :
        file_input = sys.argv[1]
        file_output = sys.argv[2]

        f = open(file_input, "r")
        contents = f.read()
        f.close()
        contents = contents.split()
        contents[0]=int(contents[0])
        contents[1]=int(contents[1])
        contents[2]=int(contents[2])
        contents[3]=int(contents[3])
        sorted_list = sorting(contents)
        s, true24, score_actual = calculate(sorted_list)
        print(score_actual)
        f = open(file_output, "w+")
        f.write(s)
        f.write("\nscore = " + str(score_actual))
        f.close()
        print("Hasil telah berhasil ditulis di file " + file_output)
    else :
        print("Wrong input format")
        
        