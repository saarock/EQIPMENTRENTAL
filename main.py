import sys
import datetime

class shop_rental:
    def __init__(self, options):
        self.options = options

    

    def clear_fine(self):
        try:
            import clearfine
            clearfine.clss()
        except Exception as e:
            print(e)

    
    def check_fine(self):
        '''
        Checked the fine
        '''
        try:
            with open('fine.txt', 'r') as file:
                a = file.readlines()
                b_ = a[4].split('=')
                b__ = b_[1].replace('$', '')
                b = b__.strip()

                if(int(b) >= 1):
                    print('You have fine clear it first')
                    file.close()
                    self.clear_fine()
                
                
        except Exception as e:
            print(e)

    
    def return_rental_things(self):
        '''
        return the rental things
        '''
        try:
            print('Do you want to return: ')
            print('1 for Yes\n 2 for No')
            y_n = input(':')
            if(int(y_n) == 1):
                import return_eq
                return_eq.return_eqp()
            elif(int(y_n) == 2):
                self.exist()
            else:
                print('Try again')
                self.return_rental_things()
        except Exception as e:
                print('Try again')
                self.return_rental_things()

    


    def book(self, eq, nn):
      try:
        '''
        algorithm for booking equipments
        '''

        with open('datas.txt', 'r+') as file:
            q = file.readlines()
            if(len(q) > 0):
                print('You already rented something to rent again you need to return first.')
                self.return_rental_things()


        



        c_name = input('Costumer Name: ')
        q_ = eq.split(',')
        print(q_)
        quantity = input(f'Your Equipment: {eq} How many Quantity you want out of {q_[3]}')
        if(int(quantity) > int(q_[3]) or int(quantity)<= 0):
            self.book()
        else:
            current_date = datetime.datetime.now()
            increased_date = current_date + datetime.timedelta(days=5)
            Due_date = increased_date.strftime("%Y:%m:%d")
 
            with open('datas.txt', 'w') as file:
                lines = [
                    f'Custumer Name: {c_name}\n',
                    f'Equipment: {q_[0]}\n',
                    f'Brand Name: {q_[1]}\n'
                    f'Rental Date= {datetime.datetime.now()}\n',
                    f'Due Date= {Due_date}\n'
                    f'Total Amount: ${q_[2]}\n',
                    f'Total Quantity:, {quantity}\n '
                ]

                file.writelines(lines)
                file.close()
                print('Done Pleased after poper used return to us respectfully!')
            

# Update after booking
            import update
            update.update_equipment_data('equipment_data.txt', q_[0], int(quantity))
            
    


      except Exception as e:
          print(e)


        
        
        
    def rental_things(self):
        '''
        rental things        
        '''
        try:
            n = 0
            with open('equipment_data.txt') as file:
                eq = file.readlines()
                for i in eq:
                    n+=1
                    print(f'{n}: ',i)
                name_of_equipment = input('Equipment Number: ')
                if(int(name_of_equipment) == 1):
                    self.book(eq[0], 0)
                elif(int(name_of_equipment) == 2):
                    self.book(eq[1], 1)
                elif(int(name_of_equipment) == 3):
                    self.book(eq[2], 2)
                elif(int(name_of_equipment) == 4):
                    self.book(eq[3], 3)
                elif(int(name_of_equipment) == 5):
                    self.book(eq[4], 4)
                    
        except Exception as e:
            print(e)
        




    
    def exist(self):
        '''
        Exist the program
        '''
        try:
            sys.exit()
        except Exception as e:
            print(e)



    def show_options(self):
        '''
        Show the option 
        '''
        try:
            for i in self.options:
                print(i)
            choose = input('Choose the option through the numbers: 1 or 2 or 3:  ')
            if(int(choose) == 1):
                # Calling the rental_things functions where user can rent the things
                self.rental_things()
            elif(int(choose) == 2):
                # Calling the function for returning the rental things
                self.return_rental_things()
            elif(int(choose) == 3):
                # Calling the exist function
                self.exist()
            else:
                print('Try again')
                # Using recursion if any things worng
                self.show_options()

        except Exception as e:
            print('Try again')
            self.show_options()

    



# Step 1 (CALL THE CLASS)
let = shop_rental(['1: Rent Equipment', '2: Return Rent Equipment', '3: Exist'])


# Step 2(Check the fine)
let.check_fine()

# step 3 (CALL THE FUNCTION TO SHOW THE OPTION)
let.show_options()
