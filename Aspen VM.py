class VM(): #Where the magic happens
    def __init__(self, args): #args is an array of: code, ip, sp, fp, data, datasize
        self.ip = args[1]
        self.sp = args[2]
        self.fp = args[3]

        self.data = args[4]
        self.datasize = args[5]
        self.code = args[0]

        self.stack = []

    def cpu(self):
        # Starting the list of all the operations =============

        def halt():
            return

        def pop():
            self.stack.pop(self.sp)
            self.sp -= 1

        def iConst():
            self.ip += 1
            self.stack.append(self.code[self.ip])
            self.sp += 1

        def iAdd():
            sum = int(self.stack[-1]) + int(self.stack[-2])
            pop()
            pop()
            self.stack.append(sum)

        def iMult():
            product = int(self.stack[-1]) * int(self.stack[-2])
            pop()
            pop()
            self.stack.append(product)

        def iMult():
            product = int(self.stack[-1]) * int(self.stack[-2])
            pop()
            pop()
            self.stack.append(product)

        def iDiv():
            quotient = int(self.stack[-1]) / int(self.stack[-2])
            pop()
            pop()
            self.stack.append(quotient)

        def iSub():
            difference = int(self.stack[-1]) - int(self.stack[-2]) #subtract the lower item in the stack from the higher item!
            pop()
            pop()
            self.stack.append(difference)

        def cout():
            print(self.stack[-1])
            pop()

        decoder = {
            "HALT": halt,
            "POP": pop,
            "ICONST": iConst,
            "IADD": iAdd,
            "ISUB": iSub,
            "IMULT": iMult,
            "IDIV": iDiv,
            "PRINT": cout,
        }

        # Ending the operations list ====================

        def picker(codeName):
            decoder[codeName]()

        while self.ip < len(self.code) - 1: #Ok, all that other stuff was just buildup, this is where the REAL magic happens
            self.ip += 1


            op = self.code[self.ip]
            #print("OPCODE: " + str(op) + "\n IP: " + str(self.ip) + "\n STACK: " + str(self.stack))
            picker(self.code[self.ip])


aspenVM = VM([

              ["ICONST", "12", "ICONST", "60", "IDIV", "PRINT", "HALT"],


              -1, -1, 4, 12, 2]) #code, IP, SP, FP, data, datasize

aspenVM.cpu()













