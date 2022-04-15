//let endOfPageDiv = document.getElementById("eop")
let endOfPageDiv;
window.onload = (event) => {
    endOfPageDiv = document.getElementById("eop")
    console.log('page is fully loaded');
};
window.onscroll = (event) => {
    //console.log("scrolling")
    //console.log(window.scrollY)
    //console.log(document.documentElement.scrollHeight)
    //console.log(window.innerHeight)
    console.log(window.scrollY)
    console.log((window.innerHeight))
    console.log(document.documentElement.scrollHeight)
    console.log(Number(window.scrollY)+Number(window.innerHeight))
    if (Number(window.scrollY)+Number(window.innerHeight) == document.documentElement.scrollHeight){
        console.log("bottom")
        console.log(endOfPageDiv)
        console.log(endOfPageDiv.style.height);
        //endOfPageDiv.style.height += 10;
    }
}
