
def concat(*text, **kwargs):
    """

    Args:
        *text: multiple input
        **kwargs=separator: separator input

    Returns:
        str : concatenated text

    """
    try:
        if len(kwargs) == 0:
            return "".join(text)
        elif len(kwargs)==1:
            return str(kwargs["separator"]).join(text)
        else:
            raise RuntimeError("kwargs only accept one key word")
    except KeyError:
        print("Key word incorrect. Use separator instead")


if __name__ == '__main__':

    print(concat("un", "deux", "trois", test="/"))