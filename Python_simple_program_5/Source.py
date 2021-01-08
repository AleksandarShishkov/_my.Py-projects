


def main():                                                                     # function main

    rect1_width = float(input("\nEnter the width of the first rectangle > "))   # a float to hold width1
    rect1_lenght = float(input("Enter the lenght of the first rectangle > "))   # a float to hold lenght1

    rect2_width = float(input("Enter the width of the second rectangle > "))    # a float to hold width2
    rect2_lenght = float(input("Enter the lenght of the second rectangle > "))  # a float to hold lenght2

    compare_areas(rect1_width, rect1_lenght, rect2_width, rect2_lenght)         # calling compare_areas function



def compare_areas(width1, lenght1, width2, lenght2):                            # compare_areas function which takes 4 float parameters
                                                                                # which calculates and compares the areas of the two
                                                                                # rectangles with relational if-else statement

    area1 = width1 * lenght1                                                    # calculating area1
    area2 = width2 * lenght2                                                    # calculating area2

    if(area1 > area2):
        print("\nArea1 (", area1, ") is greater than area2 (", area2, ")\n")
    else:
        print("\nArea2 (", area2, ") is greater than area 1 (", area1, ")\n")
        

main()                                                                          # calling main()

