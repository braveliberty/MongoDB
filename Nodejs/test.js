const nums =[ 1,2,3];
const foo = (nums) => nums;
console.log(foo(nums));



function f(x, y, z) {
  // ...
}
var args = [0, 1, 2];
f.apply(null, args);


// 箭头函数的this指向定义时所在对象

var a = 3;
var obj = {
  a: 10,
  b: () => {
    var a = 1;
    console.log(this.a); //undefined
    console.log('2',this); //window
  },
  c: function() {
    console.log(this.a); //10
    console.log(this); //obj{...}
  }
}
obj.b(); 
obj.c();
