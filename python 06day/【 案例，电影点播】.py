class TVshow:
    list_film = ["战狼","红海行动","熊出没","变形记"]
    _show = ''
    def __init__(self,value):
        self.setShow(value)
    @property
    def show(self):
        return self._show

    def setShow(self,value):
        if value in TVshow.list_film:
            self._show = '点播《' + value + '》,请稍后...'
        else:
            self._show = '电影不存在'

tv = TVshow('战狼')
print(tv.show)


