class PrimeGenerator:
    def __init__(self,stop):
        self.stop=stop
        self.lowerbound=2
        self.prime=0

    def __next__(self):
        #if self.lowerbound<self.stop:
            for n in range(self.lowerbound, self.stop):
                for x in range(2, n):
                    if n % x == 0:
                        break
                else:
                    self.prime=n
                    self.lowerbound = n+1
                    return n

            raise StopIteration()

    def __iter__(self):
        return self

# class PrimeIterator:
#
#     def __init__(self,bound):
#         self.bound=bound
#
#     def __iter__(self):
#         return PrimeGenerator(self.bound)



print(list(PrimeGenerator(100)))
#

my_gen=PrimeGenerator(5)
#
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
#


# print(list(next(my_gen)))
# next(my_gen)
# print(my_gen.prime)
# next(my_gen)
# print(my_gen.prime)
# # next(my_gen)
# # print(my_gen.prime)
# # next(my_gen)
# # print(my_gen.prime)
# # next(my_gen)
# # print(my_gen.prime)
# # next(my_gen)
# # print(my_gen.prime)
# # next(my_gen)
# # next(my_gen)
# #
# #
# a=list(next(my_gen))
# print(a)



