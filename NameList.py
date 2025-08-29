#Email: abkariyyah.ahmed31@myhunter.cuny.edu
#Name: Abkariyyah Ahmed
#Date: Feb 25, 2025
#This program outputs: Name List



def main():
    input_names = input("Please enter your list of names: ")
    names = input_names.split('; ')
    
    print()
    
    for full_name in names:
        parts = full_name.split(', ')
        last_name = parts[0]
        first_name = parts[1].split()[0]  # Get only the first part of the first name
        
        first_initial = first_name[0]
        print(f"{first_initial}. {last_name}")
    
    print("\nThank you for using my name organizer!")

if __name__ == "__main__":
    main()
