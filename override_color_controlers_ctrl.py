import maya.cmds as cmds
import re


def override(sel):

    for each in sel:
        my_shape_ctrl = each + "Shape"
    
        cmds.setAttr(my_shape_ctrl + ".overrideEnabled", 1)
    
        if "_C_" in each:
            cmds.setAttr(my_shape_ctrl + ".overrideColor", 17)
            if "ultimate" in each.lower():
                cmds.setAttr(my_shape_ctrl + ".overrideColor", 14)
   
        if "_R_" in each:
            cmds.setAttr(my_shape_ctrl + ".overrideColor", 13)
        
        if "_L_" in each:
            cmds.setAttr(my_shape_ctrl + ".overrideColor", 6)
            
def check(my_sel):
    regex = re.compile(r"^(?P<asset>[A-Z]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp)$")
    
    checked = True
    
    for each in my_sel:
        try:
            matched = regex.match(each)
            matched = matched.groupdict()
        except:
            checked = False
            print("Your controlers ar not well named. Please, rename \" " + each + "\" and try again.")

            
    return checked
            
    
sel = cmds.ls(sl=True)
    
check_ok = False
    
check_ok = check(sel)
    
if check_ok:
    override(sel)