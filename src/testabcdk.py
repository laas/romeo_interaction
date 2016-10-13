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
        GeneratedClass.__init__(self);
        try:
            self.tts = ALProxy( "ALTextToSpeech" );
        except Exception, err:
            self.log( "ERR: tts seems not to be present, so we won't use it..." );
            self.tts = False;

    def onLoad(self):
        self.bMustStop = False;
        self.bIsRunning = False;

    def onUnload(self):
        self.onInput_onStop(); # stop current loop execution

    def onInput_onPrepare(self):
        abcdk.bodytalk.bodyTalk.prepare( bUseHead = self.getParameter( 'bUseHead' ), rSide = self.getParameter( "rSide" ), rElevation = self.getParameter( "rElevation" ),
                    astrJointsToExclude = eval(self.getParameter( "astrJointsToExclude" )),
                    astrObstacles = eval(self.getParameter( "astrObstacles" )),
        );

    def startBodyTalk( self, nSayID ):
        self.log( self.boxName + ": start - begin" );

        if( self.bIsRunning ):
            self.log( self.boxName + ": already started => nothing" );
            return;

        self.bIsRunning = True;
        self.bMustStop = False;

        abcdk.bodytalk.bodyTalk.start( bUseHead = self.getParameter( 'bUseHead' ), bTrackFace = self.getParameter( 'bTrackFace' ),
                nSayID = nSayID, astrJointsToExclude = eval(self.getParameter( "astrJointsToExclude" )), astrObstacles = eval(self.getParameter( "astrObstacles" )),
        );
        rPeriod = 0.5;
        while( not self.bMustStop ):
            bRet = abcdk.bodytalk.bodyTalk.update( rSide = self.getParameter( "rSide" ), rElevation = self.getParameter( "rElevation" ) );
            if( not bRet ):
                self.bMustStop = True;
            time.sleep( rPeriod );
        # end while
        abcdk.bodytalk.bodyTalk.stop();
        self.bIsRunning = False;
        self.onStopped();
        self.log( self.boxName + ": start - end" );


    def onInput_onStart(self):
        self.startBodyTalk( -1 );

    def onInput_onStop(self):
        self.bMustStop = True; # stop current loop execution

    def onInput_onSay( self, strTxt ):
        if( self.bIsRunning ):
            self.log( "Already running => nothing..." );
            return;
        nSayID = self.tts.post.say( "\\PAU=700\\ " + abcdk.speech.getTextWithCurrentSpeed( strTxt ) );
        self.startBodyTalk( nSayID );

# abcdk_BodyTalk - end
if __name__ == '__main__':
    tmp=abcdk_class()
    tmp.





    
