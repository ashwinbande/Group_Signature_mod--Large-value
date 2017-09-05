class Open_Manager:

    X = 351007651139877993
    def Get_Y(self, G, N):
        Y = pow(G, self.X, N)
        return Y