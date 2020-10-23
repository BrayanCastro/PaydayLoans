# Author: Brayan Castro
# Class:  COMP 141-10am
# Project: Program 2
# Pledge: I have neither given nor received unauthorized aid on this program.
# Description: For this program I have developed a program that calculates the APR of a payday loan in the two scenarios listed below. Either :  "(1) I know the total loan amount or amount the borrower will receive , the total fee or cost of the loan, and the length of the loan (in days or months)" or "(2) I know the fee in dollars (or percent) for every 100 dollars borrowed and the length of the loan (in days or months"




#my main function 
def main(): 
  
  #Introduction to calculator
  print("Welcome to the Payday loan APR calculator.")   
  print("Typically payday loan companies give information in one of two ways.")
  print("Please tell us so we can calculate APR by Selecting which one that fits your situation.")  
  print("(1) I know the total loan amount or amount the borrower will receive , the total fee or cost of the loan, and the length of the loan (in days or months)")
  print("(2) I know the fee in dollars (or percent) for every 100 dollars borrowed and the length of the loan (in days or months")
  
  #Asks user what way they chose to take out their payday loan.  
  info = input("How was the information given to you (1) or (2)? ") 
  
  #The code that will run if user chose option 1
  if info == "1":
      total_loan_amount= float(input("What is the total loan amount? "))
      total_finance_charge= float(input("What is the total fee or finance charge for the loan? "))
      loan_length= input("Where you given the loan length in days or months?  Enter d or m ")
      
                            #The code that will run if user chose days
      if loan_length == "d":
          duration_in_days = int(input("How many days will you have the loan? "))            
          apr1 = (((total_finance_charge/total_loan_amount)*365)/duration_in_days)*100 
                      
          print("Your", ("%.1f" % duration_in_days), "day loan has an APR of", ("%.1f" % apr1), "%")
          
          
                            #The code that will run if user chose months      
      elif loan_length == "m":
          duration_in_months = int(input("How many months will you have the loan? "))   
          apr6 = (((total_finance_charge/total_loan_amount)*12)/duration_in_months)*100 
                       
          print("Your", ("%.1f" % duration_in_months), "month loan has an APR of", ("%.1f" % apr6), "%")
      
      else:
        print("invalid input")
        
        
        
      
  #The code that will run if user chose option 2    
  elif info == "2":
      typee = input("Where you given a percentage rate or a set finance charge for every 100 USD? Enter p or c: ")
      if typee == "c":
          total_finance_charge2= float(input("What is the flat fee for each 100 USD borrowed? "))
          loan_length2= input("Where you given the loan length in days or months?  Enter d or m ")
          
          #Will split up into wheather the user chose days or months
          
                            #The code that will run if user chose days          
          if loan_length2 == "d":
              duration_in_days2 = int(input("How many days will you have the loan? "))
              apr2 = (((total_finance_charge2/100)*365)/duration_in_days2)*100 
                                           
              print("Your", ("%.1f" % duration_in_days2), "day loan has an APR of", ("%.1f" % apr2), "%")
              

                            #The code that will run if user chose months              
          elif loan_length2 == "m":
              duration_in_months = int(input("How many days will you have the loan? "))
              apr5 = (((total_finance_charge/100)*12)/duration_in_months)*100 
                                           
              print("Your", ("%.1f" % duration_in_months), "month loan has an APR of", ("%.1f" % apr5), "%")
          else: 
            print("invalid input")
            
            
            
                            #The code that will run if user chose percentage            
      elif typee == "p":
          total_finance_charge3= float(input("What was the percentage for each 100 USD borrowed? "))
          loan_length3= input("Where you given the loan length in days or months?  Enter d or m ")
          
                            #The code that will run if user chose days
          if loan_length3 == "d":
              duration_in_days3= int(input("How many days will you have the loan? "))
              apr3 = (((total_finance_charge3/100)*365)/duration_in_days3)*100
              
              print("Your", ("%.1f" % duration_in_days3), "day loan has an APR of", ("%.1f" % apr3), "%")
              
                            #The code that will run if user chose months          
          elif loan_length3 == "m":  
              duration_in_months2 = int(input("How many months will you have the loan? "))
              apr4 = (((total_finance_charge3/100)*12)/duration_in_months2)*100 
                                           
              print("Your", ("%.1f" % duration_in_months2), "month loan has an APR of", ("%.1f" % apr4), "%")
              
          else: 
            print("invalid input")
              
      else:
          print("Invalid input")
                

  else:
    print("Invalid input")
       
    
  
main()





