from google import genai

# Initialize the client (automatically uses GEMINI_API_KEY from environment)
client = genai.Client()
MODEL_NAME = "gemini-2.0-flash-exp" 

def rewrite_email(email_text, style):
    prompt = f'''
    Rewrite the following email in a **{style}** tone:
    Email:
    {email_text}
    '''
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

def refine_email(prev, feedback):
    prompt = f'''
    Improve this email based on the feedback "{feedback}":
    {prev}
    '''
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

def main():
    print("Smart Email Rewriter (Gemini 2.0 Version)")

    email_text = input("Paste the email you want to rewrite:\n\n")
    print("\nChoose style: 1) Professional 2) Friendly 3) Concise")
    style_map = {"1":"professional","2":"friendly and warm","3":"concise and to the point"}
    style = style_map.get(input("Enter 1,2,3: ").strip(), "professional")

    rewritten = rewrite_email(email_text, style)
    print("\n----- Rewritten Email -----\n", rewritten, "\n---------------------------")

    while input("Refine? (y/n): ").lower()=="y":
        fb=input("Feedback: ")
        rewritten = refine_email(rewritten, fb)
        print("\n----- Updated Version -----\n", rewritten, "\n---------------------------")

if __name__ == "__main__":
    main()
