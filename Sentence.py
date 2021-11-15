
subject = ["Samuel", "Akpan", "Udo", "Etukudo", "Blankson", "Wayne", "Gideon", "Ediomo", "Blessing", "Ada", "Peter", "Gibson", "Paul", "Lydia", "Donald"]

predicate = ["ran","cooked", " wrote","sang","came"]





def predict(sub):
    pred = input("Enter the predicate: \n\n")
    if(pred in predicate):
        print("You got the predicate\n\n")
        
        sentence = sub+" "+ pred
        
        print("Sentence formed = ", sentence)
    else:
        print("\nError: The Predicate is not available in the array\n")
        print("Please Try Again: \n")
        print("Available Subjects are: \n", predicate, " \n\n")
        predict(sub)
        
def subj():      
    sub = input("Enter a subject: \n\n");

    if(sub in  subject):
        print("You have gotten the Subject right\n\n")
        predict(sub)
        
    else:
        print("Error: The Subject is not available in the ArrayList\n\n") 
        print("Available Subjects are: \n", subject, " \n\n")
        subj()


# Main program

subj()

        
        