CurrentOperation = 0
Clipboard = [""]
def BastShoe(command):
    command = [command[0], command[2:]]
    if int(command[0]) == 1:
        command = Add(command[1])
    elif int(command[0]) == 2:
        command = Delete(int(command[1]))
    elif int(command[0]) == 3:
        command = Give(int(command[1]))
    elif int(command[0]) == 4:
        command = Undo()
    elif int(command[0]) == 5:
        command = Redo()
    else:
        command = ""
    return command
def Add(S):
    global CurrentOperation
    global Clipboard
    if CurrentOperation != len(Clipboard) - 1:
        Clipboard = [Clipboard[CurrentOperation], Clipboard[CurrentOperation] + S]
        CurrentOperation = 1
    else:
        Clipboard.append(Clipboard[CurrentOperation] + S)
        CurrentOperation += 1
    return Clipboard[CurrentOperation]
def Delete(N):
    global CurrentOperation
    global Clipboard
    if N >= len(Clipboard[CurrentOperation]):
        temp = ""
    else:
        temp = Clipboard[CurrentOperation][:len(Clipboard[CurrentOperation]) - N] # я не уверен что это сработает
    if CurrentOperation != len(Clipboard) - 1:
        Clipboard = [Clipboard[CurrentOperation], temp]
        CurrentOperation = 1
    else:
        Clipboard.append(temp)
        CurrentOperation += 1
    return Clipboard[CurrentOperation]
def Give(i):
    global CurrentOperation
    global Clipboard
    if i >= len(Clipboard[CurrentOperation]):
        return ""
    else:
        return Clipboard[CurrentOperation][i]
def Undo():
    global CurrentOperation
    global Clipboard
    if CurrentOperation > 0:
        CurrentOperation -= 1
    return Clipboard[CurrentOperation]
def Redo():
    global CurrentOperation
    global Clipboard
    if CurrentOperation < len(Clipboard) - 1:
        CurrentOperation += 1
    return Clipboard[CurrentOperation]
