## Variables: $CLASS
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    
    if sys.excepthook is sys.__excepthook__:
        sys.excepthook = lambda *args, **kwargs: sys.__excepthook__(*args, **kwargs)
    
    app = QApplication(sys.argv)
    
    win = ${CLASS}()
    win.show()
    win.raise_()
    
    app.exec_()
