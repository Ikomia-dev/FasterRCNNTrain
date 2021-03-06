from ikomia import dataprocess
import FasterRCNNTrain_process as processMod
import FasterRCNNTrain_widget as widgetMod


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class FasterRCNNTrain(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return processMod.FasterRCNNTrainProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return widgetMod.FasterRCNNTrainWidgetFactory()
