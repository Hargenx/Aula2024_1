package aula01;

class Animal {
    public void fazerSom() {
        System.out.println("Som do Animal");
    }
}

class Cachorro extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("Latindo... Woof! Woof!");
    }
}

class Gato extends Animal {
    @Override
    public void fazerSom() {
        System.out.println("Miando... Meow!");
    }
}

public class sobrecarga {
    public static void main(String[] args) {
        Animal[] animais = new Animal[2];

        animais[0] = new Cachorro();
        animais[1] = new Gato();

        for (Animal animal : animais) {
            animal.fazerSom();
        }
    }
}
