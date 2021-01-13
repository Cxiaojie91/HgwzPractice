class Bicycle:
    def fun(self,km):
        print((f"健康环保，骑行里程数为:{km}"))

class EBicycle:
    def __init__(self,battery_level):
        # 初始化电量
        self.battery_level = battery_level

    def fill_charge(self,vol):
        #充电
        self.battery_level = self.battery_level + vol

    def run(self, km):
        # 用电骑，用脚蹬
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"已经用电行驶了：{self.battery_level * 10}km")
            # # 第一种调用
            # bicycle = Bicycle()
            # bicycle.run(miles)
            # 第二种调用
            super().run()
        else:
            print(f"已使用点行驶了：{km} km")

# if name是上一节课的内容，需要复习
# if __name__ = '__main__' :
eb = EBicycle(10)
eb.run(101)