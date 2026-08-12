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
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            text-align: center;
        }
        .container {
            background: rgba(17, 24, 39, 0.95);
            border: 1px solid #1f293d;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 255, 204, 0.15);
            width: 90%;
            max-width: 500px;
        }
        h1 {
            color: #00ffcc;
            margin-bottom: 10px;
            font-size: 26px;
        }
        .tagline {
            font-size: 14px;
            color: #9ca3af;
            margin-bottom: 25px;
        }
        .features-box {
            background: #111827;
            border: 1px solid #374151;
            padding: 15px;
            border-radius: 8px;
            text-align: left;
            margin-bottom: 25px;
        }
        .features-box h3 {
            font-size: 15px;
            color: #38bdf8;
            margin-bottom: 8px;
        }
        .features-box ul {
            list-style-type: none;
            padding-left: 0;
            font-size: 13px;
            color: #d1d5db;
        }
        .features-box li {
            margin-bottom: 6px;
        }
        .btn {
            background: linear-gradient(135deg, #00ffcc, #0077ff);
            color: #0b0f19;
            border: none;
            padding: 14px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s ease;
            width: 100%;
            text-decoration: none;
            display: inline-block;
        }
        .btn:hover {
            opacity: 0.9;
            transform: scale(1.02);
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>🛡️ CyberMind Pro</h1>
        <p class="tagline">Advanced Cybersecurity & Threat Management System</p>
        
        <div class="features-box">
            <h3>App Features:</h3>
            <ul>
                <li>🔒 Real-time system security & diagnostics</li>
                <li>🛡️ Firewall protection & threat analyzer</li>
                <li>⚡ Instant vulnerability scanning</li>
            </ul>
        </div>
        
        <a href="YOUR_APP_LINK_HERE" target="_blank" class="btn" id="openBtn">Open in Chrome Browser</a>
    </div>

    <script>
        // Automatic trigger option agar direct redirect chahiye ho
        // window.location.href = "YOUR_APP_LINK_HERE";
    </script>

</body>
</html>
