from google import genai
import env

class Gemini:
    def __init__(self):
        self.client = genai.Client()

    def thoughts(self, document):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=f"次のプレーンテキストで書かれたドキュメントは地理の授業の参考資料です。\nですます調で、ふざけずに、その資料を見て授業についての感想を3文ほどで書いてください。\n文の長さは短めにしてください。\n今から書きますなどの前置きはいりません。感想のみを書いてください。\n次の文章からがそのドキュメントです。\n{document}"
        )
        return response.text
