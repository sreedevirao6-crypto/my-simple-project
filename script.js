async function showMessage() {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/career");
        const data = await response.json();

        alert(
            "Recommended Career: " + data.career +
            "\nReadiness Score: " + data.readiness_score + "%" +
            "\nSkills: " + data.skills.join(", ")
        );

    } catch (error) {
        alert("Backend is not running!");
        console.error(error);
    }
}