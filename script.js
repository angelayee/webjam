document.getElementById('searchButton').addEventListener('click', function() {
    var searchQuery = document.getElementById('searchInput').value;
    // Here you can add code to handle the search
    alert("Search for: " + searchQuery);
});
document.getElementById('searchButton').addEventListener('click', function() {
    var searchQuery = document.getElementById('searchInput').value;
    // Here you can add code to handle the search
    alert("Search for: " + searchQuery);
});

function sortProducts() {
    var container = document.getElementById("products");
    var products = container.getElementsByClassName("product");
    var sortOption = document.getElementById("sort").value;

    var sortedProducts = Array.from(products).sort(function (a, b) {
        var nameA = a.querySelector("h3").innerText;
        var nameB = b.querySelector("h3").innerText;

        if (sortOption === "asc") {
            return nameA.localeCompare(nameB);
        } else {
            return nameB.localeCompare(nameA);
        }
    });

    // Clear existing content
    container.innerHTML = "";

    // Append sorted products
    sortedProducts.forEach(function (product) {
        container.appendChild(product);
    });
}
