import datetime
import os
def return_eqp():
    try:
        with open('datas.txt', 'r+') as file:
            a = file.readlines()
            b = a[1].split(':')
          
            c = a[3].split('=')
            due_date_string = c[1].strip() #remove the whitspace
            print(due_date_string)
            due_date = datetime.datetime.strptime(due_date_string, "%Y:%m:%d")
            time_difference = datetime.datetime.now() - due_date
            # print('Hello')
            print(time_difference.days, 'this')

            name = a[0].split(':')
            eq_ = a[1].split(':')
            so_ = 0
            rental_date = a[2].split('=')
            if(int(time_difference.days)>0):
                # Per day $5 fine
                so_ = 5*int(time_difference.days)
                print(so_, 'Fine')


                

            

            lines = [
                f'Customer Name: {name}\n',
                f'Equipment: {eq_}\n',
                f'Rental date: {rental_date}\n',
                f'Due date: {due_date_string}\n',
                f'Fine= ${so_}'

            ]

            with open('fine.txt', 'w') as file:
                file.writelines(lines)
                file.close()

            a = os.path.exists('equipment_data.txt')
            if a:
                os.remove('equipment_data.txt')
            else:
                return


            
            
    except Exception as e:
        print(e)

return_eqp()