
# For minus
def update_equipment_data(filename, eq, q):
    try:
        # Read the lines from the file
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(lines)

        # Identify and modify the line you want to change
        for index, line in enumerate(lines):
            if eq in line:
                print(index, 'INDEX')
                v = line.split(',')
                print(v[3])
                aa = str(int(v[3]))
                # print('YES')
                bb = int(v[3]) - q 
                bb_ = str(bb)
                modified_line = line.replace(aa, bb_)
                lines[index] = modified_line
                print(modified_line)
                print(aa, 'ths')
        # Write the modified lines back to the file
        with open(filename, 'w') as file:
            file.writelines(lines)
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print("An error occurred:", e)






# For plus
def update_equipments_plus(filename, eq, q):
    try:
        print('Hello Hero', filename)
        print(eq, ' I am the eq')
    
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(lines)

        # Identify and modify the line you want to change
        print('Ia m lines', lines)
        for index, line in enumerate(lines):
            print(line, 'i am line')
            if eq.lower() in line.lower():
                print(index, 'INDEX')
                v = line.split(',')            
                kk =  v[-1].split(',')
                print('YES I AM KK', kk)
                print('I am v', v)                
                aa = str(kk[0])
                bb = int(v[-1].strip()) + q 
                bb_ = str(bb)
                modified_line = line.replace(aa, f'{bb_}\n')
                lines[index] = modified_line
                print(modified_line)
                print(aa, 'ths')
            else:
                pass
        # Write the modified lines back to the file
        with open(filename, 'w') as file:
            file.writelines(lines)
        
    except Exception as e:
        print(e)
# update_equipment_data('equipment_data.txt', 'Microphone Set', 3)