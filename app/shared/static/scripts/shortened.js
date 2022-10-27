let btnCopy = document.getElementById("btn-copy");

btnCopy.addEventListener("click", async () => {
    let inputShortUrl = document.getElementById("input-short-url");

    await navigator.clipboard.writeText(inputShortUrl.value);

    btnCopy.innerHTML = "Copied!";
    document.querySelector(".url-copied span").style.display = "flex";
})

