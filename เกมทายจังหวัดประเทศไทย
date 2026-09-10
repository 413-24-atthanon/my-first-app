<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เกมทายจังหวัดประเทศไทย</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #e3f2fd;
            text-align: center;
            padding: 30px;
        }

        .game-box {
            background: white;
            max-width: 600px;
            margin: auto;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 5px 15px #999;
        }

        h1 {
            color: #1565c0;
        }

        button {
            display: block;
            width: 80%;
            margin: 12px auto;
            padding: 12px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            background: #42a5f5;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background: #1565c0;
        }

        #question {
            font-size: 22px;
            margin: 25px 0;
        }

        #score {
            color: #2e7d32;
            font-weight: bold;
        }

        #result {
            font-size: 22px;
            font-weight: bold;
            margin: 20px;
        }
    </style>
</head>

<body>

<div class="game-box">

    <h1>🇹🇭 เกมทายจังหวัดประเทศไทย 🇹🇭</h1>

    <!-- หน้าเริ่มเกม -->
    <div id="startScreen">
        <p>ทดสอบความรู้เกี่ยวกับจังหวัดต่าง ๆ ของประเทศไทย</p>
        <p>มีทั้งหมด 5 ข้อ</p>

        <button onclick="startGame()">🎮 เริ่มเกม</button>
    </div>

    <!-- หน้าเล่นเกม -->
    <div id="gameScreen" style="display:none;">

        <p id="questionNumber"></p>

        <div id="question"></div>

        <div id="answers"></div>

        <p id="score">คะแนน: 0</p>

    </div>

    <!-- หน้าผลคะแนน -->
    <div id="resultScreen" style="display:none;">

        <h2>🎉 จบเกม 🎉</h2>

        <p id="finalScore"></p>

        <p id="result"></p>

        <button onclick="startGame()">🔄 เล่นอีกครั้ง</button>

    </div>

</div>


<script>

    // ข้อมูลคำถาม
    const questions = [

        {
            question: "จังหวัดใดอยู่ทางภาคเหนือและมีดอยอินทนนท์?",
            answers: ["เชียงใหม่", "ขอนแก่น", "ชลบุรี", "ภูเก็ต"],
            correct: "เชียงใหม่"
        },

        {
            question: "จังหวัดใดมีสถานที่ท่องเที่ยวชื่อ เกาะพีพี?",
            answers: ["เชียงราย", "ภูเก็ต", "นครปฐม", "อุดรธานี"],
            correct: "ภูเก็ต"
        },

        {
            question: "จังหวัดใดมีอนุสาวรีย์ย่าโม?",
            answers: ["นครราชสีมา", "สุราษฎร์ธานี", "ลำปาง", "ระยอง"],
            correct: "นครราชสีมา"
        },

        {
            question: "จังหวัดใดเป็นที่ตั้งของสะพานข้ามแม่น้ำแคว?",
            answers: ["กาญจนบุรี", "เพชรบุรี", "ตราด", "น่าน"],
            correct: "กาญจนบุรี"
        },

        {
            question: "จังหวัดใดมีวัดร่องขุ่น?",
            answers: ["เชียงใหม่", "เชียงราย", "พะเยา", "แพร่"],
            correct: "เชียงราย"
        }

    ];


    // ตัวแปรของเกม
    let currentQuestion = 0;
    let score = 0;


    // เริ่มเกม
    function startGame() {

        currentQuestion = 0;
        score = 0;

        document.getElementById("startScreen").style.display = "none";
        document.getElementById("resultScreen").style.display = "none";
        document.getElementById("gameScreen").style.display = "block";

        showQuestion();
    }


    // แสดงคำถาม
    function showQuestion() {

        let q = questions[currentQuestion];

        document.getElementById("questionNumber").innerText =
            "ข้อที่ " + (currentQuestion + 1) + " / " + questions.length;

        document.getElementById("question").innerText =
            q.question;

        document.getElementById("score").innerText =
            "คะแนน: " + score;

        let answersDiv = document.getElementById("answers");

        answersDiv.innerHTML = "";


        // สร้างปุ่มคำตอบ
        q.answers.forEach(function(answer) {

            let button = document.createElement("button");

            button.innerText = answer;

            button.onclick = function() {
                checkAnswer(answer);
            };

            answersDiv.appendChild(button);

        });
    }


    // ตรวจคำตอบ
    function checkAnswer(answer) {

        let correctAnswer = questions[currentQuestion].correct;


        // If-Else ตรวจว่าตอบถูกหรือผิด
        if (answer === correctAnswer) {

            alert("✅ ถูกต้อง!");

            score = score + 1;

        } else {

            alert("❌ ผิด!");

        }


        currentQuestion++;


        // ตรวจว่าครบทุกข้อหรือยัง
        if (currentQuestion < questions.length) {

            showQuestion();

        } else {

            showResult();

        }

    }


    // แสดงผลคะแนน
    function showResult() {

        document.getElementById("gameScreen").style.display = "none";
        document.getElementById("resultScreen").style.display = "block";


        document.getElementById("finalScore").innerText =
            "คุณได้คะแนน " + score + " / " + questions.length;


        // If-Else ประเมินคะแนน
        if (score >= 4) {

            document.getElementById("result").innerText =
                "🏆 เก่งมาก! คุณรู้จักประเทศไทยดีมาก";

        } else if (score >= 2) {

            document.getElementById("result").innerText =
                "👍 ทำได้ดี! ลองเล่นอีกครั้งเพื่อทำคะแนนให้สูงขึ้น";

        } else {

            document.getElementById("result").innerText =
                "📚 พยายามอีกนิด! ลองศึกษาจังหวัดต่าง ๆ แล้วเล่นใหม่";

        }

    }

</script>

</body>
</html>
