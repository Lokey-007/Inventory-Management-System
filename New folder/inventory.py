class Inventory:
    def __init__(self,gid,gname,qty,price,Cost):
        self.good_sid =gid
        self.good_sname = gname
        self.goods_qty = qty
        self.goods_price = price
        self.Cost =Cost
    
    def __str__(self):
        return str(self.good_sid) + "," + self.good_sname + "," + str(self.goods_qty) + "," + str(self.goods_price)+ ","+ str(self.Cost) + "\n"