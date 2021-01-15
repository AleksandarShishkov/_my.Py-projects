



        # A Python program that prompts 
        # the user to create a file and to
        # write user-defined number of integers
        # into it.
        #
        # It then opens the file and reads the
        # data into a list.
        #
        # The user can search for a integer 
        # on the liset or to quit by pressin '-1'.




import output_file                                                                  # importing the output_file module
import input_file                                                                   # importing the input_file module
import Search_list                                                                  # impoting the Search_list module


def main():


    file_name = output_file.open_file()                                             # calling the open_file() function, assigning
                                                                                    # the returned value to a variable

    list_num = input_file.read_file(file_name)                                      # calling read_file() function with a parameter
                                                                                    # for the name of the file and assigning the reuturned
                                                                                    # value a variable


    print("\nEnter the number you are searching for or press '-1' to quit> ")       # prompting the user to enter an integer 
    num = int(input())                                                              

    while(num != -1):                                                               # entering the sentinel-controlled loop


        Search_list.serch(list_num, num)                                            # calling search() function with parameters
                                                                                    # for the list and thenputed number


        print("\nEnter the number you are searching for or press '-1' to quit> ")   # promting the user to enter another integer
        num = int(input())



    print("\nThe program has ended!\n")                                             # printing a message indicating that the
                                                                                    # program has ended




main()                                                                              # calling the main() function


