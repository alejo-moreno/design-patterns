//Old Implementation
function AdapteeShipping() {
    this.request = function(origen, destino, peso) {
        this.origen = origen;
        this.destino = destino;
        this.peso = peso;
        this.total = this.peso * 100;
        return this.total;
    }
}

//New Implementation
function TargetShipping() {
    this.login = function(username, password) {
        if (username && password)
            return true;
        else
            return false;
    }
    this.setOrigen = function setOrigen(origen) {
        this.origen = origen;
    }
    this.setDestino = function setDestino(destino) {
        this.destino = destino;
    }
    this.calculate = function calculate(peso) {
        this.peso = peso;
        this.total = this.peso * 100;
        return this.total;
    }
}

//Adapter To New Implementation
function ShippingAdapter(username, password) {
    var targetShipping = new TargetShipping();
    targetShipping.login(username, password);

    return {
        request: function request(origen, destino, peso) {
            targetShipping.setOrigen(origen);
            targetShipping.setDestino(destino);
            return targetShipping.calculate(peso)
        }
    }
}

function Client() {
    this.run = function() {
        var oldInterface = new AdapteeShipping();
        var oldCost = oldInterface.request("PCOrigen", "PCDestino", 123.45);
        console.log(oldCost);

        var adapter = new ShippingAdapter("myUser", "myPass");
        var newCost = adapter.request("PCOrigen", "PCDestino", 123.45);
        console.log(newCost);
    }
}

var cliente = new Client();
cliente.run();
