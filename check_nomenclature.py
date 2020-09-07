# Check naming nomenclature
import re


def check(selection):
    regex = re.compile(r"^(?P<asset>[A-Z]+)_(?P<side>C|L|R)_(?P<object>[A-Za-z0-9]+)_(?P<type>jnt|jntEnd|geo|ctrl|loc|clstr|crv|nbs|ikhl|grp|parentConstraint|poleVectorConstraint)$")
    grp_regex = re.compile(r"^(?P<asset>[A-Z]+)_(?P<object>SKL|CTRL|XTRAS|GEO)_(?P<type>grp)$")

    checked = False

    list_error = list()

    for each in selection:
        try:
            match = regex.match(each)
            match = match.groupdict()
            checked = True
        except:
            try:
                grp_match = grp_regex.match(each)
                grp_match = grp_match.groupdict()
                checked = True
            except:
                if "effector" not in each:
                    list_error.append(each)


    return checked, list_error



if __name__ == '__main__':

    maya_sel = cmds.ls(sl=True)

    check_pass, lst_error = check(maya_sel)

    if check_pass and lst_error == []:
        print("No error !")
    else:
        print("Some error in naming : ")
        for each in lst_error:
            print(each)