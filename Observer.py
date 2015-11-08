class AbstractObserver(object):
    def notify(self):
        raise NotImplementedError("Should have implemented this")
