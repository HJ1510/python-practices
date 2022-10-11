from human import Human


# class Leg:
#     def __init__(self,side) -> None:
#         print("다리")
#         self.side=side
#         pass


class Leg(Human):
    def __init__(self,side,name) -> None:
        self.side=side
        super().setName=name
        pass