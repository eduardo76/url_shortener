let btnCopy = document.getElementById("btn-copy");

btnCopy.addEventListener("click", async () => {
    let inputShortUrl = document.getElementById("input-short-url");

    await navigator.clipboard.writeText(inputShortUrl.value);

    document.querySelector(".url-copied span").style.display = "flex";

    setTimeout(() => {
        document.querySelector(".url-copied span").style.display = "none";
    }, 2000);
})

