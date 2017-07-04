# Trivial example of the observer design pattern.
from abc import ABCMeta, abstractmethod


class AbsObserver(object):
    """Abstract base class for observer."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class AbsSubject(object):
    """Abstract base class for subject."""
    __metaclass__ = ABCMeta
    _observers = set()

    def attach(self, observer):
        assert isinstance(observer, AbsObserver)
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self):
        for observer in self._observers:
            observer.update()


class Cart(AbsSubject):
    """Cart to observe."""
    _items = -1

    @property
    def items(self):
        return self._items

    def set_item_count(self, items):
        self._items = items
        self.notify()


class CartObserver(AbsObserver):
    """Base class for cart observer classes."""
    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)


class PrimaryCart(CartObserver):
    """Primary cart observer."""
    def update(self):
        print('Primary cart, items', self._kpis.items)


class SecondaryCart(CartObserver):
    """Secondary cart observer."""
    def update(self):
        print('Secondary cart, items', self._kpis.items)


cart = Cart()

# Register cart with observers
primary_cart = PrimaryCart(cart)
secondary_cart = SecondaryCart(cart)

# Each time items are updated the observers are notified and display
cart.set_item_count(1)
cart.set_item_count(3)

# Detach an observer and update will only be reflected by remaining observers
cart.detach(primary_cart)
cart.set_item_count(5)

# Detach last observer and update has no observers for displaying
cart.detach(secondary_cart)
cart.set_item_count(7)