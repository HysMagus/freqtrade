from abc import ABC, abstractmethod
from pandas import DataFrame


class IStrategy(ABC):
    @property
    def name(self) -> str:
        """
        Name of the strategy.
        :return: str representation of the class name
        """
        return self.__class__.__name__

    """
    Attributes you can use:
        minimal_roi -> Dict: Minimal ROI designed for the strategy
        stoploss -> float: optimal stoploss designed for the strategy
        ticker_interval -> int: value of the ticker interval to use for the strategy
    """

    @abstractmethod
    def populate_indicators(self, dataframe: DataFrame) -> DataFrame:
        """
        Populate indicators that will be used in the Buy and Sell strategy
        :param dataframe: Raw data from the exchange and parsed by parse_ticker_dataframe()
        :return: a Dataframe with all mandatory indicators for the strategies
        """

    @abstractmethod
    def populate_buy_trend(self, dataframe: DataFrame) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        :return:
        """

    @abstractmethod
    def populate_sell_trend(self, dataframe: DataFrame) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :return: DataFrame with buy column
        """
