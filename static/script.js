async function register() {
  const userId = document.getElementById("user_id").value;
  const seed = document.getElementById("seed").value;

  // シードからステップ（ランダムウォーク）を生成
  const steps = generateWalk(seed);

  const response = await fetch("/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, steps: steps }),
  });

  const data = await response.json();
  document.getElementById("message").innerText = data.message;
}

async function login() {
  const userId = document.getElementById("user_id").value;
  const seed = document.getElementById("seed").value;

  // シードからステップ（ランダムウォーク）を生成
  const steps = generateWalk(seed);

  const response = await fetch("/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, steps: steps }),
  });

  const data = await response.json();
  if (data.result === "success") {
    window.location.href = "/success"; // ログイン成功後に遷移
  } else {
    document.getElementById("message").innerText = "認証失敗";
  }
}

// シードを基にランダムウォークを生成する関数（仮）
function generateWalk(seed) {
  const steps = [];
  // seedrandom を使ってシード値でランダム生成
  let random = new Math.seedrandom(seed); // seedrandomでシードに基づく乱数生成
  const moves = ["U", "D", "L", "R", "S"]; // 上下左右動かない5パターン

  for (let i = 0; i < 256; i++) {
    // 50ステップを生成
    const move = moves[Math.floor(random() * moves.length)];
    steps.push(move);
  }

  return steps.join(",");
}
