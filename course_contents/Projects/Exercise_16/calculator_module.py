from add_module import Addition

class Calculator:
    @classmethod
    def add(cls,num1,num2):
        return Addition.add(num1,num2)

    @classmethod
    def substract(cls,num1,num2):
        return Addition.add(num1,-num2)

    @classmethod
    def multiply(cls,num1,num2):
        result=0
        for i in range(num2):
            i+=1
            result+=Addition.add(num1,0)
        return result

    @classmethod
    def divide(cls, num1, num2):
        result = 0
        i=-1
        while result<=num1:
            result+=Addition.add(num2,0)
            i+=1

        return i



result=Calculator.divide(9,5)
print(result)


