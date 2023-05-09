//for every line in links.txt, create a new list element and append it to the list  
document.addEventListener("DOMContentLoaded", () => {
    const links = fetch("links.txt").then((response) => response.text());    
    console.log(links);
    const listItem = document.createElement("li");
    listItem.textContent = "test";
    const linksList = document.getElementById("links-list")
    if (linksList != null)
        linksList.appendChild(listItem);
    else
        console.log("linksList is null"	);
});