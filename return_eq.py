import datetime, os

def return_eqp():
    try:
        # take equipment name
        eq_name = input('Enter rental equipment name.')
        y_n = os.path.exists(f'{eq_name}.txt')
        if(y_n):
         return_quantity = input('Enter return quantity: ')


         with open(f'{eq_name}.txt', 'r+') as file:
            a = file.readlines()
            q__ = a[-2].split(',')
            q___ = q__[-1]
            print(int(q___.strip()), 'thid')
            if(int(q___.strip()) < int(return_quantity)):
                print('Out of Quantity try again')
                return_eqp()



            # IF all right
            y_n = os.path.exists(f'{eq_name}.txt')
            if(y_n):
                file_path = f'{eq_name}.txt'
                with open(file_path, 'r') as file:
                    all_datas = file.readlines()

                updated = False

                for i, line in enumerate(all_datas):
                    if line.strip().startswith("Total Quantity:"):
                      v_ = line.split(',')
        
                      if len(v_) >= 2:
                          last_value = int(v_[-1].strip()) - int(return_quantity)
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
                write.update_equipments_plus(f'equipment_data.txt', eq_name  ,int(return_quantity))
                print(f'equipment_data.txt', eq_name  ,int(return_quantity))
                # return



            


















                

            b = a[1].split(':')
            c = a[4].split('=')
            due_date_string = c[1].strip() #remove the whitspace
            print('Debugging 1')
            print(a)
            print('yes0')
            due_date = datetime.datetime.strptime(due_date_string, "%Y:%m:%d")
            print('Yes')
            time_difference = datetime.datetime.now() - due_date
            print(time_difference.days, 'this')
            name = a[0].split(':')
            eq_ = a[1].split(':')
            so_ = 0
            print(a)
            # return
            rental_date = a[3].split('=')
            if(int(time_difference.days)>0):
                # Per day $5 fine
                so_ = 5*int(time_difference.days)
                print(so_, 'Fine')
            lines = [
                f'Customer Name: {name[-1]}\n',
                f'Equipment: {eq_[-1]}\n',
                f'Rental date: {rental_date[-1]}\n',
                f'Due date: {due_date_string}\n',
                f'Fine= ${so_}\n'
            ]

            y__n = os.path.exists(f'{eq_name}bill.txt')
            if y__n:
                with open(f'{eq_name}bill.txt', 'a') as file:
                    file.writelines(lines)
                    file.close()
                    return


            with open(f'{eq_name}bill.txt', 'w') as file:
                file.writelines(lines)
                file.close()
        else:
            print('File not found try again')
            return_eqp()
    
    except Exception as e:
        print(e)

return_eqp()