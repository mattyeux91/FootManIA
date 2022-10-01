_SOCCER_SIZE = 20


class Soccer(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.soccer_size = _SOCCER_SIZE
        self.vitesse = 20
        self.acceleration = 20
        self.vitesse_actuelle = 0
        self.sens_actuel = 0
        self.inertie = 0

    def newposition(self, sens):
        # si rien ne se passe
        if(sens == 0):
            self.inertie -= 0.5
        if(sens - self.sens_actuel == 0):
            self.inertie += 0.3
        elif(abs(sens - self.sens_actuel) == 1):
            self.inertie -= 0.5
        elif(abs(sens - self.sens_actuel) == 2):
            self.inertie -= 0.8

        if(self.inertie <= 0):
            self.vitesse_actuelle = 0
            self.inertie = 0
            self.sens_actuel = sens
        elif(self.inertie >= 3):
            self.inertie = 3

        if(self.vitesse_actuelle < self.vitesse):
            self.vitesse_actuelle += self.inertie * self.acceleration

        if(self.sens_actuel == 2):
            self.posx += self.vitesse_actuelle
        if(self.sens_actuel == 4):
            self.posx -= self.vitesse_actuelle
        if(self.sens_actuel == 1):
            self.posy -= self.vitesse_actuelle
        if(self.sens_actuel == 3):
            self.posy += self.vitesse_actuelle
        print("VITESSE: "+str(self.vitesse_actuelle))
        print("SENS: "+str(self.sens_actuel))
        print("INERTIE: "+str(self.inertie))
