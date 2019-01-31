# -*- coding: utf-8 -*-

import request
import json
import os
from termcolor import colored




class profiles():


    def prompt():
        while True:
            print(colored('\nSelect the option you wish to do', attrs=['bold']))
            print('(1) Create a profile')
            print('(2) Update a profie')
            print('(3) Profiles')
            print('(4) Return to Main Menu')

            choice = input("»")
            choice = int(choice)


            if choice == 1:
                print('\nFill in the prompts!')
                profiles.create()

            elif choice == 2:
                print('\nCurrent Stored Profiles..')
                profiles.update()

            elif choice == 3:
                print('\nView Profiles.')
                profiles.view()
            elif choice ==4:
                print(colored('Main Menu of NoobPreme..','red',attrs=['bold']))
                from SUPREME import main
                main.menu()



    def create():

        os.getcwd() #gets current working directory
        user_name = os.getlogin() #gets username of system
        new_path = os.path.join(os.getcwd(), '/Users/%s/Library/Application Support' % user_name)#gets the cwd then sets the path to Application Support
        os.chdir(new_path) #makes the 'new_path' path the cwd
        folder_check = os.path.join(os.getcwd(),'NoobPreme')

        try:
           os.mkdir('NoobPreme') # makes folder in the cwd
        except:
           pass

        json_conceivement = os.path.join(folder_check,'NoobPreme.json')



        accounts = {}
        # if we have a file, deserialize content
        if os.path.exists(json_conceivement):
            try:
                with open(json_conceivement) as f:
                    accounts = dict(json.loads(f.read()))
            except:
                pass

        def createUser():
            while True:
                ProfileName = input("Profile Name »  ")

                if ProfileName in accounts.keys():
                    print('\n')
                    print(colored('Profile Name Exists Already..','red'))
                    return createUser()

                Name = input("Name » ")
                Email = input("Email » ")
                Telephone = input("Telephone » ")
                Adress1 = input("Adress » ")
                Zip = input("Postal Code » ")
                City = input("City » ")
                State = input("State(TX) » ")
                CC = input("Credit Card Number » ")
                EXP = input("EXP Date(MM/YYYY) » ")
                CVV = input("CVV » ")


                # this is how you assign the new account

                accounts[ProfileName] = {'Profile Name':ProfileName, "Name":Name,"Email":Email,"Tel":Telephone,
                                         "Address":Adress1,"Zip":Zip,"City":City,
                                         "State":State,"CreditCard":CC,"EXP":EXP,"CVV":CVV}


                autoSave()
                print(colored('Profile Saved Succesfully\n','green'))

                print('Do you want to add another profile(Y/N)')
                decison = input("»")

                if(decison == 'Y'):
                    pass
                else:
                    break

        def autoSave():
            with open(json_conceivement, "w") as outfile:
                # we convert here the dict to your list structure
                json.dump(list(accounts.items()), outfile)



        createUser()


    def update():


        user_name = os.getlogin() #gets username of system
        json_data = os.path.join(os.getcwd(), '/Users/%s/Library/Application Support/NoobPreme/NoobPreme.json' % user_name)#gets the cwd then sets the path to Application Support

        with open(json_data) as f:
            accounts = dict(json.loads(f.read()))
            for key in accounts:
                print(accounts[key]['Profile Name'])# accounts[keys] is used since we dont want to hard code the first value of the brackets

        while True:
            print('\nEnter the profile you wish to update..')
            profile_update = input("»")

            print('\nWhich value of %s do you want to update?' % profile_update)
            print(colored('Profile Name, Name, Email, Tel, Address, Zip, City, State, CreditCard, EXP, CVV', attrs=['bold'] ))
            update_want = input("»")


            print('\nCurrent data in %s concerning profile %s is..' %(update_want,profile_update))

            try:# formats the way the output will be shown.
                value = (accounts[profile_update][update_want])
                print(colored(value, attrs=['bold']))
            except:# is profile does not exist it will output contents in except
                print(colored('%s Was Not Shown Succesfully, Try Again\n','red') %profile_update )

            print('\nEnter the new value you want saved')
            update_value = input("»")

            final_Update = {update_want : update_value}
            try:
                value = (accounts[profile_update])
                value.update(final_Update)

                print(colored('Profile Updated Succesfully','green'))

                print('\nUpdated Profile:')

                profile = (accounts[profile_update]['Profile Name'])
                print("Profile: " + profile)

                alias = (accounts[profile_update]['Name'])
                print("Name: " + alias)

                email = (accounts[profile_update]['Email'])
                print("Email: " + email)

                telephone = (accounts[profile_update]['Tel'])
                print("Telephone Number: " + telephone)

                addy = (accounts[profile_update]['Address'])
                print("Address: " + addy)

                zip = (accounts[profile_update]['Zip'])
                print("Postal Code: " + zip)

                city = (accounts[profile_update]['City'])
                print("City: " + city)

                state = (accounts[profile_update]['State'])
                print("State: " + state)

                cc = (accounts[profile_update]['CreditCard'])
                print("CreditCard: " + cc)

                exp = (accounts[profile_update]['EXP'])
                print("EXP: " + exp)

                cvv = (accounts[profile_update]['CVV'])
                print("CVV: " + cvv)
                print()

            except:
                print(colored('%s Was Not Updated Succesfully, Try Again\n','red') %profile_update )

            print('Do you want to update another profile(Y/N)')
            decison = input("»")

            if(decison == 'Y'):
                pass
            else:
                break




    def view():

        user_name = os.getlogin() #gets username of system
        json_data = os.path.join(os.getcwd(), '/Users/%s/Library/Application Support/NoobPreme/NoobPreme.json' % user_name)#gets the cwd then sets the path to Application Support
        #os.chdir(json_data) #makes the 'new_path' path the cwd

        with open(json_data) as f:
            accounts = dict(json.loads(f.read()))
            for key in accounts:
                print(accounts[key]['Profile Name']) # "accounts[keys] is used since we dont want to hard code the first value of the brackets"
                #shell_script = accounts['OswaldoCredit']#['Profile Name']
                #print(shell_script)

            while True:
                print('\nType the profile you wish the view.')
                view_profile = input("»")# inputting value to retrive certain profiles info
                print()

                try:# formats the way the output will be shown.
                    profile = (accounts[view_profile]['Profile Name'])
                    print("Profile: " + profile)

                    alias = (accounts[view_profile]['Name'])
                    print("Name: " + alias)

                    email = (accounts[view_profile]['Email'])
                    print("Email: " + email)

                    telephone = (accounts[view_profile]['Tel'])
                    print("Telephone Number: " + telephone)

                    addy = (accounts[view_profile]['Address'])
                    print("Address: " + addy)

                    zip = (accounts[view_profile]['Zip'])
                    print("Postal Code: " + zip)

                    city = (accounts[view_profile]['City'])
                    print("City: " + city)

                    state = (accounts[view_profile]['State'])
                    print("State: " + state)

                    cc = (accounts[view_profile]['CreditCard'])
                    print("CreditCard: " + cc)

                    exp = (accounts[view_profile]['EXP'])
                    print("EXP: " + exp)

                    cvv = (accounts[view_profile]['CVV'])
                    print("CVV: " + cvv)

                    print(colored('Profile Shown Succesfully\n','green'))

                except:# is profile does not exist it will output contents in except
                    print(colored('Profile Was Not Shown Succesfully, Try Again\n','red'))

                print('Do you want to view another profile(Y/N)')
                decison = input("»")

                if(decison == 'Y'):
                    pass
                else:
                    break





#profiles.prompt()
