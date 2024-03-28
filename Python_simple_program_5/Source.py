


def main():                                                                     

    rect1_width = float(input("\nEnter the width of the first rectangle > "))   
    rect1_lenght = float(input("Enter the lenght of the first rectangle > "))   

    rect2_width = float(input("Enter the width of the second rectangle > "))    
    rect2_lenght = float(input("Enter the lenght of the second rectangle > "))  

    compare_areas(rect1_width, rect1_lenght, rect2_width, rect2_lenght)         



def compare_areas(width1, lenght1, width2, lenght2):                            
                                                                                
                                                                                

    area1 = width1 * lenght1                                                    
    area2 = width2 * lenght2                                                    
    if(area1 > area2):
        print("\nArea1 (", area1, ") is greater than area2 (", area2, ")\n")
    else:
        print("\nArea2 (", area2, ") is greater than area 1 (", area1, ")\n")
        

main()                                                                          

