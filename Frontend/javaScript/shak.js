// const student = {
//     fullname :"shaklain",
//     age:23,
//     cgpa:8.9,
//     subject:'biology',
//     price:90000,
// }
// console.log(student["age"]);


// let a=10;
// let b =20
// // console.log("a:",++a);

// a+=6;
// document.writeln(a)
// a-=6;
// document.writeln(a)
// a*=6;
// document.writeln(a)
// a/=6;
// document.writeln(a)
// a%=6;
// document.writeln(a)












// let mode = "yellow";
// let color;
// if(mode=== "dark"){
//     color="black";
// } else if(mode==="green"){
//     color="green";
// } else if(mode==="cyan"){
//     color="cyan";
// } else{
//     color="no match to any color";
// }
// console.log(color);

// a=5;
// a+=2;
// console.log(a);



// let age=9;
// if(age>18){
//     console.log("you are adult");
// }

// else if(age<10){
//    console.log("you are child"); 
// }
// else{
//    console.log("zaid is child");  
// }

// let num= prompt("enter the number:");
// if(num%5===0){
//     console.log(num,"this is a multiple of 5");
// }
// else{
//    console.log( num,"this is not a multiple of 5"); 
// }

// let maks = prompt("enter the numebr")
// let grade;
// if(maks>80 && maks<100){
//    grade="a";
// }
//  else if(maks>70 && maks<89){
//    grade="b";
// }

// else if(maks>50 && maks<69){
//    grade="c";
// }

// else if(maks>33 && maks<49){
//    grade="d";
// }
// else (maks<33){
//    grade="fail";
// }

//     console.log(grade," is your result:");


// let sum=0;
// for(let i=1; i<=5;i++ ){
//    sum=sum+1;
   
//    console.log("shaklain")
// }

// let i=1;
// while(i<=10){
//    console.log(i);
//    i++;
// }



// for(let i=1;i<=1000;i++){
// document.write("shaklain")
// }


// for (let i=1;i<=50;i++){
//    if(i%2===0){
//       console.log(i);
//    }

// }

// for(let i=50; i>=1; i--){
//    if(i%2===0){
//       console.log(i);
//    }
// }
//  for(i=2; i<=50;i+=2){
//    console.log(i);
//  }

// let i=1;
// while(i<=50){
//    if(i%2===0){
//       console.log(i);
//    }
//    i++;
// }


// let i =1;
// let total=0;
// while(i<=100){
//    total+=i;
//    i++
//    console.log(total);
// }


// let num=5;
// let i =1;
// while(i<=10){
//    console.log(num*i);
//    i++
// }

// let num=4;
// for(let i=1; i<=10;i++){
//    console.log(num*i);
// }

// for(let i=1; i<=100; i++){
//    if(i%3===0){
//    console.log(i);
//    }
// }
  
// for(let i=1;i<=100;i++){
//    console.log(i * i);
// }

// let i =1;
// while(i<=100){
//    console.log(i*i);
//    i++
// }

// let i=2;
// while(i<=100){
//    if(i%2 ===0){
//   console.log(i)
//    }
 
//    i++;
// }

// let i=100;
// while(i>=1){
//    if(i%2===0){
//       console.log(i)
//    }
//    i--;
// }

// let total=0;
// let i=1;
// while(i<=100){
//    total+=i;
//    console.log(total);
//    i++;
// }

// let num=2;
// let i=1;
// while(i<=100){
//    console.log(num*i);
//    i++;
// }

// let i=1;
// while(i<=10){
//    console.log(i*i);
//    i++;
// }


// let n=5;
// for(let i=1; i<=n; i++){
//     let row="";
//     for(let j=1; j<=i; j++){
//       row+="*"
//     }
//     console.log(row)
// }



// let n=5;
// for(let i=0; i<=n; i--){
  
//   for( let j=1;j<=i; j++){
//     print(i)

//   }
// }

// let obj={
//   item:"pen",
//   price:10,
// };
// let output =`the cost of ${obj.item} is ${obj.price} rupees`;
// console.log(output);


// let shak="shaklain is a good boy";
// console.log(shak.toUpperCase());

// let shak="SHAKLAIN ASHRAF IS GOOD BOY";
// console.log(shak.toLowerCase());

// let shak="       SHAKLAIN ASHRAF IS GOOD            BOY       ";
// console.log(shak.trim());


// let fullname= prompt("enter your full name withot spaces");
// let username = "@" + firstname + secondname.length;
// console.log(username)       

// let str = "rehan";
// str = str.replace("r", "S");
// console.log(shak);


function changetext(){
    document.getElementById("demo").innerHTML ="welcome to java script class"
}

function changecolor(){
    document.getElementById("demo").style.color="green"
}