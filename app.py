def get_ai_response(prompt):
    prompt = prompt.lower()
    if "scam" in prompt:
        return "CyberMind AI: Scam se bachne ke liye hamesha link ka domain check karein aur kabhi OTP share na karein."
    elif "password" in prompt:
        return "CyberMind AI: Apne password mein special characters (@, #, $) aur numbers ka use zaroor karein."
    elif "hack" in prompt:
        return "CyberMind AI: Agar account hack hua hai, toh turant 2FA enable karein aur recovery email check karein."
    else:
        return f"CyberMind AI: '{prompt}' ke baare mein main seekh raha hoon. Kya aap security ya scam ke baare mein puchna chahte hain?"
