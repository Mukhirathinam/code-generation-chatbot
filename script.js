function handleLogin() {
  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  // Simple validation
  if (email === "" || password === "") {
      alert("Please enter both email and password.");
      return;
  }

  // Simulated login success (in real scenarios, verify with backend)
  localStorage.setItem('loggedInEmail', email);
  localStorage.setItem('loggedInPassword', password);

  // Redirect to ui.html after login
  window.location.href = "ui.html";
}