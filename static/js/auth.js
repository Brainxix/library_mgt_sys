document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.querySelector(".toggle-password");
    const password = document.querySelector(".password-wrapper input");

    if (toggle && password) {
        toggle.addEventListener("click", () => {
            const icon = toggle.querySelector("i");

            if (password.type === "password") {
                password.type = "text";
                icon.classList.remove("fa-eye");
                icon.classList.add("fa-eye-slash");
            } else {
                password.type = "password";
                icon.classList.remove("fa-eye-slash");
                icon.classList.add("fa-eye");
            }
        });
    }
});