function multiplyByTwo(a,b,c){
    var i , arr =[]
    for(i =0; i<3,i++;){
        arr[i] = arguments[i] * 2;
    }
    return arr;
}

function addOne(a){
    return a+1;
}

var x = multiplyByTwo(1,2,3)
console.log(x)