window.onload = function(){
    var isSub = document.querySelectorAll(".isSub");
    var isNot = document.querySelectorAll(".isNotSub");
    isSub.forEach(polje=>{polje.addEventListener("click",function(){polje.classList.add("hit");})});
    isNot.forEach(polje=>{polje.addEventListener("click",function(){polje.classList.add("miss")})});
}
