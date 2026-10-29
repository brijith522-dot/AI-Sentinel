def analyze_text(text):
   suspicious_phrases=[
      "ignore all previous instructions",
      "reveal the system prompt",
      "show confidential information",
      "bypass security"
   ]
   findings= []
   
   for phrase in suspicious_phrases:
      if phrase in text.lower():
         findings.append(phrase)

   return findings
   
     
def main():
   print("="*40)
   print("       AI SENTINEL")
   print("  AI Security Risk Analyser")
   print("="*40)

   user_input=input("\nEnter text to analyse:")

   if not user_input.strip():
      print("Please enter some text.")
      return

   findings=analyze_text(user_input)

   print("\nAnalysis completed!")
   print("Input length:",len(user_input),"characters")

   if findings:
      print("Result:Potentially suspicious phrases detected.")
      for phrase in findings:
        if "show confidential information" in phrase:
           print("Warning:HIGH RISK - This phrase may indicate an attempt to access sensitive data.")
        elif "ignore all previous instructions" in phrase:
           print("Warning:MEDIUM RISK - This phrase may indicate an attempt to override system instructions.")
        elif "bypass security" in phrase:
           print("Warning:MEDIUM RISK - This phrase may indicate an attempt to bypass security measures.")
        elif "reveal the system prompt" in phrase:
           print("Warning:MEDIUM RISK - Review for possible prompt disclosure.")
        else:
           print("Warning:LOW RISK - This phrase may indicate a potential security concern.")
      
        print("-Flagged phrase:",phrase)
   else:
      print("Result:No configured suspicious phrases detected.")

   print("\nNote:This is a basic rule-based prototype.")
   print("It cannot detect every security threat.")


if __name__ == "__main__":
    main()
