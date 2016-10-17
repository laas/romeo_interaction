#!/usr/bin/env python
# -*- coding: utf-8 -*-

from romeo_srv.srv import *
import rospy
import naoqi
from naoqi import *

broker = ALBroker("pythonBroker","",0,"127.0.0.1",9559)
import sys
sys.path.append('/home/nao/.local/lib/python2.7/site-packages')
import time

try: import abcdk.bodytalk
except: pass # this error could occurs only on first execution, it's handled in the installer
try: import abcdk.naoqitools
except: pass
try: import abcdk.speech
except: pass

from abcdk_bodytalk import abcdk_class

def speech_for_phase(req):
    print "speech"
    tts = ALProxy("ALTextToSpeech", "romeo03", 9559)
    language = 0 #0 for French, 1 for English
    if language==1:
        tts.setLanguage("English") 
 
        try:
            if req.phase==0: #presentation
              tts.say("""Hello, my name is romeo. I'm an aldebaran-robotics' research platform.
    Welcome in the Bauzil room at Laas-CNRS.
    Today I will present the mid-term step of KOROIBOT project.\\PAU=500\\
    Gepetto team is involved in this project with the robot HRP2.
    Among the possibilities of tasks proposed in Koroibot,
    Gepetto choose five of them : stepping stones, going up and down stairs and
    walking on the beam""")
                
            if req.phase==1:#going upstairs
              tts.say("""This is the first sequence of HRP2.
    He is climbing 10 centimeters high steps.
    The passage is narrow and the robot risks to strike the beam with his left hand
    and the barrier with his right hand """)      
            if req.phase==2:#walking on the beam
              tts.say("""HRP2 is now walking on the beam.
    Since the motion caption is not activated to correct the trajectory,
    the initial position of the robot on the beam is very important""")
            if req.phase==3:#Mujoko
              tts.say("""This is now the Mujoko demonstration""")
            if req.phase==4:#going downstairs
              tts.say("""HRP2 is going downstairs. The step are 15 centimeters high""")
            if req.phase==5:#stepping stones
              tts.say("""The robot walks on stones that are not on the same level""")
            if req.phase==6:#multicontact
              tts.say("""   """)
            if req.phase==7:#error
              tts.say("""humm humm,\\PAU=500\\ its seems something bad happened, I hope nothing is broken""")
            else:
              return Launch_speechResponse(0)    
            return Launch_speechResponse(1)
        except:
            return Launch_speechResponse(0)
        
    if language==0:
#        tts.setLanguage("French") 
 
        try:
            ab=abcdk_class()
            ab.onLoad()
            if req.phase==0: #presentation
              ab.onSay("""Bonjour, je m'appelle ROMEO.\\PAU=500\\ Je suis la plateforme de recherche d'Aldebaran Robotics.
    Bienvenue dans la salle Bozzil au Laas CNRS.
    Aujourd'hui, je vais vous présenter les développements
    de l'équipe Gépéto sur le robo \\PAU=200\\ HRP2.\\PAU=1000\\
    Voici les différentes épreuves qui sont tentées par HRP2 aujourd'hui.\\PAU=500\\
    une marche réactive commandée à la manette,\\PAU=500\\
    une marche corps complet\\PAU=500\\
    et enfin\\PAU=200\\ un algorithme de suivi de balle virtuelle, déplacé par un opérateur sur l'écran se trouvant en face de vous, nommé Moujoko.\\PAU=1000\\""")
#    """D'autres comportements vont vous tre présentés :
#    Il s'agit d'une mont�e des marches avec saisie de la rampe de l'escalier,
#    et d'un suivi de balle virtuelle, d�plac�e par un op�rateur sur l'ecran se trouvant en face de vous, grace � une souris 3D."""
    
                
            elif req.phase==1:#going upstairs
              ab.onSay("""HRP2 va maintenant monter l'escalier à 10 centimètres, les commandes envoyées à ses moteurs sont précalculées.\\PAU=500\\
    Pour éviter des risques de dégradations en cas de chute, une personne doit l'accompagner sur les marches mais ne le touchera pas.\\PAU=500\\
    De plusss, le pont roulant au dessus de vous, est controlé par un opérateur pour le sécuriser.
    Ceci explique notamment la présence de la télécommande""")      
            elif req.phase==2:#walking on the beam
              ab.onSay("Pour cette démonstration, HRP2 va tenter de traverser la poutre.\\PAU=500\\ Aucun systèmes de recalage en position n'est encore utilisé, la position de départ est donc ici très importante.\\PAU=300\\ Une erreur de quelques degrés peut faire chuter le robot sur le bord de la poutre.")
            elif req.phase==3:#Mujoko
              ab.onSay("""Voici maintenant la démonstration Moujoco.\\PAU=500\\
    L'objectif du robot est d'attraper une balle virtuelle avec sa main.\\PAU=500\\
    Afin de garantir la sécurité du robot et d'accomplir l'objectif,
    la tache principale doit rester le maintien en equilibre.\\PAU=300\\
    Le programme utilisé procède donc par hiérarchisation des taches.
    De plusss, le robot est capable de prévoir les autocollisions afin de les éviter""")
            elif req.phase==4:#going downstairs
              ab.onSay("""HRP2 va descendre des marches de 15 centimètres. Le taux de réussite sur cette démonstration est assez élevé""")
            elif req.phase==5:#stepping stones
              ab.onSay("""HRP2 marche sur des pierres posées à des hauteurs différentes""")
            elif req.phase==6:#multicontact
              ab.onSay(""" Dans cette démonstration, HRP2 est capable de se servir de la rampe 
pour monter des marches \\PAU=100\\ qui sont normalement trop hautes pour lui. \\PAU=500\\
Un algorithme est donc capable de prévoir une séquence de contact \\PAU=200\\ et une trajectoire de l'ensemble de ses 30 moteurs \\PAU=100\\ 
qui assure sa stabilité et son équilibre.""")
            elif req.phase==7:#remote
              ab.onSay(""" HRP2 est controlé avec une manette de console vidéo. \\PAU=500\\
Toutes les cinq millisecondes, le robo recalcule la position de ses deux prochains pas. \\PAU=300\\
De plusss la grue qui sert à assurer le robo en cas de chute se place automatiquement au dessus de lui.
""")
            elif req.phase==8:#Heidelberg
              ab.onSay(""" HRP2 va maintenant marcher en utilisant les mouvements fournis par nos collegues d'Heidelberg en Allemagne. Le robo utilise le haut du corps pour accroitre sa vitesse de déplacement. """)
            elif req.phase==9:#pickup
              ab.onSay(""" La prochaine démonstration est très particulière, une directive simple comme le ramassage d'un objet au sol est a l'origine d'un pas en arrière. L'algorithme est donc capable de combiner locomotion et manipulation""")
            elif req.phase==10:#error
              ab.onSay("""oula,\\PAU=500\\ Je crois que quelquechose s'est mal passé, j'espère qu'il n'y a pas de casse.""")
	    elif req.phase==11:#
              ab.onSay("""joyeux anniversaire Andréa""")
            else:
              return Launch_speechResponse(0)    
            return Launch_speechResponse(1)
        except:
            return Launch_speechResponse(0)

def comment_HRP2_server():
    rospy.init_node('romeo_comments_HRP2')
    s = rospy.Service('speech_by_phase', Launch_speech, speech_for_phase)
    print "Ready to comment HRP2."
   # ab1=abcdk_class()
   # ab1.onLoad()
   # ab1.onSay("Pour cette d�monstration, HRP2 va tenter de traverser la poutre.\\PAU=500\\ Aucun syst�mes de recalage en position n'est encore utilis� la position de d�part est donc ici tr�s importante.\\PAU=300\\ Une erreur de quelques degr�s peut faire chuter le robot sur le bord de la poutre.")
    rospy.spin()

if __name__ == "__main__":
    comment_HRP2_server()
