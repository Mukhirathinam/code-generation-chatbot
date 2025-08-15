// function handleLogin() {
//     const email = document.getElementById("email").value;
//     const password = document.getElementById("password").value;

//     if (!email || !password) {
//         alert("⚠ Please enter both email and password!");
//         return;
//     }

//     // Retrieve user data from localStorage
//     const storedUser = JSON.parse(localStorage.getItem("user"));

//     if (storedUser && email === storedUser.email && password === storedUser.password) {
//         alert("Login successful!");
//         localStorage.setItem("loggedInUser", email); // Store session
//         window.location.href = "dashboard.html"; // Redirect to dashboard
//     } else {
//         alert("Invalid email or password. Please try again.");
//     }
// }

// function handleSignup() {
//     let fullname = document.getElementById("fullname").value;
//     let email = document.getElementById("email").value;
//     let password = document.getElementById("password").value;
//     let confirmPassword = document.getElementById("confirm-password").value;

//     if (password !== confirmPassword) {
//         alert("Passwords do not match!");
//         return;
//     }

//     // Save user details in localStorage
//     const user = { fullname, email, password };
//     localStorage.setItem("user", JSON.stringify(user));

//     alert("Signup successful! Redirecting to login...");
//     window.location.href = "index.html"; // Redirect to login page
// }

// /* Google Login */
// function handleCredentialResponse(response) {
//     console.log("Google ID Token:", response.credential);
//     alert("Google Login Successful!");
//     localStorage.setItem("loggedInUser", "GoogleUser");
//     window.location.href = "dashboard.html"; // Redirect to dashboard
// }

// window.onload = function () {
//     google.accounts.id.initialize({
//         client_id: "YOUR_GOOGLE_CLIENT_ID",
//         callback: handleCredentialResponse
//     });

//     google.accounts.id.renderButton(
//         document.getElementById("google-login-btn"),
//         { theme: "outline", size: "large" }
//     );
// };
function handleSignup() {
    const fullname = document.getElementById("fullname").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document.getElementById("confirm-password").value.trim();

    // Simple validation
    if (email === "" || password === "" || confirmPassword === "" || fullname === "") {
        alert("Please fill in all fields.");
        return;
    }
    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }

    // Simulated signup success (in real scenarios, send to backend)
    localStorage.setItem('loggedInEmail', email);
    localStorage.setItem('loggedInPassword', password);

    // Redirect to ui.html after signup
    window.location.href = "ui.html";
}