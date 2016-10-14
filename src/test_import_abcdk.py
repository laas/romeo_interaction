#!/usr/bin/env python

from naoqi import *
broker = ALBroker("pythonBroker","",0,"127.0.0.1",9559)
import sys
sys.path.append('/home/nao/.local/lib/python2.7/site-packages')
import abcdk
"""sys.path.append('/opt/naoqi/lib')
try: import abcdk.bodytalk; print "abcdk.bodytalk ok"
except: print "no abcdk.bodytalk" # this error could occurs only on first execution, it's handled in the installer
try: import abcdk.naoqitools; print "abcdk.naoqitools ok"
except: print "no abcdk.naoqitools"
try: import abcdk.speech; print "abcdk.speech ok"
except: print "no abcdk.speech"
try: import abcdk; print "abcdk ok"
except: print "no abcdk"

if( 0 ):
    import abcdk.bodytalk
    import abcdk.bodytalk
    import abcdk.motiontools
    import abcdk.motiontools
    import abcdk.speech
from naoqi import ALProxy
print "\n\n +++++++++++++++++"
print sys.path

import abcdk.bodytalk.bodyTalk"""
from abcdk  import bodytalk
abcdk.bodytalk.bodyTalk.prepare()

