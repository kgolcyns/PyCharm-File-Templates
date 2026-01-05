## ## USER INPUT Variables: Set this in calling parent:
## #if(false)
##     $Class_Name
##     $Subclass_of
## #end
## ## REQUIRED to set in calling template variable names:
## #set( $CLASS = $Class_Name)
## #set( $BASE = $Subclass_of)
##
## derived variables from input:
#set( $UIC_MODULE = "${CLASS}_Ui")
#set( $UIC_FILE = "${UIC_MODULE}.py")
#set( $UIC_CLASS = "Ui_${CLASS}")
#set( $DESIGNER_FILE = "${CLASS}.ui")
## ----------------------------------------
#parse("header.py")
from PyQt5.QtWidgets import $BASE
from $UIC_MODULE import $UIC_CLASS


class ${CLASS}($BASE, $UIC_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # #[[ $END$ ]]#

# TODO: Compile ui, ensure object name in designer file matches Class Name
#  run: python -m PyQt5.uic.pyuic $DESIGNER_FILE -o $UIC_FILE
#parse("widget_ifmain.py")
