

class Ball(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.vitesse_actuelle = 0
        self.sens_actuel = 0
        self.is_moving = False
        self.angle

    def move(self, sens, vitesse):
        self.is_moving = True
        self.sens_actuel = sens
        self.vitesse_actuelle = vitesse
        if vitesse <= 0:
            self.vitesse_actuelle = vitesse
        # déplacement du footballeur
        if(self.sens_actuel == 2):
            self.posx += self.vitesse_actuelle
        if(self.sens_actuel == 4):
            self.posx -= self.vitesse_actuelle
        if(self.sens_actuel == 1):
            self.posy -= self.vitesse_actuelle
        if(self.sens_actuel == 3):
            self.posy += self.vitesse_actuelle
