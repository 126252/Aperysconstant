#_=%
import numpy as np
import time

class main:
    def __init__(self):
        self.size = int(input("size: ")) * 3
        self.random = np.random.randint(1, 100000, self.size).reshape((int(self.size/3), 3))
        self.random.astype(float)

        number_of_coprimes = self.coprimes(self.random)

        total = self.random.shape[0]

        Apérys_constant = 1.2020569031595942854
        Apérys_constant_ish = total / number_of_coprimes

        print("Apérys constant: ", Apérys_constant)
        print("Apérys constant ish: ", Apérys_constant_ish)

   

    def coprimes(self, array):
        # 2d array
        number_of_coprimes = 0
        i = 0
        
        while array.shape[0] > i:
            if self.numpy_gcd(array[i,:]) == 1:
                number_of_coprimes += 1
                
            print("curently at: {}".format(i))
            i += 1

        return number_of_coprimes
        

    def numpy_gcd(self, array):
        # one dimensional array only
        mod = np.array([])
        i = np.max(array)
        
        while i >= 1:
            mod = array % i
            if np.sum(mod) == 0:
                return i

            i -= 1
            
if __name__ == "__main__":
    start = time.process_time()
    main()
    end = time.process_time()
    print("processing time: {}s".format(end-start))
