_SOCCER_SIZE = 20
_FOOTING_SPEED = 8


class Soccer(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.soccer_size = _SOCCER_SIZE
        self.vitesse = 18
        self.acceleration = 6
        self.vitesse_actuelle = 0
        self.sens_actuel = 0
        self.inertie = 0
        self.is_accelerating = 0

    def newposition(self, sens, is_accelerating):
        self.is_accelerating = is_accelerating

        # si le footballeur accèlère
        if(self.is_accelerating == 1):
            # dans le même sens
            if(sens - self.sens_actuel == 0):
                self.inertie += 0.4
                self.vitesse_actuelle += self.inertie * self.acceleration
            # sur le côté
            elif(abs(sens - self.sens_actuel) == 1 or abs(sens - self.sens_actuel) == 3):
                self.inertie -= 0.4
                self.vitesse_actuelle += self.inertie * self.acceleration
            # dans le sens opposé
            elif(abs(sens - self.sens_actuel) == 2):
                self.inertie -= 0.8
                self.vitesse_actuelle += self.inertie * self.acceleration

        # si le footballeur décellère
        elif(self.is_accelerating == 0):
            self.inertie -= 0.6
            self.vitesse_actuelle = _FOOTING_SPEED

        # on ne peut changer de sens que lorsque l'inertie est à 0
        if(self.inertie <= 0):
            self.inertie = 0
            self.sens_actuel = sens
        # inertie maximum
        elif(self.inertie >= 3):
            self.inertie = 3

        # vitesses maximum et minimum non dépassables
        if(self.vitesse_actuelle >= self.vitesse):
            self.vitesse_actuelle = self.vitesse
        elif(self.vitesse_actuelle <= 0):
            self.vitesse_actuelle = 0

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
        print("ACCELERATION ?: "+str(self.is_accelerating))
