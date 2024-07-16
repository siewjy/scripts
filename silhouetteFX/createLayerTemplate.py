import fx

from fx import *

from tools.objectIterator import getObjects



class CreateLayersTemplateAction(Action):



    #This creates the new Function

    def __init__(self,):

        Action.__init__(self, "BGPrep|Create Layer Template")



    def execute(self):
        if fx.selection() == []:
            displayError("Select Roto Node", title="Error")
            return

        fg = {"id": "FG", "label": "FG", "value": True}
        fg2 = {"id": "FG2", "label": "FG2", "value": False}
        fg3 = {"id": "FG3", "label": "FG3", "value": False}
        
        mg = {"id": "MG", "label": "MG", "value": True}
        mg2 = {"id": "MG2", "label": "MG2", "value": False}
        mg3 = {"id": "MG3", "label": "MG3", "value": False}
        
        bg = {"id": "BG", "label": "BG", "value": True}
        bg2 = {"id": "BG2", "label": "BG2", "value": False}
        bg3 = {"id": "BG3", "label": "BG3", "value": False}

        layers = [fg,fg2,fg3,mg,mg2,mg3,bg,bg2,bg3]
        r = fx.getInput(title="Create Roto Layers", msg="Select the Layers to be created", fields=layers)
        
        #Creates List from User Inputs
        selection = []
        if r["FG"] == True:
            selection.append("FG")
        if r["FG2"] == True:
            selection.append("FG2")
        if r["FG3"] == True:
            selection.append("FG3")
            
        if r["MG"] == True:
            selection.append("MG")
        if r["MG2"] == True:
            selection.append("MG2")
        if r["MG3"] == True:
            selection.append("MG3")
            
        if r["BG"] == True:
            selection.append("BG")
        if r["BG2"] == True:
            selection.append("BG2")
        if r["BG3"] == True:
            selection.append("BG3")
        
        print (selection)
            

        node = activeNode()

        session = node.session

        rlayers = node.children
        missinglayers = selection



        for child in rlayers:

            if child.label in missinglayers:

                missinglayers.remove(child.label)



        if len(missinglayers) <= 0:

            print("All root layers are present")

            return



        layer = [Layer(name) for name in missinglayers]

        layer.reverse()


        beginUndo("Create Layers")



        if node.type == "RotoNode":

            for l in layer:

                node.property("objects").addObjects([l])

                rCh = Layer("{}_Red".format(l.label))

                gCh = Layer("{}_Green".format(l.label))

                bCh = Layer("{}_Blue".format(l.label))

                channels = [rCh, gCh, bCh]

                channels.reverse()

                l.property("objects").addObjects([o for o in channels])
            
                #Set Channel output for each RGB Layer
                rCh.property("channel").setValue("Red")
                gCh.property("channel").setValue("Green")
                bCh.property("channel").setValue("Blue")



        endUndo()





addAction(CreateLayersTemplateAction())
