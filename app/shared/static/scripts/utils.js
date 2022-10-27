class Utils {
  
  validateUrl = (url) => {
    var pattern = new RegExp(
      "^(https?:\\/\\/)?" + // protocol
        "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
        "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
        "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
        "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
        "(\\#[-a-z\\d_]*)?$",
      "i"
    ); // fragment locator
    if (!pattern.test(url)) return false;
    else return true;
  }

  fetchForm = async (url, method, data) => {
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
}

export default new Utils();
