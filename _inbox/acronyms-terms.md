#Acronyms #reference #python #terminology

- **[[Terminal]]** — the window/app itself. Just a box that displays text and lets you type. It doesn't interpret anything on its own.
- **[[Shell]]** — the program running inside a terminal window in vs code for example that actually understands your commands. So when you open Git Bash, you get a terminal window running the Bash shell inside it. That's why Git Bash commands look like Linux commands (forward slashes, source, ls) rather than Windows ones (backslashes, dir) — you're talking to Bash, not to Windows directly.There's more than one shell, by the way — Bash is just the most common. Windows has its own native shells too: Command Prompt (cmd.exe, older) and PowerShell (newer, more powerful). They understand different commands than Bash does — that's why a command that works in Git Bash sometimes fails if you paste it into PowerShell, and vice versa. Same idea (a shell), different "language" each one understands.
- **.bashrc** is specifically Bash's settings file — it runs every time a new Bash shell starts, which is why putting your alias there means it's available every time you open Git Bash, instead of just once.
- **[[Git Bash]]** — a specific terminal program for Windows that gives you the Bash shell (the same shell Linux/Mac use) instead of Windows' native shell.
- **MINGW64** stands for Minimalist GNU for Windows, 64-bit
- **Bash** stands for Bourne Again Shell — it's a pun. The original Unix shell from the 1970s was written by a guy named Stephen Bourne, called the "Bourne Shell" (sh). In 1989, a new improved version was released and named "Bourne Again Shell" — a joke on "born again." A shell in general just means the program that sits between you and the operating system, letting you type commands. There are several shells: 1- bash (most common on Linux/ac), 2- zsh (default on modern Macs), 3- PowerShell (Windows), 4- cmd.exe (older Windows); They all do the same basic job, just with slightly different syntax.
- **Protobuf** = Protocol Buffers, a format created by Google for serializing structured data — basically a more compact, faster, strictly-typed alternative to JSON for passing data between two programs.
- **CLI** Command-Line Interface. It just means running a program by typing commands into a terminal (like your Git Bash window) instead of clicking buttons in a browser or app window.
- **[[CUDA]]** stands for Compute Unified Device Architecture...
- [[WebSocket]] is a way for a browser and a server to keep a connection open and send messages back and forth in both directions, without the browser having to re-ask for a new page each time.
- [[HTTP]] Hypertext Transfer Protocol: the system that lets your browser request and receive web pages from servers. It works like a request-response language for the web, helping devices exchange page data, images, and other content. browsing is request → response, then the connection closes.
- [[Streamlit]] isn't a normal web framework. There's no routing, no request handlers, no templates. The Python script is the entire app, top to bottom, and Streamlit reruns the whole file every time something happens. That's the single fact that explains almost everything else about how it behaves. Every st.* call doesn't just "draw" something — it sends an instruction over a WebSocket to the browser saying "render a title here," "render a text input here," etc. The browser (running React under the hood) draws those components. Since the whole script reruns on every interaction, normal Python variables don't persist between runs. That's why Streamlit has st.session_state.
**IDE** = **Integrated Development Environment**.

It's a single application that bundles together the main tools you need to write and run code, so you're not jumping between separate programs. Typically that means:

- **Code editor** — where you actually type code, usually with syntax highlighting
- **Debugger** — lets you pause execution, step through code line-by-line, inspect variable values
- **Build/run tools** — a button or shortcut to actually execute your program, built in
- **Often: project/file management, version control integration, autocomplete**

The "integrated" part is the key word — everything lives in one window instead of you using a plain text editor, then switching to a terminal to run the code, then switching to another tool to debug.

**Where VS Code sits:** out of the box, it's closer to a smart text editor — it has an editor, a terminal, Git integration. What it lacks natively is deep language-aware tooling (debugging, intelligent autocomplete, error-checking) — you add those per-language via extensions (e.g. the Python extension gives you a debugger, linting, IntelliSense for Python specifically). Once those are installed, it functions as a full IDE for that language — which is the state your setup is already in.

**For comparison**, something like PyCharm is a "true" IDE because it ships with all of that Python-specific tooling already built in — you don't add it, it's just there. The tradeoff: PyCharm is heavier and Python-only, where VS Code is lighter and adapts to whatever language you install support for.