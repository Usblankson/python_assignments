# import Regular Expression ( REGEX)
import re

# string = "geeks for geeks"
# sub_str ="geek"

string = input("Enter the Main String: ")
sub_str = input("\nEnter the Substring (char) to test: ")
  
# re.search() returns a Match object if there is a match anywhere in the string
if re.search(sub_str,string ):
    print("\nYES, String '{0}' is present in string '{1}' \n" .format(sub_str, string))
else:
    print("\nNO, String '{0}' is not present in string {1}\n" .format(sub_str, string) )       
# Main code body

