#Abkariyyah Ahmed
#abkariyyah.ahmed31@myhunter.cuny.edu
#program 45

import pandas as pd

def make_addr_df(Last, First, emails):
    Last = Last.split(" ")
    First = First.split(" ")
    emails = emails.split(" ")
    data = {
        "Last": Last,
        "First": First,
        "emails": emails
    }
    df = pd.DataFrame(data)
    return df

def main():
    Last = input("Enter last names: ")
    First = input("Enter first names: ")
    emails = input("Enter emails: ")
    print(make_addr_df(Last, First, emails))

if __name__ == "__main__":
    main()
