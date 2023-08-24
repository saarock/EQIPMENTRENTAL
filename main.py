import sys
import datetime, os

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



# To checked already rented somethings
        # with open('datas.txt', 'r+') as file:
        #     q = file.readlines()
        #     if(len(q) > 0):
        #         print('You already rented something to rent again you need to return first.')
        #         self.return_rental_things()


        



        c_name = input('Costumer Name: ')
        q_ = eq.split(',')
        print(q_)
        quantity = input(f'Your Equipment: {eq} How many Quantity you want out of {q_[3]}')
        if(int(quantity) > int(q_[3]) or int(quantity)<= 0):
            print('Quantity not available try again')
            self.rental_things()
        else:
            current_date = datetime.datetime.now()
            increased_date = current_date + datetime.timedelta(days=5)
            Due_date = increased_date.strftime("%Y:%m:%d")
 
            # checked that the equipment is already rented
            y_n = os.path.exists(f'{q_[0]}.txt')
            if(y_n):
                file_path = f'{q_[0]}.txt'
                with open(file_path, 'r') as file:
                    all_datas = file.readlines()

                updated = False

                for i, line in enumerate(all_datas):
                    if line.strip().startswith("Total Quantity:"):
                      v_ = line.split(',')
        
                      if len(v_) >= 2:
                          last_value = int(v_[-1].strip()) + int(quantity)
                          v_[-1] = f'{last_value}\n'
                          all_datas[i] = ', '.join(v_)
                          updated = True
                          break

                if not updated:
                    print("Total Quantity line not found in the file.")

# Write the updated content back to the file
                with open(file_path, 'w') as file_again:
                    file_again.writelines(all_datas)

                import write  # This import seems unnecessary and might lead to circular imports

# Assuming the 'write.update_equipment_data' function is correct
                write.update_equipment_data('equipment_data.txt', q_[0], int(quantity))
                return

                
        #         with open(f'{q_[0]}.txt', 'r') as file:
        #             all_datas = file.readlines()
        #             print(all_datas[-2])
        #             v = all_datas[-2]
        #             v_  = v.split(',')

        #             if len(v_) >= 2:  # Ensure there are at least 2 parts in the split
        # # Update the quantity value and rewrite the line
    
        #                  last_value  = int(v_[-1].strip()) + int(quantity)
        #                  new_quantity = int(quantity) + int(v_[-1].strip())  # Strip to remove any whitespace or newline
        #                 #  return
        #                  all_datas[-1] = f'{v_[0]}, {last_value}'  # Assuming v_[0] is the label before quantity
        #                  print(last_value, 'THISIS MY LAST VALUE')
        
        # # Write the updated content back to the file
        #                  with open(f'{q_[0]}.txt', 'w') as file_again:
        #                       print(all_datas, 'Helll bhaiho')
        #                       file_again.writelines(all_datas)
        #                  import write
        #                  write.update_equipment_data('equipment_data.txt', q_[0], int(quantity))
        #                  return

                    # print(v_, 'yes')
                    # all_datas[-1] = f'{int(quantity)+int(v_[-1])}'
                    # print(all_datas, 'I AM')
                    # with open(f'{q_[0]}.txt' , 'w') as file_again:
                    #     file_again.writelines(all_datas)
                
                    # return
                #


            
 
            with open(f'{q_[0]}.txt', 'w') as file:
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
            import write
            write.update_equipment_data('equipment_data.txt', q_[0], int(quantity))
            
    


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
# let.check_fine()

# step 3 (CALL THE FUNCTION TO SHOW THE OPTION)
let.show_options()
