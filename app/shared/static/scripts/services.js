import Utils from "./utils.js";

const fetchForm = async (url, method, data) => {
  let headers = new Headers();

  headers.append("X-Requested-With", "XMLHttpRequest");
  headers.append("Content-Type", "application/json");
  headers.append("Accept", "application/json");

  return await fetch(url, {
    method: `${method}`,
    headers,
    body: data,
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
    const urlShortened = form.getAttribute("data-action-shortened");

    console.log("urlShortened ====================>", urlShortened);

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

    formData = new FormData();

    formData.append("id_url", responseData.id_url);
    formData.append("long_url", responseData.long_url);
    formData.append("short_url", responseData.short_url);
    formData.append("status_url", responseData.status_url);
    formData.append("total_access", responseData.total_access);
    formData.append("updated_at", responseData.updated_at);

    if (json.success) {
      response = await fetchForm(urlShortened, method, formData);
      const json = await response.json();
      
      console.log("response ===============:", response);
      console.log("json ==========", json);

    }

    // console.log("response ===============:", response);
    // console.log("json ==========", json);
    
  });
};

sendFormShortenUrl();