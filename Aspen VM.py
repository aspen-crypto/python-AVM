import hashlib

def chainDataFind():
    pass








class VM(): #Where the magic happens
    def __init__(self, args, runData, blockChainData): #args is an array of: code, ip, sp, fp, data, datasize
                                                                                    #runData is [[this address, origin address, callerAddress], gas]
        self.ip = args[1]
        self.sp = args[2]
        self.fp = args[3]

        self.data = args[4]
        self.datasize = args[5]

        self.selfAddress = runData[0][0]
        self.originAddress = runData[0][1]
        self.callerAddress = runData[0][2]

        self.gas = runData[1]



        self.code = args[0].split(" ")

        self.stack = []
        self.memory = [None] * self.datasize

    def cpu(self):
        # Starting the list of all the operations =============

        def halt():

            return

        def pop():
            self.gas -= 1

            self.stack.pop()
            self.sp -= 1

        def iConst():
            self.gas -= 3

            self.ip += 1
            self.stack.append(self.code[self.ip])
            self.sp += 1

        def iAdd():
            self.gas -= 3

            summation = int(self.stack[-1]) + int(self.stack[-2])
            pop()
            pop()
            self.stack.append(summation)

        def iMult():
            self.gas -= 5

            product = int(self.stack[-1]) * int(self.stack[-2])
            pop()
            pop()
            self.stack.append(product)

        def iDiv():
            self.gas -= 5

            quotient = int(self.stack[-1]) / int(self.stack[-2])
            pop()
            pop()
            self.stack.append(quotient)

        def iSub():
            self.gas -= 3

            difference = int(self.stack[-1]) - int(self.stack[-2])  # subtract the lower item in the stack from the higher item!
            pop()
            pop()
            self.stack.append(difference)

        def cout():
            print(self.stack[-1])

        def iMod():
            self.gas -= 5

            mod = int(self.stack[-1]) % int(self.stack[-2])
            pop()
            pop()
            self.stack.append(mod)

        def branch():
            self.gas -= 8

            self.ip += 1
            addr = int(self.code[self.ip])
            self.ip = addr - 1

        def isLessThan():
            self.gas -= 3

            bul = self.stack[-1] < self.stack[-2]
            self.stack.append(bul)

        def isEqualTo():
            self.gas -= 3

            bul = self.stack[-1]==self.stack[-2]
            self.stack.append(bul)

        def isGreaterThan():
            self.gas -= 3

            bul = self.stack[-1] > self.stack[-2]
            self.stack.append(bul)

        def branchIfTrue():
            self.gas -= 10

            if self.stack[-1]:
                branch()
            else:
                self.ip += 1

        def branchIfFalse():
            self.gas -= 10

            if not self.stack[-1]:
                branch()
            else:
                self.ip += 1

        def gStore():
            self.ip += 1
            addr = int(self.code[self.ip])
            self.memory[addr] = self.stack[-1]

        def gLoad():
            self.gas -= 200

            self.ip += 1
            addr = int(self.code[self.ip])
            self.stack.append(self.memory[addr])

        def sha512():
            input = self.stack[-1]
            newHash = hashlib.sha512(input.encode(encoding = 'UTF-8')).digest()
            pop()
            self.stack.append(newHash)

        def Or():
            self.gas -= 3

            firstCondition = self.stack[-1]
            secondCondition = self.stack[-2]
            self.stack.append(firstCondition or secondCondition)

        def And():
            self.gas -= 3

            firstCondition = self.stack[-1]
            secondCondition = self.stack[-2]
            self.stack.append(firstCondition and secondCondition)

        def Not():
            self.gas -= 3

            self.stack.append(self.stack[-1]==False)

        def Xor():
            self.gas -= 3

            firstCondition = self.stack[-1]
            secondCondition = self.stack[-2]
            self.stack.append(firstCondition or secondCondition and not firstCondition and secondCondition)

        def selfAddress():
            self.stack.append(self.selfAddress)

        def originAddress():
            self.stack.append(self.originAddress)

        def callerAddress():
            self.stack.append(self.callerAddress)



        decoder = {
            "HALT": halt,

            "POP": pop,
            "ICONST": iConst,

            "IADD": iAdd,
            "ISUB": iSub,
            "IMULT": iMult,
            "IDIV": iDiv,
            "IMOD": iMod,

            "PRINT": cout,

            "IL": isLessThan,
            "IQ": isEqualTo,
            "IG": isGreaterThan,
            "OR": Or,
            "AND": And,
            "NOT": Not,
            "XOR": Xor,

            "BR": branch,
            "BRT": branchIfTrue,
            "BRF": branchIfFalse,

            "GSTORE": gStore,
            "GLOAD": gLoad,

            "SHA": sha512,

            "SADDR": selfAddress,
            "OADDR": originAddress,
            "CADDR": callerAddress
        }

        # Ending the operations list ====================

        def picker(codeName):
            decoder[codeName]()

        while self.ip < len(
                self.code) - 1:  # Ok, all that other stuff was just buildup, this is where the REAL magic happens
            self.ip += 1

            op = self.code[self.ip]
            print("OPCODE: " + str(op) + "\n IP: " + str(self.ip) + "\n STACK: " + str(self.stack) + "\n MEMORY: " + str(self.memory)+ "\n GAS: "+str(self.gas)+ "\n ---")
            picker(op)
            print("OPCODE: " + str(op) + "\n IP: " + str(self.ip) + "\n STACK: " + str(self.stack) + "\n MEMORY: " + str(self.memory) + "\n GAS: "+str(self.gas)+ "\n -------------------------")



aspenVM = VM(['ICONST 5 SHA PRINT POP HALT', -1, -1, 4, 12, 12, 10],  # Args = [code, IP, SP, FP, data, datasize]
                         [["SANTA CLARA", "SANTA BARBARA", "SANTA CRUZ"], 20],                        # RunData = [[SADDR, OADDR, CADDR], gas]
                         blockChainData = "dummyData")

aspenVM.cpu()