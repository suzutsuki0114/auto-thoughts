from google import genai
import env

class Gemini:
    def __init__(self):
        self.client = genai.Client()

    def thoughts(self, document):
        prompt = f"次のプレーンテキストで書かれたドキュメントは学校の授業の参考資料です。\n\
        ですます調で、ふざけずに、その資料を見て授業についての感想を3文ほどで書いてください。\n\
        文の長さは短めにしてください。\n\
        今から書きますなどの前置きはいりません。感想のみを書いてください。\n\
        また、資料を見た感想ではなく、授業を受けたかのような感想を書いてください。\n\
        次の文章からがそのドキュメントです。\n\
        {document}"
        response = self.client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        return response.text
