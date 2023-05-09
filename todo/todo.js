
//for every line in links.txt, create a new list element and append it to the list  
document.addEventListener("DOMContentLoaded", () => {


    const listItem = document.createElement("li");
    listItem.textContent = "test";

    document.getElementById("links-list").appendChild(listItem);
});