class Qbit:
    def __self__(self):
        alpha = complex(0.0,0.0)
        betha = complex(0.0,0.0)

    def __self__(self,alpha,betha):
        alpha = alpha
        betha = betha

        self.validateQubit()


    def validateQubit(self):
        result = self.alpha ** 2 + self.betha ** 2

        if result == 1:
            return True
        else:
            return False

        