
<script type="module">

</script>
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
import { getDatabase, ref, set, get, child } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";


// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBLO09Ptx792E0Jjcc19tS3xZt-1q_ED7M",
    authDomain: "autostart-3f221.firebaseapp.com",
    projectId: "autostart-3f221",
    storageBucket: "autostart-3f221.firebasestorage.app",
    messagingSenderId: "667197415265",
    appId: "1:667197415265:web:90e7454736d74b47386f20"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// get ref to database
const db = getDatabase(app)

document.getElementById("submit").addEventListener("click", function (e) {

    set(ref(db, 'user/' + document.getElementById("name").value), {
        nameInput : document.querySelector('.q1 .styled-input'),
        phoneInput :document.querySelector('.q2 .styled-input'),
        emailInput : document.querySelector('.q3 .styled-input'),
        profileInput : document.querySelector('.q4 .styled-input'),
        companyInput : document.querySelector('.q5 .styled-input'),
        designationInput : document.querySelector('.q6 .styled-input'),
        introInput : document.querySelector('.q7 .styled-input')

    })
})