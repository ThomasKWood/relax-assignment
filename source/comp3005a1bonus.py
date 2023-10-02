# global
db = {}
tables = 0


def printRelation(pInput):
    found = False
    for i in range(0, tables):
        if db[i][0] == pInput:
            found = True
            # print headers
            pString = "|"
            for y in range(0, db[i][2]):
                pString = pString + db[i][1][y][0]
                pString = pString + "|"
            print(pString)

            # print rows
            pString = "|"
            for row in range(1, db[i][3] + 1):
                for rIndex in range(0, db[i][2]):
                    pString = pString + str(db[i][1][rIndex][1][row])
                    pString = pString + "|"
                print(pString)
                pString = "|"
                
        if not found:
            print("Table not found.")

def addRelaiton():
    global tables
    global db
    columnList = {}
    # create data here
    name = input("Enter table name ")
    headers = input("Enter headers: h1,h2,h3... ")
    if "," in headers:
        headerList = headers.split(',')
    else:
        headerList = [headers]
            
    x = 0
    for hName in headerList:
        columnList[x] = [hName, [None]]
        x += 1

    valuesAmt = int(input("How many values do you plan to enter? "))
            
    for i in range(0, valuesAmt):
        vInput = input("Please enter your " + str(i+1) + " set of data: t1,t2,t3... ")
        if "," in vInput:
            values = vInput.split(',')
            for y in range(0, len(headerList)):
                if values[y] != "":
                    columnList[y][1].append(values[y])
                else:
                    columnList[y][1].append(None)
        else:
            if vInput != "":
                columnList[0][1].append(vInput)
            else:
                columnList[0][1].append(None)
            
    db[tables] = [name, columnList, len(headerList), valuesAmt]
    tables += 1


def processQuery():
    query = input("Accepted queuries:\nselect(relation, condition)\nproject(relation, attributes)\njoin(relation1, relation2, condition)\nunion(relation1, relation2)\nunion_all(relation1, relation2)\nintersect(relation1, relation2)\nminus(relation1, relation2)\nEnter your query: ")
# Remove any whitespace from the query
    query = query.replace(" ", "")
    
    # Check if the query starts with a valid operation
    if query.startswith("selection("):
        # Extract the operation, relation name, and condition
        operation, rest = query.split("(", 1)
        relation_name, condition = rest.split(",", 1)
        condition = condition.rstrip(")")
        return selection(relation_name, condition)
    
    elif query.startswith("project("):
        # Extract the operation, relation name, and attributes
        operation, rest = query.split("(", 1)
        relation_name, attributes = rest.split(",", 1)
        attributes = attributes.rstrip(")")
        return project(relation_name, attributes)
    
    elif query.startswith("join("):
        # Extract the operation, relation names, and condition
        operation, rest = query.split("(", 1)
        relation_names, condition = rest.split(",", 1)
        relation1, relation2 = relation_names.split("->", 1)
        condition = condition.rstrip(")")
        return join(relation1, relation2, condition)
    
    elif query.startswith("union_all("):
        # Extract the operation, relation names
        operation, rest = query.split("(", 1)
        relation_names = rest.rstrip(")")
        relation1, relation2 = relation_names.split(",", 1)
        return union_all(relation1, relation2)
    
    elif query.startswith("union("):
        # Extract the operation, relation names
        operation, rest = query.split("(", 1)
        relation_names = rest.rstrip(")")
        relation1, relation2 = relation_names.split(",", 1)
        return union(relation1, relation2)
    
    elif query.startswith("intersect("):
        # Extract the operation, relation names
        operation, rest = query.split("(", 1)
        relation_names = rest.rstrip(")")
        relation1, relation2 = relation_names.split(",", 1)
        return intersect(relation1, relation2)
    
    elif query.startswith("minus("):
        # Extract the operation, relation names
        operation, rest = query.split("(", 1)
        relation_names = rest.rstrip(")")
        relation1, relation2 = relation_names.split(",", 1)
        return minus(relation1, relation2)
    
    else:
        return "Invalid query format"


# Queries
# selection, projection, join, union, union all, intersect, minus
def selection(relation_name, condition):
    pass

def project(relation_name, attributes):
    pass

def join(relation1, relation2, condition):
    pass

def union_all(relation1, relation2):
    pass

def union(relation1, relation2):
    pass

def intersect(relation1, relation2):
    





def main():
    # menu
    loop = True
    while loop:
        # get choice

        cinput = input("Select Choice: 1 Add Relation, 2 Query Relation, 3 Print Relation, 4 Quit ")
        if cinput == "1":
            addRelaiton()

        elif cinput == "2":
            # query here
            continue
        
        elif cinput == "3":
            uInput = input("Name the relation you want to print: ")
            printRelation(uInput)

        elif cinput == "4":
            loop = False
            exit(0)

        else:
            print("Option not recognized")

if __name__ == "__main__":
    main()