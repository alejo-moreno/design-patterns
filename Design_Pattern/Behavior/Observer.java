public class Main {

    Carlos carlos = new Carlos();
    carlos.addObserver(new Parents());
    carlos.addObserver(new GirlFriend());

    carlos.wasFired();

}

public interface IObserver {

    public void notify();
}
// observer
public class Parents implements IObserver {

    public void notify() {
        System.out.println("We are gonna kill you!!!");
    }
}

// observer
public class GirlFriend implements IObserver {

    public void notify() {
        System.out.println("Oh honey!!!!");
    }
}

// subject 
public class Carlos {

    private ArrayList<IObserver> observers;

    public void addObserver(IObserver observer) {
        observers.add(observer);
    }

    public void wasFired() {
        for (IObserver observer : this.observers) {
            observer.notify();
        }
    }
}
