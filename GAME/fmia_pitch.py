import pygame
import random as rdn
from fmia_soccer import Soccer
from fmia_ball import Ball
# import math

_PITCH_WIDTH = 1200
_PITCH_HEIGHT = 800
_TOUCH_WIDTH = 50
_CENTRAL_CIRCLE_RADIUS = 91.5
_LINE_THICKNESS = 3
_SURFACE_WITDH = 165
_SURFACE_HEIGHT = 403
_GOAL_SURFACE_WIDTH = 55
_GOAL_SURFACE_HEIGHT = _SURFACE_HEIGHT-2*110
_PENALT_DISTANCE = 110
_PENALT_SIZE = 5
_CENTRAL_SIZE = 5
_GOAL_WIDTH = 15
_GOAL_HEIGHT = 73.2
_BALL_SIZE = 5


class Pitch(object):

    def __init__(self):
        self.clock_update = pygame.time.Clock()  # clock to manage time update and FPS
        self.pitch_frame = pygame.Surface((_PITCH_WIDTH, _PITCH_HEIGHT))  # main surface
        self.pitch_frame.fill((126, 200, 80))
        self.soccer = Soccer(rdn.randint(_TOUCH_WIDTH, _PITCH_WIDTH), rdn.randint(_TOUCH_WIDTH, _PITCH_HEIGHT))
        self.ball = Ball(_PITCH_WIDTH/2, _PITCH_HEIGHT/2)
        self.rect_soccer = pygame.draw.circle(self.pitch_frame, (255, 0, 0), (self.soccer.posx, self.soccer.posy), self.soccer.soccer_size/2, width=0)
        self.rect_ball = pygame.draw.circle(self.pitch_frame, (0, 0, 0), (_PITCH_WIDTH/2, _PITCH_HEIGHT/2), _BALL_SIZE, width=0)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# renndering
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def render_pitch(self):
        # self.ball.move(self.ball.sens_actuel, self.ball.vitesse_actuelle/1.5-1)
        self.collision_ball()
        self.pitch_frame.fill((126, 200, 80))
        # dessine les lignes du terrain
        pygame.draw.rect(self.pitch_frame, (255, 255, 255), (_TOUCH_WIDTH, _TOUCH_WIDTH, _PITCH_WIDTH-2*_TOUCH_WIDTH, _PITCH_HEIGHT-2*_TOUCH_WIDTH), _LINE_THICKNESS)
        # dessine la line médiane
        pygame.draw.line(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH/2, _TOUCH_WIDTH), (_PITCH_WIDTH/2, _PITCH_HEIGHT-_TOUCH_WIDTH), _LINE_THICKNESS)
        # dessine le rond central
        pygame.draw.circle(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH/2-1, _PITCH_HEIGHT/2-1), _CENTRAL_CIRCLE_RADIUS, width=_LINE_THICKNESS)
        # dessine les surfaces de réparation
        pygame.draw.rect(self.pitch_frame, (255, 255, 255), (_TOUCH_WIDTH, (_PITCH_HEIGHT-_SURFACE_HEIGHT)/2, _TOUCH_WIDTH+_SURFACE_WITDH, _SURFACE_HEIGHT), _LINE_THICKNESS)
        pygame.draw.rect(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH-_TOUCH_WIDTH*2-_SURFACE_WITDH, (_PITCH_HEIGHT-_SURFACE_HEIGHT)/2, _TOUCH_WIDTH+_SURFACE_WITDH, _SURFACE_HEIGHT), _LINE_THICKNESS)
        # dessine les surfaces du goal
        pygame.draw.rect(self.pitch_frame, (255, 255, 255), (_TOUCH_WIDTH, (_PITCH_HEIGHT-_GOAL_SURFACE_HEIGHT)/2, _GOAL_SURFACE_WIDTH, _GOAL_SURFACE_HEIGHT), _LINE_THICKNESS)
        pygame.draw.rect(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH-_TOUCH_WIDTH-_GOAL_SURFACE_WIDTH, (_PITCH_HEIGHT-_GOAL_SURFACE_HEIGHT)/2, _GOAL_SURFACE_WIDTH, _GOAL_SURFACE_HEIGHT), _LINE_THICKNESS)
        # dessine le point de pénalty
        pygame.draw.circle(self.pitch_frame, (255, 255, 255), (_TOUCH_WIDTH+_PENALT_DISTANCE, _PITCH_HEIGHT/2-1), _PENALT_SIZE, width=0)
        pygame.draw.circle(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH-_TOUCH_WIDTH-_PENALT_DISTANCE, _PITCH_HEIGHT/2-1), _PENALT_SIZE, width=0)
        # dessine le point central
        pygame.draw.circle(self.pitch_frame, (255, 255, 255), (_PITCH_WIDTH/2, _PITCH_HEIGHT/2), _CENTRAL_SIZE, width=0)
        # dessine les cages
        pygame.draw.rect(self.pitch_frame, (158, 158, 158), (_TOUCH_WIDTH-_GOAL_WIDTH+2, (_PITCH_HEIGHT-_GOAL_HEIGHT)/2, _GOAL_WIDTH, _GOAL_HEIGHT), 0)
        pygame.draw.rect(self.pitch_frame, (158, 158, 158), (_PITCH_WIDTH-_TOUCH_WIDTH-2, (_PITCH_HEIGHT-_GOAL_HEIGHT)/2, _GOAL_WIDTH, _GOAL_HEIGHT), 0)
        # self.ball.move(self.ball.direction, self.ball.vitesse_actuelle)

    def render_footballeur(self):
        self.rect_soccer = pygame.draw.circle(self.pitch_frame, (255, 0, 0), (self.soccer.posx, self.soccer.posy), self.soccer.soccer_size/2, width=0)

    def render_ball(self):
        self.rect_ball = pygame.draw.circle(self.pitch_frame, (0, 0, 0), (self.ball.posx, self.ball.posy), _BALL_SIZE, width=0)

    def render(self):
        self.render_pitch()
        self.render_footballeur()
        self.render_ball()

    def collision_ball(self):
        # ax = self.rect_soccer.centerx
        # ay = self.rect_soccer.centery
        # bx = self.rect_ball.centerx
        # by = self.rect_ball.centery
        # cx = bx
        # cy = ay
        # ac = cx - ax
        # bc = by - cy
        # # ab = math.sqrt(math.pow(ac, 2) + math.pow(bc, 2))
        # # print("ax " + str(ax))
        # # print("ay " + str(ay))
        # # print("bx " + str(bx))
        # # print("by " + str(by))
        # # print("cx " + str(cx))
        # # print("cy " + str(cy))
        # # print("AC " + str(ac))
        # # print("BC " + str(bc))
        # # print("AB " + str(ab))
        # direction = (ac, bc)
        if self.rect_soccer.colliderect(self.rect_ball):
            self.soccer.pushball(self.ball, "CONDUITE")
