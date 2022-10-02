import fmia_settings as settings

_SOCCER_SIZE = 20
_FOOTING_SPEED = 8


class Soccer(object):

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.soccer_size = _SOCCER_SIZE
        self.vitesse = 18
        self.vitesse_actuelle = 0
        self.sens_actuel = 0
        self.is_accelerating = False
        self.get_balle = False
        self.attributes = {}

    def move(self, sens, is_accelerating):
        self.sens_actuel = sens
        self.is_accelerating = is_accelerating

        # si le footballeur accèlère
        if(self.is_accelerating):
            self.vitesse_actuelle = self.vitesse/settings.GENERAL_SETTINGS["SMOOTHLESSMODE"]

        # si le footballeur décellère
        elif(not self.is_accelerating):
            self.vitesse_actuelle = _FOOTING_SPEED/settings.GENERAL_SETTINGS["SMOOTHLESSMODE"]

        # déplacement du footballeur
        if(self.sens_actuel == 2):
            self.posx += self.vitesse_actuelle
        if(self.sens_actuel == 4):
            self.posx -= self.vitesse_actuelle
        if(self.sens_actuel == 1):
            self.posy -= self.vitesse_actuelle
        if(self.sens_actuel == 3):
            self.posy += self.vitesse_actuelle

        # trace
        # print("VITESSE: "+str(self.vitesse_actuelle))
        # print("SENS: "+str(self.sens_actuel))
        # print("INERTIE: "+str(self.inertie))
        # print("ACCELERATION ?: "+str(self.is_accelerating))

    def pushball(self, balle):
        self.get_ball = True
        balle.move(self.sens_actuel, self.vitesse_actuelle)
