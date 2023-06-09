""""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import random

import arcade
import game_state
#import arcade.gui

from attack_animation import AttackType, AttackAnimation
from game_state import GameState

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45  # The default line height for text.


class MyGame(arcade.Window):
   """
   La classe principale de l'application

   NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
   Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
   """

   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT / 2.5
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK_OLIVE)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None

       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = None
       self.computer_attack_type = None
       self.player_sprite_chosen = True
       self.player_won_round = None
       self.draw_round = None

       self.game_state = game_state.GameState.NOT_STARTED

   def setup(self):
       """
       Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
       fois si vous recommencer une nouvelle partie.
       """
       # C'est ici que vous allez créer vos listes de sprites et vos sprites.
       # Prenez note que vous devriez attribuer une valeur à tous les attributs créés dans __init__
       #self.game_state = GameState.NOT_STARTED
       #self.computer_score = 0
       #self.player_score = 0
       self.player = arcade.Sprite(Assets/faceBeard.png)
       self.computer = arcade.Sprite(Assets/compy.png)

       self.players = arcade.SpriteList()
       self.players.append(self.player)
       self.players.append(self.computer)
       self.rock = AttackAnimation(AttackType.ROCK)
       self.paper = AttackAnimation(AttackType.PAPER)
       self.scissors = AttackAnimation(AttackType.SCISSORS)

       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = None
       self.computer_attack_type = None
       self.player_sprite_chosen = True
       self.player_won_round = None
       self.draw_round = None

       self.game_state = game_state.GameState.ROUND_ACTIVE

   def validate_victory(self):
       """
       Utilisé pour déterminer qui obtient la victoire (ou s'il y a égalité)
       Rappel: après avoir validé la victoire, il faut changer l'état de jeu
       """


   def draw_possible_attack(self):
       """
       Méthode utilisée pour dessiner toutes les possibilités d'attaque du joueur
       (si aucune attaque n'a été sélectionnée, il faut dessiner les trois possibilités)
       (si une attaque a été sélectionnée, il faut dessiner cette attaque)
       """
       pass

   def draw_computer_attack(self):
       """
       Méthode utilisée pour dessiner les possibilités d'attaque de l'ordinateur
       """
       pass


   def draw_scores(self):
       """
       Montrer les scores du joueur et de l'ordinateur
       """
       pass

   def draw_instructions(self):
       """
       Dépendemment de l'état de jeu, afficher les instructions d'utilisation au joueur (appuyer sur espace, ou sur une image)
       """
       pass

   def on_draw(self):
       """
       C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
       de votre jeu à l'écran.
       """

       # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
       # plan selon la couleur spécifié avec la méthode "set_background_color".
       arcade.start_render()

       # Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.BLACK_BEAN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.draw_instructions()
       self.players.draw()
       self.draw_possible_attack()
       self.draw_scores()

       #afficher l'attaque de l'ordinateur selon l'état de jeu
       #afficher le résultat de la partie si l'ordinateur a joué (ROUND_DONE)
       pass

   def on_update(self, delta_time):
       """
       Toute la logique pour déplacer les objets de votre jeu et de
       simuler sa logique vont ici. Normalement, c'est ici que
       vous allez invoquer la méthode "update()" sur vos listes de sprites.
       Paramètre:
           - delta_time : le nombre de milliseconde depuis le dernier update.
       """
       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques
       #si le joueur a choisi une attaque, générer une attaque de l'ordinateur et valider la victoire
       #changer l'état de jeu si nécessaire (GAME_OVER)

       self.rock.on_update()
       self.paper.on_update()
       self.scissors.on_update()

       self.computer_rock.on_update()
       self.computer_paper.on_update()
       self.computer_scissors.on_update()

       pc_attack = randint(0, 2)
       if pc_attack == 0:
           self.player_attack_type == AttackType.ROCK
           if self.computer_attack_type == AttackType.ROCK:
               pass
           if self.computer_attack_type == AttackType.PAPER:
               self.computer_score += 1
           if self.computer_attack_type == AttackType.SCISSORS:
               self.player_score += 1

       if pc_attack == 1:
           self.player_attack_type == AttackType.PAPER
           if self.computer_attack_type == AttackType.PAPER:
               pass
           if self.computer_attack_type == AttackType.SCISSORS:
               self.computer_score += 1
           if self.computer_attack_type == AttackType.ROCK:
               self.player_score += 1

       if pc_attack == 2:
           self.player_attack_type == AttackType.SCISSORS
           if self.computer_attack_type == AttackType.SCISSORS:
               pass
           if self.computer_attack_type == AttackType.ROCK:
               self.computer_score += 1
           if self.computer_attack_type == AttackType.PAPER:
               self.player_score += 1

   def on_key_press(self, key, key_modifiers):
       """
       Cette méthode est invoquée à chaque fois que l'usager tape une touche
       sur le clavier.
       Paramètres:
           - key: la touche enfoncée
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?

       Pour connaître la liste des touches possibles:
       http://arcade.academy/arcade.key.html
       """
       if (self.game_state == game_state.GameState.NOT_STARTED and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE
       if (self.game_state == game_state.GameState.ROUND_DONE and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE
           game_state.GameState.ROUND_DONE = False
       if (self.game_state == game_state.GameState.GAME_OVER and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE
           game_state.GameState.GAME_OVER = False
           self.player_score = 0

       """N'oubliez pas de remettre à faux ou 0 toute variable qui sert à la validation"""

   def reset_round(self):
       """
       Réinitialiser les variables qui ont été modifiées
       """
       #self.computer_attack_type = -1
       #self.player_attack_chosen = False
       #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       #self.player_won_round = False
       #self.draw_round = False

       pass

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Méthode invoquée lorsque l'usager clique un bouton de la souris.
       Paramètres:
           - x, y: coordonnées où le bouton a été cliqué
           - button: le bouton de la souris appuyé
           - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
       """

       # Test de collision pour le type d'attaque (self.player_attack_type).
       # Rappel que si le joueur choisi une attaque, self.player_attack_chosen = True
       if self.rock.collides_with_point((x, y)):
           self.player_attack_type = AttackType.ROCK
           self.computer_attack_type = True
           self.game_state = GameState.VALIDATE_VICTORY

       if self.paper.collides_with_point((x, y)):
           self.player_attack_type = AttackType.PAPER
           self.computer_attack_type = True
           self.game_state = GameState.VALIDATE_VICTORY

       if self.scissors.collides_with_point((x, y)):
           self.player_attack_type = AttackType.SCISSORS
           self.computer_attack_type = True
           self.game_state = GameState.VALIDATE_VICTORY

def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()

if __name__ == "__main__":
   main()