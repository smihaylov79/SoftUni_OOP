from project.cls_id_mixin import ClsIdMixin


class Equipment(ClsIdMixin):
    def __init__(self, name):
        self.name = name
        self.id=self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
