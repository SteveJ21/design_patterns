# Trivial example of the strategy design pattern.
from abc import ABCMeta, abstractmethod
from unittest import TestCase, main


class Order:
    """Container for order info."""
    def __init__(self, item_count):
        self._item_count = item_count

    @property
    def item_count(self):
        return self._item_count


class ShippingStrategy:
    """Abstract base class for strategy classes."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost based on an order."""
        pass


class FedExShippingStrategy(ShippingStrategy):
    """Calculates shipping costs for FedEx."""
    def calculate(self, order):
        cost_per_item = 3
        return cost_per_item * order.item_count


class UPSShippingStrategy(ShippingStrategy):
    """Calculates shipping costs for UPS."""
    def calculate(self, order):
        cost_per_item = 4
        return cost_per_item * order.item_count


class USPSShippingStrategy(ShippingStrategy):
    """Calculates shipping costs for USPS."""
    def calculate(self, order):
        cost_per_item = 5
        return cost_per_item * order.item_count


class ShippingCoster:
    def __init__(self, strategy):
        self._strategy = strategy

    def cost(self, order):
        return self._strategy.calculate(order)


class ShippingTest(TestCase):

    def setUp(self):
        self._order = Order(5)

    def test_fed_ex(self):
        fed_ex = ShippingCoster(FedExShippingStrategy())
        self.assertEqual(fed_ex.cost(self._order), 15)

    def test_ups(self):
        ups = ShippingCoster(UPSShippingStrategy())
        self.assertEqual(ups.cost(self._order), 20)

    def test_usps(self):
        usps = ShippingCoster(USPSShippingStrategy())
        self.assertEqual(usps.cost(self._order), 25)

if __name__ == '__main__':
    main()