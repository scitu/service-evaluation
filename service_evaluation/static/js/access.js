function getOS() {
  let userAgent = window.navigator.userAgent;
  let platform = window.navigator.platform;
  let macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'];
  let windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'];
  let iosPlatforms = ['iPhone', 'iPad', 'iPod'];
  let os = null;

  if (macosPlatforms.indexOf(platform) !== -1) {
    os = 'Mac OS';
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    os = 'iOS';
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = 'Windows';
  } else if (/Android/.test(userAgent)) {
    os = 'Android';
  } else if (!os && /Linux/.test(platform)) {
    os = 'Linux';
  }
  return os;
}

window.onload = () => {
  const API_URL = 'https://analytics.service.sci.tu.ac.th/api/count/'
  let payload = JSON.stringify({
    url: window.location.href,
    host: window.location.hostname,
    path: window.location.pathname,
    protocol: window.location.protocol,
    os: getOS(),
  });
  
  let xhr = new XMLHttpRequest();
  xhr.open("POST", API_URL);
  xhr.setRequestHeader("content-type", "application/json");
  xhr.setRequestHeader("cache-control", "no-cache");
  xhr.send(payload);
}
