// First, start with a function expression: 

var a = function(){
    console.log("this is an expression");
}

var a = function expressionFunction(){
    console.log("This also works as an expression");
}

(function thirdExpressionFunction(){
    console.log("Immediately invoked function expression");
})();