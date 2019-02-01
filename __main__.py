import sys

from md2html.md2html import Md2Html

def main():
    args = sys.argv

    if len(args) <= 1:
        print("引数の数が足りません。")
        return 1

    source = args[1]

    
    if len(args) > 2:
        output = args[2] 
    else:
        output = "index.html"

    if len(args) > 3:
        proxy = args[3] 
    else:
        proxy = "none"

    print(source)
    print(output)
    print(proxy)

    engine = Md2Html()

    engine.set_proxy(proxy)

    engine.to_html(source, output)

main()