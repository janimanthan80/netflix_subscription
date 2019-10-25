print("\t\t\t\t\t\t\\\\\\\\Welcome To My NetFlix Page\\\\\\\\")

class myreg():

  def plan():

    name = input("Enter Your Name : ")

    email1 = input("\nEnter Your Email : ")
    password1 = input("\nEnter Your Password : ")

    msg = print("\nWelcome To MyPage " + name.upper() + "\n\nYou Have Successfully Registered.")

  
                        #login

    print("\n\t\t\t\t\t\t\\\\\\\\Welcome To Login Page\\\\\\\\")

    while True:

      email2 = input("\nEnter your Email : ")#registered email and login email must be same
      password2 = input("\nEnter Your Password : ")#registered password ans login password must be same

      if email1 == email2 and password1 == password2:
        print("\nLogin Successful\n\nWelcome To Our Page")
        
        
        print("\n\t\t\t\t\t\t\\\\\\\\Choose Your Monthly Plan\\\\\\\\")
        plans_dict = {"a" : "30", "b" : "40", "c" : "50"}

        print("\n30zl\t\t\t\t40zl\t\t\t\t50zl\n\nHD(No)\t\t\t\tHD(Yes)\t\t\t\tHD(Yes)\n\nUltraHD(No)\t\t\tUltraHD(No)\t\t\tUltraHD(Yes)\n\nScreenPlay(1)\t\tScreenPlay(2)\t\tScreenPlay(4)")

       # while True:
        choose_plan = input("\n\nChoose Your Monthly Plan From The Option Above(In Number) : ") #You can choose any plan from above 3 options
      
        if choose_plan == plans_dict["a"]:
          print("\nYou have choosen " + plans_dict["a"] +"zl plan")
        elif choose_plan == plans_dict["b"]:
          print("\nYou have choosen " + plans_dict["b"] +"zl plan")
        elif choose_plan == plans_dict["c"]:
          print("\nYou have choosen " + plans_dict["c"] +"zl plan")  
        else:
          print("\nSorry You Have Entered Invalid Number\n\nPlease Try Again")

        paymentdict = {"paypal" : "1",
                       "creditordebitcard" : "2",
                       "reedemcode" : "3"}

        print("\nMethod Of Payment\n\n(1)Paypal\t\t(2)Credit/DebitCard\t\t(3)ReedemCode")

        method_payment = {"paypal" : email1,
                    "c/d" : "1234567891234567",
                    "code" : "JACK123"}  
        while True:

          method = input("\nChoose Your Payment Method : ") #choose payment method in number

          if method == "1":

            print("\t\t\nYou Have Choosen 'Paypal' as Your Payment Method")

            while True:
              
              print("\nyour paypal email should be same as your gmail\n")
              details = input("\nEnter Your Paypal Email To Procceed Payment : ")#paypal email should be same as dictionary named(method_payment)

              if details == method_payment["paypal"]:

                print("\nPayment Accepted \n\nCongratulations " + name.upper() + ", Enjoy Your Streams.")

                break

              else:
                print("\nWrong Number try again")  
                        

          elif method == "2":

            print("\nYou Have Choosen 'Credit/Debitcard' as Your Payment Method")

            while True:

              details1 = input("\nEnter Your Credit/Debit Card Number : ") #card number should be same as dictionary named(method_payment)

              validetails = input("\nEnter Validity (ex. Month/Year) : ")

              cvvdetails = input("\nEnter CVV Number : ")

              if details1 == method_payment["c/d"]:
                print("\nPayment Accepted \n\nCongratulations " + name.upper() + ", Enjoy Your Streams.")

              break  

            else:
              print("\nWrong Numbertry again")    

          elif method == "3":

            print("\nYou Have Choosen 'ReedemCode' as Your Payment Method") #enter any code 

            while True:

              details3 = input("\nEnter Your GiftCode to Procceed Payment : ") #reeedem code should be same as dictionary named(method_payment)

              if details3 == method_payment["code"]:

                print("\nPayment Accepted \n\nCongratulations " + name.upper() + ", Enjoy Your Streams.")

                break

              else:

                print("\nwrong number try again")       

            break      

        else:
          print("\ntry again") 

        break   

      else:
        print("\nYou Have Entered Wrong Email Or Password Please Try Again")  

  plan()   
    
myreg() 
