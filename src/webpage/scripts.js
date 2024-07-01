let producturl;

// recupera valores inputs
function addProduct() {
    const productUrl = document.getElementById('product-url-input').querySelector('input').value;
    if (productUrl.startsWith("https://www.mercadolivre.com.br")) {
        alert("Produto Adicionado!");
        // Aqui você pode fazer a requisição POST para adicionar o produto
    } else {
        alert("URL inválida");
    }
}
