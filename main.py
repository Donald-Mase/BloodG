START = "\n Enter '1' to register Blood type in the program, \n '2' To see the people in the Scheme,\n '3' to find a donor by blood group,\n '4' To find a donor by Area,\n 'q' to exit the session"
Bloodgroups = []
#GroupPs = ['A+','A-','B+','B-','AB+','AB-','O-','O+']
def add_group():
    fName = input("Enter you First Name:")
    lName = input("Enter your Last Name:")
    Group = input("Enter your blood type and Rhesus Factor:")
    Registration = input("Enter your Registration Number:")
    Contact = input("Enter your Phone Number:")
    Area = input("Enter the area you are based:")
    Bloodgroups.append({
        'Name':fName+' '+lName,
        'Registration': Registration,
        'Group': Group.upper(),
        'Camp': Area,
        'Contact': Contact,
    })
def list_donors():
    Total_Donors = len(Bloodgroups)
    Groups = [Bloodgroups['Group'] for Group in Bloodgroups]
    Groups = ','.join(Groups)
    if Total_Donors:
        print(f'The following bloodgroups are available to make blood donation:{Group}')
    else:print(f'There are no donors.')
def print_blood_group_info(Bloodgroups):
    print(f'Here is info about the blood group you are seeking')
    #print(f'Name:{Bloodgroup["Name"]})
    #print(f'Registration:{Bloodgroup["Group"]})
    #print(f'Registration:{Bloodgroup["Registration"]})
    #print(f'Contact{Bloodgroup['Contact']})
    #print(f'Area:{Bloodgroup["Area"]}),

def my_donors():
    group_title = input ('Enter Bloodgroup you are looking for:')
    area_title = input('Enter Area you are seeking:')
    for Group in Groups:
        if Bloodgroups['Group'] == group_title and Bloodgroups['Camp']== area_title:
            print("Donor found nearby")
            print_blood_group_info(Group)
        elif Bloodgroups['Group'] == group_title and Bloodgroups['Camp']!= area_title:
            print(f'Donor available')
            print_blood_group_info(Group)
        else: print('You do not have a donor')
def my_type():
    compatible = input('Enter blood group to match a donor:')
    for Group in Groups:
        if compatible == 'A-':
            pass
           #print(f'{print_blood_group_info()}') for [ A-, O-] in [Bloodgroups['Group']
        elif compatible == 'A+':
            pass
           #print(f'{print_blood_group_info()}') for [A+, A-, O+, O-] in [Bloodgroups['Group']
        elif compatible == 'B+':
            pass
           #print(f'{print_blood_group_info()}') for [B+, B-, O+, O-] in [Bloodgroups['Group']
        elif compatible == 'B-':
            pass
           #print(f'{print_blood_group_info()}') for [B-, O-] in [Bloodgroups['Group']
        elif compatible == 'AB+':
            pass
           #print(f'{print_blood_group_info()}') for [Bloodgroups['Group']
        elif compatible == 'AB-':
            pass
           #print(f'{print_blood_group_info()}') for [AB-, A-, B-, O-] in [Bloodgroups['Group']
        elif compatible == 'O+':
            pass
           #print(f'{print_blood_group_info()}') for [O+, O-] in [Bloodgroups['Group']
        elif compatible == 'O-':
            pass
           #print(f'{print_blood_group_info()}') for [O-] in [Bloodgroups['Group']


user_selection = {
    '1': add_group(),
    '2': list_donors(),
    '3': print_blood_group_info(),
    '4': my_donors(),
}

def menu():
    selection = input(START).lower()
    while selection!= 'q':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Choose from option 1,2,3,4")
        selection = input(START)
    print('Done')