// var polje = document.getElementsByClassName
// for (var svako of polje){
//     if (svako.classList.contains('isSub')){
//         svako.addEventListener('click',function(){
//             svako.classList.add('hit')
//         })
//     }
//     else{
//         svako.classList.addEventListener('click',function(){
//             svako.classList.add('miss')
//         })
//     }
// }

var isSub =document.querySelectorAll(".isSub");
var isNot = document.querySelectorAll('.isNotSub');
isSub.forEach(polje=>{
    polje.addEventListener('click',function(){
        polje.classList.add('hit');
    })
});
isNot.forEach(polje=>{
    polje.addEventListener('click',function(){
        polje.classList.add('miss')
    })
});

