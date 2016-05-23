var MySingleton = (function() {
    var instance;

    function init() {

        var privateNumber = Math.round(Math.random() * 1000);

        function privateMethod() {
            console.log("I am a private Method");
        }

        return {
            publicMethod: function() {
                console.log("Entré a metodo público");
                privateMethod();
                console.log("Salí de metodo público");
            },
            getRandomNumber: function() {
                return privateNumber;
            }
        }
    }

    return {
        getInstance: function() {
            if (!instance) {
                instance = init();
            }
            return instance;
        }
    }
})();

var testOne = MySingleton.getInstance();
testOne.publicMethod();

var testTwo = MySingleton.getInstance()
testTwo.publicMethod()

console.log(testOne.getRandomNumber() === testTwo.getRandomNumber())