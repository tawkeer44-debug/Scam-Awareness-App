<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CyberMind Pro - Security Dashboard</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body {
            background-color: #0b0f19;
            color: #00ffcc;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .dashboard {
            background: rgba(17, 24, 39, 0.9);
            border: 1px solid #1f293d;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 255, 204, 0.1);
            width: 450px;
            text-align: center;
        }
        h1 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 24px;
        }
        .status {
            font-size: 14px;
            color: #9ca3af;
            margin-bottom: 25px;
        }
        .btn {
            background: linear-gradient(135deg, #00ffcc, #0077ff);
            color: #0b0f19;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s ease;
            width: 100%;
        }
        .btn:hover {
            opacity: 0.9;
            transform: scale(1.02);
        }
        #output {
            margin-top: 20px;
            font-size: 14px;
            color: #38bdf8;
            min-height: 40px;
        }
    </style>
</head>
<body>

    <div class="dashboard">
        <h1>🛡️ CyberMind Pro</h1>
        <p class="status">Advanced System Security & Threat Analyzer</p>
        
        <button class="btn" onclick="runSecurityScan()">Initialize Security Scan</button>
        
        <div id="output">System ready for diagnostics...</div>
    </div>

    <script>
        function runSecurityScan() {
            const output = document.getElementById("output");
            output.innerHTML = "🔄 Initializing firewall protocols...";
            
            setTimeout(() => {
                output.innerHTML = "🔍 Scanning network ports and checking vulnerabilities...";
            }, 1200);

            setTimeout(() => {
                output.innerHTML = "✅ Status: All systems secure. No threats detected.";
            }, 2500);
        }
    </script>

</body>
</html>
