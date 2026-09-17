<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เกมทายคำศัพท์ภาษาไทย</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<div class="game-box">
    <h1>🎮 เกมทายคำศัพท์ภาษาไทย</h1>

    <p id="questionNumber">ข้อที่ 1 / 5</p>
    <p id="question"></p>

    <input type="text" id="answer" placeholder="พิมพ์คำตอบที่นี่">

    <button onclick="checkAnswer()">ส่งคำตอบ</button>

    <p id="score">คะแนน: 0</p>
    <p id="timer">เวลา: 30 วินาที</p>

    <div id="result"></div>

    <button id="restart" onclick="restartGame()" style="display:none;">
        🔄 เล่นอีกครั้ง
    </button>
</div>

<script src="script.js"></script>

</body>
</html>
body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #74ebd5, #ACB6E5);
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.game-box {
    background: white;
    width: 90%;
    max-width: 500px;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

h1 {
    color: #333;
}

#question {
    font-size: 22px;
    font-weight: bold;
    margin: 25px 0;
}

input {
    width: 80%;
    padding: 12px;
    font-size: 18px;
    border: 2px solid #ddd;
    border-radius: 10px;
    margin-bottom: 15px;
}

button {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 17px;
    border-radius: 10px;
    cursor: pointer;
    margin: 5px;
}

button:hover {
    opacity: 0.85;
}

#score {
    font-size: 18px;
    color: #333;
}

#timer {
    color: #e67e22;
    font-weight: bold;
}

#result {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}
const questions = [
    {
        question: "คำว่า 'กตัญญู' หมายถึงอะไร?",
        answer: "รู้คุณ"
    },
    {
        question: "คำว่า 'สามัคคี' หมายถึงอะไร?",
        answer: "ความพร้อมเพรียง"
    },
    {
        question: "คำว่า 'ขยัน' หมายถึงอะไร?",
        answer: "ตั้งใจทำงาน"
    },
    {
        question: "คำว่า 'สุจริต' หมายถึงอะไร?",
        answer: "ซื่อสัตย์"
    },
    {
        question: "คำว่า 'ประหยัด' หมายถึงอะไร?",
        answer: "ใช้จ่ายอย่างรอบคอบ"
    }
];

let currentQuestion = 0;
let score = 0;
let timeLeft = 30;
let timer;

function startGame() {
    currentQuestion = 0;
    score = 0;
    timeLeft = 30;

    document.getElementById("score").innerText = "คะแนน: 0";
    document.getElementById("result").innerText = "";

    showQuestion();

    clearInterval(timer);
    timer = setInterval(updateTimer, 1000);
}

function showQuestion() {

    if (currentQuestion >= questions.length) {
        endGame();
        return;
    }

    document.getElementById("questionNumber").innerText =
        `ข้อที่ ${currentQuestion + 1} / ${questions.length}`;

    document.getElementById("question").innerText =
        questions[currentQuestion].question;

    document.getElementById("answer").value = "";
    document.getElementById("answer").focus();
}

function checkAnswer() {

    const userAnswer =
        document.getElementById("answer").value.trim();

    if (userAnswer === "") {
        alert("กรุณาพิมพ์คำตอบก่อนครับ");
        return;
    }

    if (userAnswer === questions[currentQuestion].answer) {
        score++;
    }

    document.getElementById("score").innerText =
        `คะแนน: ${score}`;

    currentQuestion++;

    showQuestion();
}

function updateTimer() {

    timeLeft--;

    document.getElementById("timer").innerText =
        `เวลา: ${timeLeft} วินาที`;

    if (timeLeft <= 0) {
        endGame();
    }
}

function endGame() {

    clearInterval(timer);

    document.getElementById("question").innerText =
        "🎉 จบเกมแล้ว!";

    document.getElementById("questionNumber").innerText = "";

    document.getElementById("answer").style.display = "none";

    document.querySelector("button[onclick='checkAnswer()']")
        .style.display = "none";

    let level = "";

    if (score === 5) {
        level = "🌟 ดีมาก";
    } else if (score >= 2) {
        level = "😊 ดี";
    } else {
        level = "📚 ปรับปรุง";
    }

    document.getElementById("result").innerHTML =
        `คุณได้ <b>${score} / 5 คะแนน</b><br>${level}`;

    document.getElementById("restart").style.display = "inline-block";
}

function restartGame() {

    document.getElementById("answer").style.display = "inline-block";

    document.querySelector("button[onclick='checkAnswer()']")
        .style.display = "inline-block";

    document.getElementById("restart").style.display = "none";

    timeLeft = 30;

    document.getElementById("timer").innerText =
        "เวลา: 30 วินาที";

    startGame();
}

startGame();
