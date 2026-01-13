s_list = []

def exist(id: str) -> int:       #Check if id is in list

    for i in range(len(s_list)):
        if s_list[i]["id"] == id:
            return i + 1
    
    return 0

def main():

    print("CLASSROOM DATA MANAGER")
    print("Type '1': Add a new student")
    print("Type '2': Search by student ID")
    print("Type '3': Display all scores")
    print("Type anything else to exit.")

    choice = input().strip()       #Read user's choice
    
    if choice == "1":       #1. Add a new student
        
        id = input("ID? ").strip()       #Read ID
        while len(id) == 0 or exist(id):
            print("Try again! (ID must not be empty/ ID already exists)")
            id = input("ID? ").strip()
        
        name = input("Name? ").strip()       #Read name
        while len(name) == 0:
            print("Try again! (Name must not be empty)")
            name = input("Name? ").strip()
        
        score = input("Score? ").strip()       #Read score
        while len(score) == 0:
            print("Try again! (Score must not be empty)")
            score = input("Score? ").strip()
        
        s_list.append({       #Add student
            "id": id,
            "name": name,
            "score": score
        })
        print("Student recorded!")

    elif choice == "2":       #2. Search student by ID
        
        id = input("ID? ").strip()       #Read ID
        while len(id) == 0 or not exist(id):
            print("Try again! (ID must not be empty/ ID does not exist)")
            id = input("ID? ").strip()
        
        s = s_list[exist(id) - 1]
        print(f"ID: {s["id"]} | Name: {s["name"]} | Score: {s["score"]}")       #Print all students

    elif choice == "3":       #3. Display all scores
    
        if len(s_list) == 0:
            
            print("No students found.")

        else:
            
            l_no, l_id, l_name, l_score = max(3, len(str(len(s_list)))), 2, 4, 5
            for s in s_list:
                l_id = max(l_id, len(s["id"]))
                l_name = max(l_name, len(s["name"]))
                l_score = max(l_score, len(s["score"]))
            print("No." + (l_no - 3) * ' ' + " | ID" + (l_id - 2) * ' ' + " | Name" + (l_name - 4) * ' ' + " | Score")
            print((l_no + l_id + l_name + l_score + 9) * '=')

            for i in range(len(s_list)):       #Print all scores
                s = s_list[i]
                i_no = len(str(i + 1))
                i_id = len(s["id"])
                i_name = len(s["name"])
                print(str(i + 1) + (l_no - i_no) * ' ' + " | " + s["id"] + (l_id - i_id) * ' ' + " | " + s["name"] + (l_name - i_name) * ' ' + " | " + s["score"])

    else:

        return       #Exit

    if input("Continue? (Type 'y' to proceed) ").strip().lower() == 'y':       #Ask to continue

        main()

main()