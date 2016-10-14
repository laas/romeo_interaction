#!/usr/bin/env python
# coding: utf-8

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

if( 0 ):
    import abcdk.bodytalk
    import abcdk.bodytalk
    import abcdk.motiontools
    import abcdk.motiontools
    import abcdk.speech
from naoqi import ALProxy

import time
class abcdk_class():
    """ insert here your comments about this class """
    def __init__(self):
        #GeneratedClass.__init__(self);
        try:
            self.tts = ALProxy( "ALTextToSpeech" );
        except Exception, err:
            self.log( "ERR: tts seems not to be present, so we won't use it..." );
            self.tts = False;

    def onLoad(self):
        self.bMustStop = False;
        self.bIsRunning = False;

#    def onUnload(self):
#        self.onInput_onStop(); # stop current loop execution

    def onPrepare(self):
        abcdk.bodytalk.bodyTalk.prepare( bUseHead = True, rSide = 0, rElevation = 0, astrJointsToExclude = [], astrObstacles = [])

    def startBodyTalk( self, nSayID ):
#        self.log( self.boxName + ": start - begin" );

        if( self.bIsRunning ):
#            self.log( self.boxName + ": already started => nothing" );
            return;

        self.bIsRunning = True;
        self.bMustStop = False;

        abcdk.bodytalk.bodyTalk.start( bUseHead = True, bTrackFace = 0,nSayID = nSayID,astrJointsToExclude = "", astrObstacles = "")
        rPeriod = 0.5;
        while( not self.bMustStop ):
            bRet = abcdk.bodytalk.bodyTalk.update( rSide = 0, rElevation = 0 );
            if( not bRet ):
                self.bMustStop = True;
            time.sleep( rPeriod );
        # end while
        abcdk.bodytalk.bodyTalk.stop();
        self.bIsRunning = False;
#        self.onStopped();
#        self.log( self.boxName + ": start - end" );


    def onStart(self):
        self.startBodyTalk( -1 );

    def onStop(self):
        self.bMustStop = True; # stop current loop execution

    def onSay( self, strTxt ):
        if( self.bIsRunning ):
            self.log( "Already running => nothing..." );
            return;
        nSayID = self.tts.post.say( "\\PAU=700\\ " + abcdk.speech.getTextWithCurrentSpeed( strTxt ) );
        self.startBodyTalk( nSayID );

# abcdk_BodyTalk - end
if __name__ == '__main__':
    ab=abcdk_class()
    print "class initialized"
    #ab.tts.post.say( "\\PAU=700\\ " + abcdk.speech.getTextWithCurrentSpeed( "Bonjour, je m'appelle Roméo. Je suis la plateforme de recherche d'aldebaran robotics. Je sers a tester des nouvelles technologies matérielle et logicielle, mais aussi de nouveaux usages des robots humanoïdes. Dans le cadre du projet romeo2, 16 partenaires travaillent sur moi pour explorer l'aide à  la personne. Je suis fier de vous rencontrer au LAASSE aujourd'hui. \\PAU=500\\ Avec le groupe GEPETTO, je vais essayer d'ameliorer mes mouvements. \\PAU=500\\ Avec le groupe RAPE, je vais essayer d'ameliorer ma perception. \\PAU=500\\ Avec le groupe RISSE, je vais essayer de mieux interagir avec les etres humains. \\PAU=500\\ Mon camarade HRP-2 est moins fort que moi pour l'interaction avec l'homme. " ) );
    #abcdk.bodytalk.bodyTalk.start( bUseHead = True, bTrackFace = 0, nSayID = 0, astrJointsToExclude = "", astrObstacles = "")
    #time.sleep(2)
    #abcdk.bodytalk.bodyTalk.stop();
#    ab.onPrepare()
    ab.onLoad()
    ab.onSay( "Bonjour, je m'appelle Roméo. Je suis la plateforme de recherche d'aldebaran robotics. Je sers a tester des nouvelles technologies matérielle et logicielle, mais aussi de nouveaux usages des robots humanoïdes. Dans le cadre du projet romeo2, 16 partenaires travaillent sur moi pour explorer l'aide à  la personne. Je suis fier de vous rencontrer au LAASSE aujourd'hui. \\PAU=500\\ Avec le groupe GEPETTO, je vais essayer d'ameliorer mes mouvements. \\PAU=500\\ Avec le groupe RAPE, je vais essayer d'ameliorer ma perception. \\PAU=500\\ Avec le groupe RISSE, je vais essayer de mieux interagir avec les etres humains. \\PAU=500\\ Mon camarade HRP-2 est moins fort que moi pour l'interaction avec l'homme." )
