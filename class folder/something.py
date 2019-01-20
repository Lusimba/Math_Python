function plus(n1,n2) {
  return n1+n2;
}

function isEven(n3) {
  if (n3%2==0) {
    return true;
  }
  return false;
}

function reverseIt(string) {
  var rstring="";
  for (var i = string.length-1; i>=0; i--) {
  	rstring=rstring+string.charAt(i);
  };
  return rstring;
}

function isPalindrome(pstring) {
  if (pstring==reverseIt(pstring)) {
    return true;
  }
    return false;
}

function printFib(n) {
  var a=0;
  var b=1;
  console.log(a);
  console.log(b);
  for (var i = 1; i <=n ; i++) {
  	var c=a+b;
  	console.log (c);
  	a=b;
  	b=c;
  };
  return;
}

function minus(n1,n2) {
  return n1-n2;
}

console.log(plus(6,9));
console.log(plus(8,9));
console.log(plus(8,9));
console.log(plus(8,9));

console.log(isEven(6));
console.log(isEven(7));
console.log(isEven(12));
console.log(isEven(345));

console.log(reverseIt("mamma"));
console.log(reverseIt("papa"));

console.log(isPalindrome("dad"));
console.log(isPalindrome("key"));

printFib(100);
printFib(65);

console.log(minus(13,14));
console.log(minus(13,15));