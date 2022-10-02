

class Ball(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.vitesse_actuelle = 0
        self.direction = (0, 0)
        self.is_moving = False

    def move(self, direction, vitesse):
        self.is_moving = True
        self.direction = direction
        self.vitesse_actuelle = vitesse
        if vitesse <= 0:
            self.vitesse_actuelle = vitesse
        # déplacement de la balle
        d_x = self.direction[0]
        d_y = self.direction[1]
        deplacement = 0
        deplacement = self.vitesse_actuelle / 3
        for i in range(abs(int(d_x))):
            if d_x > 0:
                self.posx += deplacement
            elif d_x < 0:
                self.posx -= deplacement
        for j in range(abs(int(d_y))):
            if d_y > 0:
                self.posy += deplacement
            elif d_y < 0:
                self.posy -= deplacement
        print("---BALLE MOVE---")
        print("Vitesse " + str(self.vitesse_actuelle))
        print("Direction " + str(self.direction))
        # if(self.sens_actuel == 2):
        #     self.posx += self.vitesse_actuelle
        # if(self.sens_actuel == 4):
        #     self.posx -= self.vitesse_actuelle
        # if(self.sens_actuel == 1):
        #     self.posy -= self.vitesse_actuelle
        # if(self.sens_actuel == 3):
        #     self.posy += self.vitesse_actuelle
