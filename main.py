import math

class AddTwoLinkedLists:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_length(self):
    # Check length of the two lists and equalize the length by adding zeros
        l1 = self.value1
        l2 = self.value2

        if len(l1) != len(l2):
            diff = len(l1) - len(l2)

            if diff > 0:
                l2.extend([0]*diff)
            
            else:
                l1.extend([0]*abs(diff))
        
        return l1, l2

    def calculate(self):
    # Calculate output as a linked list
        l1, l2 = self.check_length()

        output = []
        carry = 0

        for i in range(len(l1)):
            addition = int(l1[i]) + int(l2[i]) + carry
            div_by_10 = addition / 10
            remainder = addition % 10
            carry = math.trunc(div_by_10)

            if div_by_10 < 1:
                output.append(addition)
            else:
                output.append(remainder)

        if carry > 0:
            output.append(carry)

        print('Output as linked list: ', output)

        return output
