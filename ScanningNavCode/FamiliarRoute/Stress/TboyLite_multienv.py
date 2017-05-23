# Copyright (c) 2007-2012, Michael J. Kahana.
#
# This file is part of PandaEPL.
#
# PandaEPL is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 2.1 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Alec Solway
# URL: http://memory.psych.upenn.edu/PandaEPL

## to "disable" keyboard, look at ignoreAll method of DirectObject
## to install modules to panda that are pre-compiled windows exe:
## must edit registry "install" path for python to point to panda3d version

from pandaepl.common import *
from random import shuffle
import os

class dboyLite:

    def __init__(self):
        """
        Initialize the experiment.
        """
        # Get experiment instance.
        exp = Experiment.getInstance()

        # Assign a label (folder name) to the data from when this was run
        #exp.setSessionNum(0)
        exp.setSessionNum(datetime.datetime.now().strftime("%y_%m_%d_%H_%M"))

        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Get VR environment object.
        vr = Vr.getInstance()

        # If this is the first time running this subject, 
        # initialize experiment parameters.
        if not exp.getState():
            # Load list of available stores.
            # Each store has an associated '.egg' file in the 
            # stores directory.
            storeDirList = os.listdir(config['storeDir'])
            storest       = []
            for store in storeDirList:
                if store[-4:] == '.egg':
                    storest.append(store[:-4])
   
            # Shuffle store list and reduce to the number of 
            # stores in the environment.
##            shuffle(stores)
            #stores = stores[:config['numStores']]
            
            # 0 alligator
            # 1 apple
            # 2 banana
            # 3 Benedict_Cumberbatch
            # 4 Beyonce
            # 5 brown_bear
            # 6 carrot
            # 7 cow
            # 8 cucumber
            # 9 drill
            # 10 duck
            # 11 elephant
            # 12 Emma_Watson
            # 13 flamingo
            # 14 George_Clooney
            # 15 giraffe
            # 16 goat
            # 17 grapes
            # 18 hammer
            # 19 Jennifer_Aniston
            # 20 Jim_Parsons
            # 21 Johnny_Depp
            # 22 Katy_Perry
            # 23 kitten
            # 24 lettuce
            # 25 Mark_Zuckerberg
            # 26 Natalie_Portman
            # 27 oranges
            # 28 panda
            # 29 Paul_McCartney
            # 30 puppy
            # 31 saw
            # 32 scissors
            # 33 screwdriver
            # 34 stapler
            # 35 tape_measure
            # 36 Taylor_Swift
            # 37 watermelon
            # 38 wrench
            # 39 zebra
            # 40 Zooey_Deschanel

            # note: code for assigning goals works as follows -
            # store = state['stores'][state['deliveries'][state['currentDelivery']]]
            # thus, order of the storest and its corresponding position vector must be set such that the first value is desired goal 1 and second is desired goal 2 (if you have a second goal per env)
            stores1 = [storest[14]]+[storest[24]]+[storest[39]]
            stores2 = [storest[25]]+[storest[32]]+[storest[8]]
            stores3 = [storest[12]]+[storest[5]]+[storest[33]]
            stores4 = [storest[26]]+[storest[0]]+[storest[31]]
            stores5 = [storest[3]]+[storest[37]]+[storest[13]]
            stores6 = [storest[36]]+[storest[7]]+[storest[35]]
            stores7 = [storest[20]]+[storest[15]]+[storest[9]]
            stores8 = [storest[4]]+[storest[30]]+[storest[27]]
            stores9 = [storest[29]]+[storest[2]]+[storest[38]]
            stores10 = [storest[22]]+[storest[10]]+[storest[17]]
            stores11 = [storest[21]]+[storest[6]]+[storest[18]]
            stores12 = [storest[40]]+[storest[34]]+[storest[1]]           

            ##add custom finish line for training/route following
            customgoal = [storest[41]]

            # Load list of available shops.
            shopDirList = os.listdir(config['shopDir'])
            shops       = []
            for shop in shopDirList:
                if shop[-4:] == '.egg':
                    shops.append(shop[:-4])
   
            shops = [shops[0]]+[shops[1]]+[shops[2]]



            
            # Load list of buildings.
            buildingDirList = os.listdir(config['buildingDir'])
            buildings       = []
            for building in buildingDirList:
                if building[-4:] == '.egg':
                    buildings.append(building[:-4])
            bldings = [buildings[24]]+[buildings[22]]+[buildings[10]]+[buildings[47]]+[buildings[14]]+[buildings[25]]+[buildings[2]]+[buildings[4]]

##            # Shuffle building list and reduce to the number of
##            # buildings in the environment.
##            shuffle(buildings)
##            bldings = buildings[:10]#config['numBuildings']]

            #now replicate list 9x
            m = 9
            buildings = bldings*m
            #print buildings
            #shuffle(buildings)
            buildings = buildings[:config['numBuildings']]

            # Load list of barrierss.
            barrierDirList = os.listdir(config['barrierDir'])
            barriers       = []
            for barrier in barrierDirList:
                if barrier[-4:] == '.egg':
                    barriers.append(barrier[:-4])

            #barriers = barriers[:config['numBarriers5']]

            # Construct random sequence of deliveries. numbers in the "deliveries" list refer to the index of "stores" (e.g. 0 = store 1)
##            deliveries = []
##            while len(deliveries) < config['numDeliveries']:
##                nextSequence = range(config['numStores'])
##                shuffle(nextSequence)
##                if len(deliveries) == 0 or deliveries[-1] != nextSequence[0]:
##                    deliveries.extend(nextSequence)
##            deliveries = deliveries[:config['numDeliveries']]
            
            #numdeliveries = config['numDeliveries']#total/across towns
            envs = config['environs']
            deliveries = config['deliveries'] # delivs per town
            # Save experiment parameters.
            exp.setState({'stores1': stores1,
                          'stores2': stores2,
                          'stores3': stores3,
                          'stores4': stores4,
                          'stores5': stores5,
                          'stores6': stores6,
                          'stores7': stores7,
                          'stores8': stores8,
                          'stores9': stores9,
                          'stores10': stores10,
                          'stores11': stores11,
                          'stores12': stores12,
                          'customgoal': customgoal,#custom goal, e.g. for training
                          'barriers': barriers,
                          'shops': shops,
                          'buildings': buildings,
                          'deliveries': deliveries,
                          'currentDelivery': 0,#within-town delivery idx
                          'envs': envs, #list of environment numbers
                          'envwarns': config['shockwarns'],#envs in which they get a shock warning
                          'envshocks': config['shockenvs'],#envs in which they get a shock
                          'envcount': 0, #total environment count
                          'score': config['startingScore'],
                          'fixation': config['fixationflag']})
            
        # Register custom log entry types.
        # They correspond to, respectively, arriving at a store,
        # being assigned to make a delivery to a new store,
        # and updating the score.
        Log.getInstance().addType("ARRIVED",[("STORE",basestring)], False)
        Log.getInstance().addType("ASSIGNED",[("STORE",basestring)], False)
        Log.getInstance().addType("SCORE",[("VALUE",int)], True)
        Log.getInstance().addType("INTRO",[("task_intro",basestring)],False)
        Log.getInstance().addType("SHOCKSTATE",[("shock_intro",basestring)],False)#this logs when ITI happens
        Log.getInstance().addType("ORIENT",[("orientation_time",basestring)],False)
        Log.getInstance().addType("NAVIGATE",[("start_to_nav",basestring)],False)
        Log.getInstance().addType("SCAN",[("scan_trigger",basestring)],False)
        Log.getInstance().addType("SHOCK",[("shock_trigger",basestring)],False)
        

       
        # Load environment.
        self.loadEnvironment()


        # Set up lighting.
        self.lightingScheme = config['initialLightingScheme']
        self.setUpLighting()

        # Create text field to display the participant's score in
        #the upper right hand corner.
        self.score = Text("score", str(config['startingScore']), 
                          config['scorePos'], config['scoreSize'], 
                          config['scoreColor'], config['instructFont'])

        # Create text field to display current delivery.
        self.assignment = Text("assignmentHUD", "", config['assignmentPos'], 
                               config['assignmentSize'], config['assignmentColor'], 
                               config['instructFont'])

        # Register task to decrement score at a constant rate.
        vr.addTask(Task("decrementScore", 
                    lambda taskInfo: 
                      self.updateScore(-config['scoreDecrement']), 
                    config['scoreDecrementInterval']))
        
        # Sound related variables.
        self.sound       = None
        self.isRecording = False

        # Handle keyboard events.
        #vr.inputListen("toggleLighting", self.toggleLighting)
        #vr.inputListen("toggleFog", self.toggleFog)
        vr.inputListen("toggleDebug", 
                       lambda inputEvent: 
                         Vr.getInstance().setDebug(not Vr.getInstance().isDebug()))

        #keyboard.ignoreAll()

    def loadEnvironment(self):
        """
        Load terrain, sky, buildings and stores.
        """
        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Get experiment parameters.
        state = Experiment.getInstance().getState()

        # Load terrain.
        modid = 'terrain'+str(state['envcount'])
        modnum = 'terrainModel'+str(state['envs'][state['envcount']])#modnum = 'terrainModel'+str(state['envcount'])
        self.terrainModel = Model(modid, config[modnum], 
                                  config['terrainCenter'])

        # When hitting an object that is part of the terrain, slide across it.
        self.terrainModel.setCollisionCallback(MovingObject.handleSlideCollision)

        # Load sky.
        self.skyModel = Model("sky", config['skyModel'])
        self.skyModel.setScale(config['skyScale'])
                                       
        # Load stores. these are goal objects, not necessarily "stores"
        storelist = 'stores'+str(state['envs'][state['envcount']])
        storeloclist = 'storeLocs'+str(state['envs'][state['envcount']])
        state['stores'] = state[storelist]

        # Save new goal states.
        Experiment.getInstance().setState(state)

        # Load stores. these are goal objects, not necessarily "stores"
        self.storeModels = []
        for i, store in enumerate(state['stores']):
            storeModel = Model(store, 
                               os.path.join(config['storeDir'], store+".bam"),

                               Point3(config[storeloclist][i][0], 
                                      config[storeloclist][i][1], 
                                      config['storeZ'])#,
                               #self.collideStore) #commenting out disables collision
                               )
            storeModel.setH(config[storeloclist][i][2])
            self.storeModels.append(storeModel)



        # Load a custom goal - used for training (could be invisible barrier for circumnavigating route)
        #finishlist = 'stores'+str(state['envs'][state['envcount']])
        finishloclist = 'custLocs'+str(state['envs'][state['envcount']])
        #state['stores'] = state[storelist]

        # Save new goal states.
        #Experiment.getInstance().setState(state)
        
        self.custgoalModels = []
        for i, storeg in enumerate(state['customgoal']):
            custgoalModel = Model(storeg, 
                               os.path.join(config['storeDir'], storeg+".bam"),
                               Point3(config[finishloclist][i][0], 
                                      config[finishloclist][i][1], 
                                      config['custZ']),
                               self.collideStore) #commenting out disables collision
                               
            custgoalModel.setH(config[finishloclist][i][2])
            self.custgoalModels.append(custgoalModel)

##        #Run a matlab script from task
##        import win32com.client
##        import sys, time
##        def execute_matlab_command(command):
##            handle = win32com.client.Dispatch('matlab.application')
##            handle.visible = True
##            handle.Execute(command)
##        execute_matlab_command("run('C:\\Users\\waglab\\Documents\\Thackery\\Tboy\\matlabplottest.m')")

        #position participant at REAL staring pos
        postion = 'initialPos'+str(state['envs'][state['envcount']])
        Avatar.getInstance().setPos(config[postion])

        #orient participant to starting heading
        heading = 'initialHead'+str(state['envs'][state['envcount']])
        Avatar.getInstance().setH(config[heading][0][0])
        
    def setUpLighting(self):
        """
        Set up lighting according to the current scheme.
        """
        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Delete previous lights.
        self.ambLight             = None
        self.demoDirectionalLight = None
        self.demoPointLight       = None
        self.demoSpotlight        = None

        # Bright ambient light.
        if self.lightingScheme == 0:
            self.ambLight = AmbientLight("ambLight", config['brightAmbientLightColor'])
        # Dark ambient light, directional light.
        elif self.lightingScheme == 1:
            self.ambLight             = AmbientLight("ambLight", 
                                                     config['darkAmbientLightColor'])
            self.demoDirectionalLight = DirectionalLight("demoDirectionalLight", 
                                                         config['directionalLightOrient'], 
                                                         config['directionalLightColor'])
        # Dark ambient light, point light.
        elif self.lightingScheme == 2:
            render.clearLight()
            self.ambLight       = AmbientLight("ambLight", 
                                               config['darkAmbientLightColor'])
            self.demoPointLight = PointLight("demoPointLight", 
                                             config['pointLightPos'], 
                                             config['pointLightAttenuation'], 
                                             config['pointLightColor'])
        # Dark ambient light, spotlight.
        elif self.lightingScheme == 3:
            self.ambLight      = AmbientLight("ambLight", 
                                              config['darkAmbientLightColor'])
            self.demoSpotlight = SpotLight("demoSpotlight", 
                                           config['spotlightPos'], 
                                           config['spotlightFallof'], 
                                           config['spotlightHorzFov'], 
                                           None, 
                                           config['spotlightColor'])


    def start(self):
        """
        Start the experiment.
        """
        self.intro()
        Experiment.getInstance().start()


    def intro(self):
        scanflag = 1#change to 0 if not scanning - code will crash if it can't find USB (trigger) device
        """
        Present introductory screens.
        """
        # Read intro text in from external text file.
##        fid       = open(Conf.getInstance().getConfig()['instructionFile'], 'r')
##        introText = fid.read()
##        fid.close()
##
##        # Display intro text followed by information about the first delivery.
##        Instructions("intro", introText).display()#, self.showDeliveryInfo
        
        # custom log label for this event
        VLQ.getInstance().writeLine("INTRO",['task_introduced'])
        
        """
        scan trigger
        """
        def scantrig(task):
            ser.write('[t]\n');# send out pulse, must be adjusted to whatever scanner users as trigger
            #sleep(1)
            print 'scan!'
            # Log the shock.
            VLQ.getInstance().writeLine("SCAN",['scan_triggered'])
            
            ser.close()

        if scanflag == 1: #if we are scanning (that is, a trigger is plugged in
            import serial
            #from time import sleep
            #import sys, os, time #only import if this wasn't done previously
            device = 'COM4' #COM4 is back right USB port on Nico - change as needed
            ser = serial.Serial(device, 57600, timeout=0.05)
            taskMgr.doMethodLater(2,scantrig,'trigscan')#if the goal instructions last 8s, we want to shoot for ~n+8 as our delay


        def instructstop(task):
            """
            Clear current instruction screen and begin task
            """
##            Instructions.currentlyDisplayed.displayOff(Instructions.currentlyDisplayed)
            config = Conf.getInstance().getConfig()

            # Create text field to display shock status of new town.
            state = Experiment.getInstance().getState()# Get experiment parameters.
            warn = state['envwarns']
            fixation = state['fixation']
            if fixation == 1:#if we are just showing fixations during ITI
                Instructions("warning", config['fixation']).display()
                Instructions.currentlyDisplayed.text.setColor(config['fixColor'])
                Instructions.currentlyDisplayed.text.setPos(config['fixPos'])
                Instructions.currentlyDisplayed.text.setScale(config['fixSize'])
            elif warn[state['envcount']] == 1:#if we are showing text, is is a "shock warning"?
                Instructions("warning", config['shockWarning']).display()
                Instructions.currentlyDisplayed.text.setColor(config['shockColor'])
                Instructions.currentlyDisplayed.text.setPos(config['shockPos'])
                Instructions.currentlyDisplayed.text.setScale(config['shockSize'])
            else: #...or no warning?
                Instructions("nowarning", config['noshockWarning']).display()
                Instructions.currentlyDisplayed.text.setScale(config['shockSize'])
            # custom log label for this event
            VLQ.getInstance().writeLine("SHOCKSTATE",['shock_state_introduced'])

            def turnme(task):
                diff = (task.time - self.oldturnTaskTime) #* rotspeed
                if diff >= 1.25:
                    Avatar.getInstance().setH(Avatar.getInstance().getH()+45)
                    self.oldturnTaskTime = task.time
                return task.cont
                     
            def teststop(task):
                taskMgr.remove('rightaround')
                # Show next delivery
                self.showDeliveryInfo()
                # reference Vr and config
                vr = Vr.getInstance()
                config = Conf.getInstance().getConfig()

## added 4/4/2016 ~~~~~~~~~~~~
                def shock(task):
                    ##Trigger shock machine    
##                    import serial
##                    from time import sleep
##                    #import sys, os, time #only import if this wasn't done previously
##                    device = 'COM5' #COM5 is ___ ___ USB port on Nico - change as needed
##                    ser = serial.Serial(device, 57600, timeout=0.05)
                    #sleep(2)
                    #ser.read()
                    ser.write('t\n');# send out pulse
                    #sleep(1)
                    print 'zap!'
                    # Log the shock.
                    VLQ.getInstance().writeLine("SHOCK",['zap_delivered'])
                    
                    ser.close()
    
                #options = Options.getInstance().get()
                
                #subj_list = ['s3']
                #if options.subjId in subj_list: #or 's4' or 's5':#only deliver shock in this env for specific subs
                state = Experiment.getInstance().getState()    
                shockstate = state['envshocks']
                if shockstate[state['envcount']] == 1:#if we are showing text, is is a "shock warning"?
                    import serial
                    #from time import sleep
                    #import sys, os, time #only import if this wasn't done previously
                    device = 'COM5' #COM5 is ___ ___ USB port on Nico - change as needed
                    ser = serial.Serial(device, 57600, timeout=0.05)
                    taskMgr.doMethodLater(18,shock,'zap')#if the goal instructions last 8s, we want to shoot for ~n+8 as our delay
## added 4/4/2016 ^^^^^^^^




                #reset score countdown for new env
                state = Experiment.getInstance().getState()# Get experiment parameters.
                state['score'] = config['startingScore']# Update score.
                VLQ.getInstance().writeLine("SCORE", [state['score']])# Log new score.
                self.score.setText(str(state['score']))  # Update heads-up display.
                Experiment.getInstance().setState(state) # Save new score.

                

            def stopshockwarn(task):
                Instructions.currentlyDisplayed.displayOff(Instructions.currentlyDisplayed)

                # custom log label for this event
                VLQ.getInstance().writeLine("ORIENT",['oriented_to_env'])
                
                self.oldturnTaskTime = 0.0
                taskMgr.add(turnme,'rightaround')

            taskMgr.doMethodLater(10, stopshockwarn, 'clearwarning')    
            taskMgr.doMethodLater(21,teststop,'stopthattask')
        
        taskMgr.doMethodLater(0,instructstop,'clearinst')


    def collideStore(self, collisionInfoList):
        """
        Handle the participant colliding with a store.
        """
        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Get experiment parameters.
        state = Experiment.getInstance().getState()

        # ID of the store (goal) the participant collided with.
        store = collisionInfoList[0].getInto().getIdentifier()

        # Log collision.
        VLQ.getInstance().writeLine("ARRIVED", [store])

        # If a delivery is currently assigned, is this the goal where it is going?
        if state['currentDelivery'] >= 0 and \
           state['currentDelivery'] < len(state['deliveries']) and \
           store == state['customgoal'][0]:            ## custom goal - e.g. invisible barrier for training
           #store == state['stores'][state['deliveries'][state['currentDelivery']]]:
            # Update score.
            self.updateScore(config['deliveryBonus'])
            
            # Inform participant that they have made the delivery and assign the next one.
            Instructions("deliveryMade", 
                         config['deliveryMadeText']).display() # % self.storeName(store)).display()
            Instructions.currentlyDisplayed.text.setPos(config['victoryscreenPos'])
            def victorystop(task):
                """
                Clear current victory screen
                """
                Instructions.currentlyDisplayed.displayOff(Instructions.currentlyDisplayed)
                # set up next delivery
                self.nextDelivery()                
               
            taskMgr.doMethodLater(2,victorystop,'stopthatvictory') #note: when a new town is being loaded, several processes slow computer down, causing duration to be extended by ~2s. So with a 2, the victore screen will be up nearly 4s
            
        # Don't let the participant move inside the goal.
        MovingObject.handleRepelCollision(collisionInfoList)

    def nextDelivery(self):
        """
        Give the participant their next assignment.
        """
        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Get experiment parameters.
        state = Experiment.getInstance().getState()

        # If all deliveries have not been made prior to this one.
        if state['currentDelivery'] < len(state['deliveries']):
            # Move on to next delivery.
            state['currentDelivery'] += 1

            # Save next delivery.
            Experiment.getInstance().setState(state)
           

            
            
            ## if we are doing another trial in same env
            if state['currentDelivery'] < len(state['deliveries']):

                #reposition participant to new location
                #set new starting pos for new env
                Avatar.getInstance().setPos(config['laterPos'][state['envcount']])

                #i = 0
                #Avatar.getInstance().setPos(config['laterPos'][i])

                #reorient participant to new starting heading
                Avatar.getInstance().setH(config['laterHead'][state['envcount']][0])
                        
                #Avatar.getInstance().setH(config['laterHead'][i])
                
                #temporarily clear the goal text from HUD
                self.assignment.setText("")

                
                # handle rotation to survey new loc, then show next delivery
                def turnme(task):
                    """
                    Turns around a set amount of degrees after a certain time has elapsed
                    """
                    diff = (task.time - self.oldturnTaskTime) #* rotspeed
                    if diff >= 1.25:
                        Avatar.getInstance().setH(Avatar.getInstance().getH()+45)
                        self.oldturnTaskTime = task.time
                    return task.cont

                        
                def teststop(task):
                    taskMgr.remove('rightaround')
                    self.showDeliveryInfo()

                # custom log label for this event
                VLQ.getInstance().writeLine("ORIENT",['oriented_to_env'])

                self.oldturnTaskTime = 0.0
                taskMgr.add(turnme,'rightaround')
                taskMgr.doMethodLater(11,teststop,'stopthattask')
            # if we are moving on to new town    
            else:
                #update environment count
                state['envcount'] += 1
                #display new env
                self.showDeliveryInfo()
     
        
    def showDeliveryInfo(self):
        """
        Display information about the current delivery.
        """
        # Get configuration dictionary.
        config = Conf.getInstance().getConfig()

        # Get experiment parameters.
        state = Experiment.getInstance().getState()

                       #   'envs': envs, #list of environment numbers
                       #   'envcount': 1, #total environment count

        def insstop(task):
            """
            Clear current instruction screen
            """
            Instructions.currentlyDisplayed.displayOff(Instructions.currentlyDisplayed)
            ##   self.assignment.setText(self.storeName(store))#display current goal on HUD

            # record video (SLOW! But necessary for some purposes - e.g. training task or presentation)
            #base.movie(namePrefix='./trainvid/vid', duration=100, fps=24, format='jpg', sd=4, source=None)

            # custom log label for this event
            VLQ.getInstance().writeLine("NAVIGATE",['started_navigation'])

        # If all deliveries have been made, end the run/experiment.
        if state['envcount'] == len(state['envs']):
            Instructions("experimentComplete", config['experimentCompleteText'], 
                         Experiment.getInstance().stop).display()
##        if state['currentDelivery'] == len(state['deliveries']):
##            Instructions("experimentComplete", config['experimentCompleteText'], 
##                         Experiment.getInstance().stop).display()

        elif state['currentDelivery'] == len(state['deliveries']):

           
            #test loading in a new env       
            def loadNewEnvironment(task):
                """
                Load terrain, sky, buildings and stores.
                """
                # Get configuration dictionary.
                config = Conf.getInstance().getConfig()

                # Get experiment parameters.
                state = Experiment.getInstance().getState()

                # Load terrain.
                #model id
                modid = 'terrain'+str(state['envcount'])
                modnum = 'terrainModel'+str(state['envs'][state['envcount']])#modnum = 'terrainModel'+str(state['envcount'])
                self.terrainModel = Model(modid, config[modnum], 
                                          config['terrainCenter'])
                #self.terrainModel = Model("terrain1", config['terrainModel1'], 
                #                          config['terrainCenter'])

                # When hitting an object that is part of the terrain, slide across it.
                self.terrainModel.setCollisionCallback(MovingObject.handleSlideCollision)              

                #set stores exp state to those of the new env
                #exp.setState({'stores': stores1})
                storelist = 'stores'+str(state['envs'][state['envcount']])
                storeloclist = 'storeLocs'+str(state['envs'][state['envcount']])
                state['stores'] = state[storelist]
                finishloclist = 'custLocs'+str(state['envs'][state['envcount']])#new custom target location for env
    
                # Save new goal states.
                Experiment.getInstance().setState(state)

                # Load stores. these are goal objects, not necessarily "stores"
                self.storeModels = []
                for i, store in enumerate(state['stores']):
                    storeModel = Model(store, 
                                       os.path.join(config['storeDir'], store+".bam"),

                                       Point3(config[storeloclist][i][0], 
                                              config[storeloclist][i][1], 
                                              config['storeZ']))#,
                                       
                                       #self.collideStore)
                    storeModel.setH(config[storeloclist][i][2])
                    self.storeModels.append(storeModel)

                # Load a custom goal - used for training (could be invisible barrier for circumnavigating route)
                self.custgoalModels = []
                for i, storeg in enumerate(state['customgoal']):
                    custgoalModel = Model(storeg, 
                                       os.path.join(config['storeDir'], storeg+".bam"),
                                       Point3(config[finishloclist][i][0], 
                                              config[finishloclist][i][1], 
                                              config['custZ']),
                                       self.collideStore) #commenting out disables collision
                                       
                    custgoalModel.setH(config[finishloclist][i][2])
                    self.custgoalModels.append(custgoalModel)
                                                     

            taskMgr.add(loadNewEnvironment,'newen')
            #taskMgr.doMethodLater(60,loadNewEnvironment,'newtown')

            #set new starting pos for new env
            #Avatar.getInstance().setPos(config['newstartPos'][state['envcount']-1])
            postion = 'initialPos'+str(state['envs'][state['envcount']])
            Avatar.getInstance().setPos(config[postion])

            #reset within-town delivery counter
            state['currentDelivery'] = 0

            ## ITI + introduce them to next env
            # Create text field to display ITI fixation or shock status of new town (which stands in for ITI).
            warn = state['envwarns']
            fixation = state['fixation']
##            if fixation == 1:#if we are just showing fixations during ITI
            Instructions("warning", config['fixation']).display()#, self.showDeliveryInfo
            Instructions.currentlyDisplayed.text.setColor(config['fixColor'])
            Instructions.currentlyDisplayed.text.setPos(config['fixPos'])
            Instructions.currentlyDisplayed.text.setScale(config['fixSize'])
##            elif warn[state['envcount']] == 1:#if we are showing text, is is a "shock warning"?
##                Instructions("warning", config['shockWarning']).display()#, self.showDeliveryInfo
##                Instructions.currentlyDisplayed.text.setColor(config['shockColor'])
##                Instructions.currentlyDisplayed.text.setPos(config['shockPos'])
##                Instructions.currentlyDisplayed.text.setScale(config['shockSize'])
##            else: #...or no warning?
##                Instructions("nowarning", config['noshockWarning']).display()#, self.showDeliveryInfo
##                Instructions.currentlyDisplayed.text.setScale(config['shockSize'])

                            
            def newenvintro(task):
                #orient participant to starting heading
                heading = 'initialHead'+str(state['envs'][state['envcount']])
                Avatar.getInstance().setH(config[heading][0][0])
                
                """
                Clear current instruction screen and begin task
                """
                Instructions.currentlyDisplayed.displayOff(Instructions.currentlyDisplayed)
                def turnme(task):
                    diff = (task.time - self.oldturnTaskTime) #* rotspeed
                    if diff >= 1.25:
                        Avatar.getInstance().setH(Avatar.getInstance().getH()+45)
                        self.oldturnTaskTime = task.time
                    return task.cont
                         
                def teststop(task):
                    taskMgr.remove('rightaround')
                    # Show next delivery
                    self.showDeliveryInfo()
                    # reference Vr and config
                    vr = Vr.getInstance()
                    config = Conf.getInstance().getConfig()

## added 4/4/2016 ~~~~~~~~~~~~~~
                    def shock(task):
                        ##Trigger shock machine    
    ##                    import serial
    ##                    from time import sleep
    ##                    #import sys, os, time #only import if this wasn't done previously
    ##                    device = 'COM5' #COM5 is ___ ___ USB port on Nico - change as needed
    ##                    ser = serial.Serial(device, 57600, timeout=0.05)
                        #sleep(2)
                        #ser.read()
                        ser.write('t\n');# send out pulse
                        #sleep(1)
                        print 'zap!'
                        # Log the shock.
                        VLQ.getInstance().writeLine("SHOCK",['zap_delivered'])
                        
                        ser.close()
        
                    #options = Options.getInstance().get()
                    
                    #subj_list = ['s3']
                    #if options.subjId in subj_list: #or 's4' or 's5':#only deliver shock in this env for specific subs
                    state = Experiment.getInstance().getState()    
                    shockstate = state['envshocks']
                    if shockstate[state['envcount']] == 1:#if we are showing text, is is a "shock warning"?
                        import serial
                        #from time import sleep
                        #import sys, os, time #only import if this wasn't done previously
                        device = 'COM5' #COM5 is ___ ___ USB port on Nico - change as needed
                        ser = serial.Serial(device, 57600, timeout=0.05)
                        taskMgr.doMethodLater(18,shock,'zap')#if the goal instructions last 8s, we want to shoot for ~n+8 as our delay
## added 4/4/2016 ^^^^^^^^

                    #reset score countdown for new env
                    state = Experiment.getInstance().getState()# Get experiment parameters.
                    state['score'] = config['startingScore']# Update score.
                    VLQ.getInstance().writeLine("SCORE", [state['score']])# Log new score.
                    self.score.setText(str(state['score']))  # Update heads-up display.
                    Experiment.getInstance().setState(state) # Save new score.
                    
                    #base.movie(namePrefix='./trainvid/vid', duration=100, fps=24, format='jpg', sd=4, source=None)

                # custom log label for this event
                VLQ.getInstance().writeLine("ORIENT",['oriented_to_env'])
            
                self.oldturnTaskTime = 0.0
                taskMgr.add(turnme,'rightaround')
                taskMgr.doMethodLater(11,teststop,'stopthattask')
                
                                  
            taskMgr.doMethodLater(12,newenvintro,'clearinst')# duration of ITI or shock warning. **NOTE** due to flaws in resource allocation, the preceding process (victory screen) runs long and bleeds into this time. True task timing: thus number + victorystop delay (e.g. 12+2), but victory screen might occupy more than 2s of those 14s



                
##            store = state['stores'][state['deliveries'][state['currentDelivery']]]
##            VLQ.getInstance().writeLine("ASSIGNED", [store])#log assignment
##            #self.assignment.setText(self.storeName(store))#display current goal on HUD
##
##            Instructions("assignmentInstruct", #displays black screen with instruction text
##                         config['assignmentText'] % self.storeName(store)).display()
##            taskMgr.doMethodLater(8,insstop,'stopthatins')


            
        # Otherwise, display information about the current delivery within the town.
        else:
            #store = state['stores'][state['deliveries'][state['currentDelivery']]]
            ## custom goal - e.g. invisible barrier for training
            store = state['customgoal'][0]
            VLQ.getInstance().writeLine("ASSIGNED", [store])#log assignment
            #self.assignment.setText(self.storeName(store))#display current goal on HUD

            Instructions("assignmentInstruct", #displays black screen with instruction text
                         config['assignmentText']).display() #% self.storeName(store)).display()
            Instructions.currentlyDisplayed.text.setPos(config['assignmentscreenPos'])

            taskMgr.doMethodLater(8,insstop,'stopthatins')
            



            
    def updateScore(self, deltaScore):
        """
        Update the participant's score.
        """
        # Get experiment parameters.
        state = Experiment.getInstance().getState()

        # Update score.
        state['score'] = max(0, state['score'] + deltaScore)

        # Log new score.
        VLQ.getInstance().writeLine("SCORE", [state['score']])

        # Update heads-up display.
        self.score.setText(str(state['score']))

        # Save new score.
        Experiment.getInstance().setState(state)



    def storeName(self, store):
        """
        Given a store ID, return its name.
        """
        return store.replace("_", " ")

dboyLite().start()

