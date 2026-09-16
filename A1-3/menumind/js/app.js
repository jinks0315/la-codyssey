const recommendButton = document.getElementById("recommendButton");
const ingredientsInput = document.getElementById("ingredients");
const difficultySelect = document.getElementById("difficulty");
const timeSelect = document.getElementById("time");
const result = document.getElementById("result");


recommendButton.addEventListener("click", async function () {

    const ingredients = ingredientsInput.value.trim();
    const difficulty = difficultySelect.value;
    const cookingTime = timeSelect.value;


    // 1. 빈 입력 확인
    if (ingredients === "") {

        result.innerHTML = `
            <h3>입력 확인</h3>
            <p>가지고 있는 재료를 입력해주세요.</p>
        `;

        return;
    }


    // 2. 로딩 표시
    result.innerHTML = `
        <h3>AI 요리 추천</h3>
        <p>✨ AI가 요리를 찾고 있습니다...</p>
    `;

    recommendButton.disabled = true;
    recommendButton.textContent = "추천 중...";


    try {

        // 3. Python API 호출
        const response = await fetch("/api/recommend", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                ingredients: ingredients,
                difficulty: difficulty,
                time: cookingTime
            })

        });


        // 4. Python이 보낸 JSON 받기
        const data = await response.json();


        // 5. 서버 오류 확인
        if (!response.ok) {
            throw new Error(data.message || "서버 오류");
        }


        // 6. AI 결과 화면에 출력
        result.innerHTML = `
            <h3>🍽️ AI 추천 결과</h3>
            <p class="ai-result">${escapeHtml(data.result)}</p>
        `;


    } catch (error) {

        console.error(error);

        result.innerHTML = `
            <h3>오류</h3>
            <p>
                요리를 추천하지 못했습니다.<br>
                잠시 후 다시 시도해주세요.
            </p>
        `;

    } finally {

        // 7. 버튼 원래대로
        recommendButton.disabled = false;
        recommendButton.textContent = "AI 추천받기";

    }

});


function escapeHtml(text) {

    const div = document.createElement("div");
    div.textContent = text;

    return div.innerHTML.replace(/\n/g, "<br>");
}