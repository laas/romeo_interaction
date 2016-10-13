#!/usr/bin/env python
# -*- coding: utf-8 -*-

from romeo_srv.srv import *
import rospy
import naoqi
from pynaoqi.naoqi import ALProxy

def speech_for_phase(req):
    print "speech"
    tts = ALProxy("ALTextToSpeech", "romeo03", 9559)
    language = 0 #0 for French, 1 for English
    if language==1:
        tts.setLanguage("English") 
## 
##        try:
##            if req.phase==0: #presentation
##              return Launch_speechResponse(0)
##                
##            if req.phase==1:#going upstairs
##              """tts.say(This is the first sequence of HRP2.
##    He is climbing 10 centimeters high steps.
##    The passage is narrow and the robot risks to strike the beam with his left hand
##    and the barrier with his right hand ) """
##              return Launch_speechResponse(1)
##            if req.phase==2:#walking on the beam
##              tts.say("""HRP2 is now walking on the beam.
##    Since the motion caption is not activated to correct the trajectory,
##    the initial position of the robot on the beam is very important""")
##            if req.phase==3:#Mujoko
##              tts.say("""This is now the Mujoko demonstration""")
##            if req.phase==4:#going downstairs
##              tts.say("""HRP2 is going downstairs. The step are 15 centimeters high""")
##            if req.phase==5:#stepping stones
##              tts.say("""The robot walks on stones that are not on the same level""")
##            if req.phase==6:#multicontact
##              tts.say("""   """)
##            if req.phase==7:#error
##              tts.say("""humm humm,\\PAU=500\\ its seems something bad happened, I hope nothing is broken""")
##            else:
##              return Launch_speechResponse(0)    
##            return Launch_speechResponse(1)
##        except:
##            return Launch_speechResponse(0)
        
    if language==0:
        tts.setLanguage("French") 
 
        try:
            if req.phase==0: #presentation
              return Launch_speechResponse(0)
                
            elif req.phase==1:#going upstairs
              """tts.say(HRP2 va maintenant monter l'escalier à 10 centimètres, les commandes envoyées à ses moteurs sont précalculées.\\PAU=500\\
    Pour éviter des risques de dégradations en cas de chute, une personne doit l'accompagner sur les marches mais ne le touchera pas.\\PAU=500\\
    De plusss, le pont roulant au dessus de vous, est controlé par un opérateur pour le sécuriser.
    Ceci explique notamment la présence de la télécommande)    """
              return Launch_speechResponse(1)
            elif req.phase==2:#walking on the beam
              """tts.say(Pour cette démonstration, HRP2 va tenter de traverser la poutre.\\PAU=500\\ Aucun systèmes de recalage en position n'est encore utilisé,
    la position de départ est donc ici très importante.\\PAU=300\\ Une erreur de quelques degrés peut faire chuter le robot sur le bord de la poutre.)"""
              return Launch_speechResponse(2)
            elif req.phase==3:#Mujoko
              tts.say("""Voici maintenant la démonstration Moujoco.\\PAU=500\\
    L'objectif est de suivre la balle avec la main du robot en temps ré elle.\\PAU=500\\
    Afin de garantir la sécurité du robot et d'accomplir cet objectif,
    la tache principale doit rester le maintien en l'equilibre. Le programme utilisé procède donc par hiérarchisation des taches""")
            elif req.phase==4:#going downstairs
              tts.say("""HRP2 va descendre des marches à 15 centimètres. Le taux de réussite sur cette démonstration est assez élevé""")
            elif req.phase==5:#stepping stones
              tts.say("""HRP2 marche sur des pierres posées à des hauteurs différentes""")
            elif req.phase==6:#multicontact
              tts.say(""" En multicontacte, HRP2 peut saisir la rampe pour s'aider à monter les marches""")
            elif req.phase==7:#error
              tts.say("""oula,\\PAU=500\\ Je crois que quelquechose s'est mal passé, j'espère qu'il n'y a pas de casse.""")
            else:
              return Launch_speechResponse(0)    
            #return Launch_speechResponse(1)
        except:
            pass

def comment_HRP2_server():
    rospy.init_node('romeo_comments_HRP2')
    s = rospy.Service('speech_by_phase', Launch_speech, speech_for_phase)
    print "Ready to comment HRP2."
    rospy.spin()

if __name__ == "__main__":
    comment_HRP2_server()
