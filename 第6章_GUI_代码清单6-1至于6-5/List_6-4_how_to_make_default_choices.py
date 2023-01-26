import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanilla') # Here 's the default
easygui.msgbox("You entered " + flavor)
