from container.basket import Basket
from entity.bread import Bread
from entity.milk import Milk
from entity.orange import Orange


def main():
    br = Bread()
    m = Milk(1, 4.2, 5.5)
    o = Orange()
    basket = Basket()
    basket.add(br)
    basket.add(m)
    basket.add(o)
    print(f"Size = {basket.size}")
    # print(br)
    # print(m)
    # print(o)

    print(basket)


if __name__ == '__main__':
    main()
