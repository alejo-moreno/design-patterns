public class Main {

    public static void main(String[] args) {
        ICoffee coffeeWithMilk = new CoffeeWithMilk(new Coffee());
        System.out.println(coffeeWithMilk->getCost());
    }
}

public interface ICoffee {

    public double getCost();
}

public class Coffee implements ICoffee {

    public double getCost() {
        return 1;
    }
}

public class CoffeeWithMilk implements ICoffee {

    private ICoffee coffee;

    public CoffeeWithMilk(ICoffee coffee) {
        this.coffee = coffee;
    }

    public double getCost() {
        return this.coffee.getCost() + 0.25;
    }
}