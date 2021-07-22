from typing import NoReturn, Optional


class Parser(object):
    """
    Yaml parser.

    Usage:
        p = Parser().open('filepath')
        p.filepath = 'your/new/file/path.yaml'
        p.data = {'new': 'data'}

    Args:
        filepath (str): path/of/your/file.yaml
        data (dict): data to put in the yaml file

    Class methods:
        open(file_): Generate a Parser object from the given yaml file
                     or create a new one if the yaml file does not exists

    Methods:
        new(data, filepath): Create a new yaml
        write(): Write the yaml file with the stored filepath and data

    """

    def __init__(self, filepath=None, data=None):
        # type: (Optional[str], Optional[dict]) -> NoReturn
        self.__file = filepath or str()
        self.__data = data or dict()

    def new(self, data=None, filepath=None):
        # type: (dict, str) -> Parser
        """
        Create a new yaml file

        Args:
            data (dict):
            filepath (str): filepath of the yaml file

        Returns:
            Parser:

        """
        import yaml
        import os
        from CommonTools.os_ import make_dirs

        self.filepath = filepath or self.filepath
        self.data = data or self.data

        path, _ = os.path.split(self.filepath)
        make_dirs(path)

        content = yaml.safe_dump(self.data)

        with open(self.filepath, "w") as file_:
            file_.write(content)

        return self

    def write(self):
        # type: () -> NoReturn
        """
        Write the yaml file

        Raises:
            RuntimeError: if the file does not exist

        """
        import yaml
        import os

        if os.path.isfile(self.filepath):
            with open(self.filepath, "w") as file_:
                yaml.dump(self.data, file_)
        else:
            raise RuntimeError("Use 'Parser.new()' to create a new yaml file.")

    @property
    def filepath(self):
        # type: () -> str
        return self.__file

    @filepath.setter
    def filepath(self, value):
        # type: (str) -> NoReturn
        self.__file = value

    @property
    def data(self):
        # type: () -> dict
        return self.__data

    @data.setter
    def data(self, values):
        # type: (dict) -> NoReturn
        self.__data = values

    @classmethod
    def open(cls, file_):
        # type: (str) -> Parser
        import yaml

        try:
            data = yaml.load(open(file_, "r"), Loader=yaml.Loader)

            return cls(file_, data)
        except IOError:
            data = dict()
            return cls(file_, data).new()
