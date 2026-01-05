## Set order of variables here
#if(false)
    $Class_Name
    $Subclass_of
#end
## set variable names here
#set( $CLASS = $Class_Name)
#set( $BASE = $Subclass_of)
## --------------------
#parse("header.py")
import sys
from PyQt5.QtWidgets import $BASE
from PyQt5.QtCore import Qt


class $CLASS($BASE):
    def __init__(self, parent=None):
        super().__init__(parent)
        # #[[ $END$ ]]#


#parse("widget_ifmain.py")
