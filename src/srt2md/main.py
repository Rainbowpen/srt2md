import argparse
import os

# from ollama import chat
from ollama import ChatResponse
from ollama import Client


class Translation:
    def __init__(self, ollama_host: str):
        self.client = Client(
            host=ollama_host,
            headers={'x-some-header': 'some-value'}
        )

    def call_ollama(self, text: str) -> str:
        response: ChatResponse = self.client.chat(model='gemma3:4b', messages=[
            {
                'role': 'user',
                'content': f'Translate the giving text from fr into en. Only return the translation. Nothing else. DO NOT YAPPING. ```{text}```',
            },
        ])
        # print(response['message']['content'])
        # or access fields directly from the response object
        # print(response.message.content)
        return response['message']['content'].split("\n")[0]


def srt_to_markdown(source_file: str, output_file: str = "output.md", ollama_host: str = "http://localhost:11434") -> None:
    trans = Translation(ollama_host)
    # trans.call_ollama("[Eda] Que voulez-vous manger ?")
    markdown_content = ""
    markdown_content += f"**Time** | **French (Original)** | **English (Translation)**\n"
    markdown_content += f"------- | -------- | --------\n"
    s_path = os.path.expanduser(source_file)
    if os.path.exists(s_path):
        with open(s_path, "r") as file:
            content = file.read()
            # a = content.split("\n\n")
            b = [i.split("\n") for i in content.split("\n\n")]
            for i in b:
                if len(i) > 1:
                    for j in range(1, 11):
                        ot = "".join(i[2:])
                        t = trans.call_ollama(ot)
                        if abs(len(t) - len(i[2]) <= 30):
                            print(f"{i[1]} | {ot} | {t}\n")
                            markdown_content += f"{i[1]} | {ot} | {t}\n"
                            break
                        else:
                            print(f"{i[2]} | {t}")

                        if j == 10:
                            markdown_content += f"{i[1]} | {ot} | {i[2]}\n"

                print(markdown_content)

            with open(os.path.expanduser(output_file), "w") as file:
                file.write(markdown_content)
    else:
        print(f"The path to {source_file} doesn't exist.")


def main():
    parser = argparse.ArgumentParser(description=".srt file to .md Script")
    parser.add_argument("-i", nargs=1,
                        metavar=("SOURCE"), help="Path to .srt file")
    parser.add_argument("-o", nargs=1,
                        metavar=("DEST"), help="Path to output.md")
    parser.add_argument("-s", nargs=1,
                        metavar=("ollama_host"), help="url to the ollama host. (Default to http://localhost:11434)")
    parser.add_argument('--version', action='version',
                        version='srt2md 0.01')
    args = parser.parse_args()

    if not any([args.i, args.o, args.s]):
        print("Use --help to see available options")
        print("Example:\n   srt2md -i path_to_srt -o path_to_md")
    elif args.i and args.o and not args.s:
        srt_to_markdown(args.i[0], args.o[0])
    elif args.i and args.o and args.s:
        srt_to_markdown(args.i[0], args.o[0], args.s[0])
    elif args.i and not args.o:
        print("missing path_to_md")
    elif not args.i and args.o:
        print("missing path_to_srt")
    else:
        print("Use --help to see available options")
        print("Example:\n   srt2md -i path_to_srt -o path_to_md")


if __name__ == "__main__":
    main()
