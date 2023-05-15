//for every line in links.txt, create a new list element and append it to the list  
document.addEventListener("DOMContentLoaded", () => {
    fetch("todo/links.txt")
      .then((response) => response.text())
      .then((text) => {
        const links = text.split("\n");
        const linksList = document.getElementById("links-list");
        if (linksList) {
          links.forEach((link) => {
            const listItem = document.createElement("li");
            listItem.textContent = link;
            linksList.appendChild(listItem);
          });
        } else {
          console.log("linksList is null");
        }
      })
      .catch((error) => console.log("Error fetching links:", error));


      
  });