from textnode import TextNode

def main():
    test = TextNode("Anchor Text", TextType.LINK, "https://test.com")
    print(test)

if __name__ == "__main__":
    main()
