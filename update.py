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

# update_equipment_data('equipment_data.txt', 'Microphone Set', 3)