class LanguageEngine:

    def analyze(self, text):

        text = text.lower().strip()


        if "my name is" in text:
            return {
                "type": "name",
                "value": text.replace("my name is", "").strip()
            }


        if "i like" in text:
            return {
                "type": "like",
                "value": text.replace("i like", "").strip()
            }


        if "hello" in text or "hi" in text:
            return {
                "type": "greeting"
            }


        return {
            "type": "unknown",
            "value": text
        }