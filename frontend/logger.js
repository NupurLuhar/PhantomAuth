let behaviorData = [];

document.addEventListener("keydown", (e) => {
  const time = new Date().getTime();
  behaviorData.push({
    key: e.key,
    type: "keydown",
    timestamp: time,
  });
});

document.addEventListener("keyup", (e) => {
  const time = new Date().getTime();
  behaviorData.push({
    key: e.key,
    type: "keyup",
    timestamp: time,
  });
});

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const response = await fetch("http://127.0.0.1:8000/authenticate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password, behaviorData }),
  });

  const result = await response.json();
  alert(result.message);
});
