import Utils from "./utils.js";

const fetchForm = async (url, method, data) => {
  let headers = new Headers();

  headers.append("X-Requested-With", "XMLHttpRequest");
  headers.append("Content-Type", "application/json");
  headers.append("Accept", "application/json");

  return await fetch(url, {
    method: `${method}`,
    headers,
    body: data ? data : null,
    processData: false,
    contentType: false,
  });
};

const sendFormShortenUrl = async () => {
  const form = document.getElementById("form-shorten-url");

  form?.addEventListener("submit", async (e) => {
    e.preventDefault();

    let formData = new FormData(form);
    const data = JSON.stringify(Object.fromEntries(formData));
    const url = form.getAttribute("data-action-shorten");

    const method = form.getAttribute("method");
    const inputUrl = document.getElementById("long-url");

    if (!Utils.validateUrl(inputUrl.value)) {
      inputUrl.classList.add("is-invalid");
      inputUrl.focus();
      return;
    }

    let response = await fetchForm(url, method, data);
    let json = await response.json();

    const responseData = json.data.data
    const id_url = responseData.id_url;
    const newUrl = `/shortened/${id_url}`;

    if (json.success) {
      window.location.href = newUrl;
    }

  });
};

sendFormShortenUrl();