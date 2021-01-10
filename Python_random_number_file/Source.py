



        #
        # This Python program creates a .txt file with
        # user-defined name and writes to it randomly
        # generated numbers which number and limit are
        # also define by the user.
        #
        # The program displays the numbers, calculates their
        # total and keep a running count for the number of
        # values read.
        #
        # It also prompts the user to select whether additional
        # numbers will be applied.
        #







import Output_r_file                                                                # importing Output_r_file
import Input_r_file                                                                 # importing Input_r_file
import Add_r_numbers                                                                # importing Add_r_numbers






def main():

    
    name_file = Output_r_file.o_file()                                              # calling o_file() function and assigning
                                                                                    # the returned string to name_file

    Input_r_file.i_file(name_file)                                                  # calling i_file() function with parameter for
                                                                                    # the file name


    if(Add_r_numbers.a_file(name_file)):                                            # calling a_file() function with parameter for
                                                                                    # the file name

        Input_r_file.i_file(name_file)                                              # calling i_file() function with parameter for
                                                                                    # the file name



    print("\nThe program has ended\n")                                              # printing message indicating that the
                                                                                    # program has ended





main()                                                                              # calling the main() function
