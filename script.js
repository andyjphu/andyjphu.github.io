let oHeight = 0
window.onload = (event) => { 
    //console.log('page is fully loaded');
};
window.onscroll = (event) => {
    //console.log("scrolling")
    //console.log(window.scrollY)
    //console.log(document.documentElement.scrollHeight)
    //console.log(window.innerHeight)
   // console.log(window.scrollY)
    //console.log((window.innerHeight))
    //console.log(document.documentElement.scrollHeight)
    //console.log(Number(window.scrollY)+Number(window.innerHeight))
    if (Number(window.scrollY)+Number(window.innerHeight) >= document.documentElement.scrollHeight-420){
        oHeight+=420
        //console.log("bottom");
        //console.log(eopclass);
        document.getElementById("eop").style.height=String(oHeight)+"px"
    }
}
