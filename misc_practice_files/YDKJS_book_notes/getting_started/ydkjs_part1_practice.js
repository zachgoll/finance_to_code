//var bankBalance = prompt("Enter your bank account balance");
//const taxRate = 0.4;
//const phonePrice = 99.99;
//var amount = 0;
//
//const spendingThreshold = prompt("What is the maximum you'd like to spend on phones today?"); 
//
//if(spendingThreshold>bankBalance){
//    alert("You can't spend that much today.  The amount entered is less than the bank balance!");
//}
//
//var numberPhones = Math.floor(spendingThreshold/phonePrice);
//var totalBeforeTax = numberPhones * phonePrice;
//
//var totalAfterTax = totalBeforeTax + totalBeforeTax*taxRate;
//
//function formatTotal(){
//    console.log("$" + totalAfterTax.toFixed(2)) ;
//}
//
//formatTotal();


//// Hoisting 
//
//foo();
//
//function foo(){
//    var a = 2;
//}

// The foo() function is called before it is declared, but it works because the function is "hoisted" to the top.

//Scope 

//function master(){
//    var a = 2;
//    function child(){ 
//        var b = 1;
//        console.log(a,b);
//    }
//    console.log(a); //You cannot console.log(b) from master(), but you can console.log(a,b) from child().
//}
//
//master();

// all errors calling variables out of scope are "referenceErrors"

// Javascript Variable Types 

//var a = 2; //standard declaration of variable.  Can be changed later in the function 
//const a = 2; //once defined, cannot be changed later 
//let a =2; //defines a specific scope for the variable
//

//Normal vs. Immediately Invoked Functions 

//(function II() {
//    console.log("This is an immediately invoked function thanks to the outer parentheses");
//})();
//
//function normal(){
//    console.log("You must call this function later in your code for it to work");
//}

//____________________________________________________

//Closure

//function makeAdder(x) {
//    // parameter `x` is an inner variable
//
//    // inner function `add()` uses `x`, so
//    // it has a "closure" over it
//    function add(y) {
//        return y + x;
//    };
//
//    return add;
//}
//
//var plusOne = makeAdder(1);
//
//plusOne(4);


//____________________________________________________

