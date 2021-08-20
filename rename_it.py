import maya.cmds as cmds
import re

def get_name():

    selection = cmds.ls(sl=True)

    for object_name in selection:
        regex = re.compile(
            r"(?P<reference>.*:)?(?P<asset>[A-Z]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>[a-zA-Z+]+)(?P<selection>.*)?")

        name = regex.match(object_name)

        if name is None:
            cmds.warning("Object " + object_name + " is not conform with the naming convention.")
        else:
            name = name.groupdict()

            create_loc_grp(name["asset"])

            locator_name = check_double(name)

            cmds.select(selection)

            return locator_name


def create_locator(name):

    cmds.cluster()

    sel = cmds.ls(sl=True, long=True)

    for clstr in sel:
        pos = cmds.xform(clstr, q=True, rp=True)
        cmds.delete(clstr)
        my_loc = cmds.spaceLocator(p=pos, n=name)
        cmds.xform(my_loc, cp=1)

    cmds.parent(name, "*locators_grp")

    cmds.makeIdentity(a=True, t=True, r=True, s=True, n=False, pn=True)


def create_loc_grp(asset):
    cmds.select(all=True, hi=True)

    xtras = False
    locator_bool = False

    xtras_n = asset + "_XTRAS_grp"
    locator_grp = asset + "_C_locators_grp"

    for element in cmds.ls(sl=True):
        if "XTRAS" in element:
            xtras = True
        if "locators_grp" in element:
            locator_bool = True

    if not xtras:
        cmds.group(p=asset + "_grp", n=xtras_n, em=True)
        cmds.group(p=xtras_n, n=locator_grp, em=True)
    elif not locator_bool:
        cmds.group(p=xtras_n, n=locator_grp, em=True)

    cmds.select(clear=True)


def check_double(groupdict):
    cmds.select(all=True, hi=True)

    name = groupdict["asset"] + "_" + groupdict["side"] + "_" + groupdict["object"]

    count = 0

    for element in cmds.ls(sl=True):
        if "loc" in element and name in element and not "Shape" in element:
            print(element)
            count+=1
            cmds.rename(element, name + str(count).zfill(2) + "_loc")

    if count == 0:
        name = name + "_loc"
    else:
        name = name + str(count + 1).zfill(2) + "_loc"
    return name


if __name__ == '__main__':

    locator = get_name()

    if locator not in ["", None]:
        create_locator(locator)
