
class CSVLoader(object):
    """
    This class is to be used to load any .csv file as any data object.
    Currently, .csv to pandas dataframe is the only supported functionality, but the
    class should be used to load .csvs as other data types as well.
    """

    @classmethod
    def load_as_dataframe(cls, file_path):
        """
        Load in csv and return data as a pandas dataframe

        :param file_path: a path to a .csv file containing all cross-account transactional data
        :type file_path: str

        :returns: a pandas.DataFrame
        """
        cls.validate_file_path(file_path)

        try:
            import pandas as pd
            return pd.read_csv(file_path)
        except IOError as e:
            raise IOError("Failed to load {}, with message: {}".format(file_path, e.message))

    @classmethod
    def validate_file_path(cls, file_path):
        """
        :param file_path: the file path to validate
        :type file_path: str

        :returns: raises if invalid or None
        """
        if not file_path:
            raise ValueError("A path to a .csv file must be supplied to perform a balance inquiry")

        if not file_path.endswith('.csv'):
            raise ValueError("File path supplied must point to a .csv file")
