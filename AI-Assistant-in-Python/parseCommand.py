def commandParser(command):
    keywords = ["news", "open", "play"]

    for keyword in keywords:
        if keyword in command:
            if keyword == "news":
                if "about" in command:
                    topic = command.split("about", 1)[1].strip()
                    return f"news {topic}"
                elif "on" in command:
                    topic = command.split("on", 1)[1].strip()
                    return f"news {topic}"
                elif command.strip().endswith("news"):
                    if command.strip() == "tell me some news":
                        return "news"
                    topic = command.rsplit("news", 1)[0].strip()
                    return f"news {topic}"
            elif keyword == "open":
                app_name = command.split("open", 1)[1].strip()
                return f"open {app_name}"
            elif keyword == "play":
                app_name = command.split("play", 1)[1].strip()
                return f"play {app_name}"

    return command

if __name__ == "__main__":
    # Examples
    while True:
        command = input("Enter Command: ")
        print(commandParser(command))