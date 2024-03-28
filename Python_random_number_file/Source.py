
import Output_r_file                                                               
import Input_r_file                                                                 
import Add_r_numbers                                                                






def main():

    
    name_file = Output_r_file.o_file()                                              
                                                                                    

    Input_r_file.i_file(name_file)                                                  
                                                                                    


    if(Add_r_numbers.a_file(name_file)):                                            
                                                                                    

        Input_r_file.i_file(name_file)                                              
                                                                                    



    print("\nThe program has ended\n")                                              
                                                                                    





main()                                                                              
