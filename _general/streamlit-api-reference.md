# Streamlit API Reference

Streamlit ([streamlit.io](https://streamlit.io/)) is an open-source app framework — simple, easy to use, installed like any other Python library. Good for testing programs without deploying to the web.

**Core principle:** It isn't a normal web framework. There's no routing, no request handlers, no templates — the Python script *is* the entire app, top to bottom, and Streamlit reruns the whole file on every interaction. That single fact explains almost everything else. Every `st.*` call sends an instruction over a WebSocket telling the browser (React under the hood) to render something.

Because the whole script reruns on every interaction, normal Python variables don't persist between runs — that's what `st.session_state` is for: a dict that *survives* reruns (tied to the browser session), while everything else gets wiped and recomputed.

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")
```

Build an app in a few lines with a simple API, then watch it auto-update as you save the source file.

---

## Write & Magic

| Function | Description | Example |
|---|---|---|
| `st.write` | Write arguments to the app (auto-detects type) | `st.write("Hello **world**!")` |
| `st.write_stream` | Write generators/streams with a typewriter effect | `st.write_stream(my_llm_stream)` |

## Text Elements

| Function | Description | Example |
|---|---|---|
| `st.markdown` | Display string formatted as Markdown | `st.markdown("Hello **world**!")` |
| `st.title` | Title formatting | `st.title("The app title")` |
| `st.header` | Header formatting | `st.header("This is a header")` |
| `st.subheader` | Subheader formatting | `st.subheader("This is a subheader")` |
| `st.badge` | Small colored badge | `st.badge("New")` |
| `st.caption` | Small font text | `st.caption("small caption text")` |
| `st.code` | Code block w/ syntax highlighting | `st.code("a = 1234")` |
| `st.echo` | Display code, then execute it (tutorials) | `with st.echo(): st.write('printed')` |
| `st.latex` | LaTeX-formatted math | `st.latex(r"\int a x^2 \,dx")` |
| `st.text` | Fixed-width preformatted text | `st.text("Hello world")` |
| `st.divider` | Horizontal rule | `st.divider()` |
| `st.help` | Show an object's docstring | `st.help(st.write)` |
| `st.html` | Render raw HTML | `st.html("<p>Foo bar.</p>")` |
| `st.iframe` | Embed content in an iframe | `st.iframe("https://docs.streamlit.io")` |

## Data Elements

| Function | Description | Example |
|---|---|---|
| `st.dataframe` | Interactive table | `st.dataframe(my_data_frame)` |
| `st.data_editor` | Editable data widget | `edited = st.data_editor(df, num_rows="dynamic")` |
| `st.column_config` | Configure dataframe/data_editor columns | `st.column_config.NumberColumn("Price", min_value=0, format="$%d")` |
| `st.table` | Static table | `st.table(my_data_frame)` |
| `st.metric` | Big bold metric w/ optional delta indicator | `st.metric("My metric", 42, 2)` |
| `st.json` | Pretty-printed JSON | `st.json(my_dict)` |

## Chart Elements

| Function | Description |
|---|---|
| `st.area_chart` / `st.bar_chart` / `st.line_chart` / `st.scatter_chart` | Simple built-in charts from a dataframe |
| `st.map` | Scatterplot on a map |
| `st.pyplot` | Display a Matplotlib figure |
| `st.altair_chart` | Altair chart |
| `st.vega_lite_chart` | Vega-Lite chart |
| `st.plotly_chart` | Interactive Plotly chart |
| `st.pydeck_chart` | PyDeck chart |
| `st.graphviz_chart` | GraphViz chart (dagre-d3) |

## Input Widgets

| Function | Description | Example |
|---|---|---|
| `st.button` | Button | `clicked = st.button("Click me")` |
| `st.download_button` | Download button | `st.download_button("Download file", file)` |
| `st.form_submit_button` | Submit button for `st.form` | `st.form_submit_button("Sign up")` |
| `st.link_button` | Button that opens a URL | `st.link_button("Go to gallery", url)` |
| `st.menu_button` | Dropdown menu button | `st.menu_button("Export", options=["CSV","JSON","PDF"])` |
| `st.page_link` | Link to another page in a multipage app | `st.page_link("pages/profile.py", label="My profile")` |
| `st.checkbox` | Checkbox | `selected = st.checkbox("I agree")` |
| `st.color_picker` | Color picker | `color = st.color_picker("Pick a color")` |
| `st.feedback` | Rating/sentiment buttons | `st.feedback("stars")` |
| `st.multiselect` | Multi-select (starts empty) | `st.multiselect("Buy", ["milk","apples","potatoes"])` |
| `st.pills` | Pill-button selector | `st.pills("Tags", ["Sports","AI","Politics"])` |
| `st.radio` | Radio buttons | `choice = st.radio("Pick one", ["cats","dogs"])` |
| `st.segmented_control` | Segmented button selector | `st.segmented_control("Filter", ["Open","Closed","All"])` |
| `st.selectbox` | Dropdown select | `choice = st.selectbox("Pick one", ["cats","dogs"])` |
| `st.select_slider` | Slider over a list of items | `size = st.select_slider("Pick a size", ["S","M","L"])` |
| `st.toggle` | Toggle switch | `activated = st.toggle("Activate")` |
| `st.number_input` | Numeric input | `choice = st.number_input("Pick a number", 0, 10)` |
| `st.slider` | Numeric slider | `number = st.slider("Pick a number", 0, 100)` |
| `st.date_input` | Date picker | `date = st.date_input("Your birthday")` |
| `st.datetime_input` | Datetime picker | `dt = st.datetime_input("Schedule your event")` |
| `st.time_input` | Time picker | `time = st.time_input("Meeting time")` |
| `st.chat_input` | Chat-style input | `prompt = st.chat_input("Say something")` |
| `st.text_area` | Multi-line text input | `text = st.text_area("Text to translate")` |
| `st.text_input` | Single-line text input | `name = st.text_input("First name")` |
| `st.pagination` | Pagination widget | `page = st.pagination(10)` |
| `st.audio_input` | Mic recording widget | `speech = st.audio_input("Record a voice message")` |
| `st.file_uploader` | File upload widget | `data = st.file_uploader("Upload a CSV")` |
| `st.camera_input` | Camera capture widget | `image = st.camera_input("Take a picture")` |

## Media Elements

| Function | Description |
|---|---|
| `st.image` | Display image(s) — numpy array, bytes, file, or URL |
| `st.logo` | Logo in upper-left corner + sidebar |
| `st.pdf` | Display a PDF file |
| `st.audio` | Audio player |
| `st.video` | Video player |

## Layouts & Containers

| Function | Description | Example |
|---|---|---|
| `st.columns` | Side-by-side containers | `col1, col2 = st.columns(2)` |
| `st.container` | Multi-element container | `c = st.container()` |
| `st.dialog` | Modal dialog (reruns independently) | `@st.dialog("Sign up")` |
| `st.empty` | Single-element placeholder container | `c = st.empty()` |
| `st.expander` | Collapsible container | `with st.expander("Open to see more"):` |
| `st.popover` | Click-to-open popover container | `with st.popover("Settings"):` |
| `st.sidebar` | Sidebar container | `st.sidebar.button("Click me!")` |
| `st.bottom` | Container pinned to bottom of window | `st.bottom.chat_input("Say something")` |
| `st.space` | Vertical/horizontal spacer | `st.space("small")` |
| `st.tabs` | Tabbed containers | `tab1, tab2 = st.tabs(["Tab 1","Tab 2"])` |

## Chat Elements

Built to be used together: `st.chat_message` inserts a chat bubble container (can hold any other Streamlit element), `st.chat_input` displays the input box.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```

- `st.status` — container for long-running task output: `with st.status('Running'): do_something_slow()`
- `st.write_stream` — typewriter-effect streaming output

## Status Elements

| Function | Description | Example |
|---|---|---|
| `st.progress` | Progress bar | `for i in range(101): st.progress(i)` |
| `st.spinner` | Spinner during a block of code | `with st.spinner("Please wait..."):` |
| `st.status` | Long-running task output container | `with st.status('Running'):` |
| `st.toast` | Brief bottom-right toast message | `st.toast('Butter!', icon='🧈')` |
| `st.balloons` | Celebratory balloons | `st.balloons()` |
| `st.snow` | Celebratory snowflakes | `st.snow()` |
| `st.success` / `st.info` / `st.warning` / `st.error` | Colored message boxes | `st.success("Match found!")` |
| `st.exception` | Display an exception | `st.exception(e)` |

---

## App Logic & Configuration

**App server**
- `st.App()` — configure the underlying Starlette server

**Authentication**
- `st.login()` — start an auth flow with an identity provider
- `st.logout()` — remove a user's identity info
- `st.user` — info about the logged-in user (`if st.user.is_logged_in: ...`)

**Navigation and pages**
- `st.navigation({...})` — configure pages in a multipage app, grouped by section:
  ```python
  st.navigation({
      "Your account": [log_out, settings],
      "Reports": [overview, usage],
      "Tools": [search]
  })
  ```
- `st.Page(...)` — define a page: `home = st.Page("home.py", title="Home", icon=":material/home:")`
- `st.page_link(...)` — link to another page
- `st.switch_page(...)` — programmatically navigate: `st.switch_page("pages/my_page.py")`

**Execution flow**
- `st.dialog` — modal dialog, reruns independently
- `st.form` — batch inputs with a submit button:
  ```python
  with st.form(key='my_form'):
      name = st.text_input("Name")
      email = st.text_input("Email")
      st.form_submit_button("Sign up")
  ```
- `st.fragment` — rerun a function independently of the rest of the script: `@st.fragment(run_every="10s")`
- `st.rerun()` — rerun the script immediately
- `st.stop()` — stop execution immediately

**Caching and state**
- `st.cache_data` — cache functions returning data (dataframe transforms, queries, ML inference)
- `st.cache_resource` — cache functions returning global resources (DB connections, ML models)
- `st.session_state` — dict that survives reruns, scoped per user session
- `st.query_params` — get/set/clear URL query params
- `st.context` — read-only access to cookies, headers, locale, browser-session info

**Connections and databases**
- `st.connection('name', type='sql')` — connect to a data source/API:
  ```python
  conn = st.connection('pets_db', type='sql')
  pet_owners = conn.query('select * from pet_owners')
  ```
- Built-in: `SnowflakeConnection`, `SQLConnection` (SQLAlchemy)
- Build your own: subclass `BaseConnection`
- Secrets: `st.secrets["KEY"]`, stored in a per-project/per-profile `secrets.toml`

**Custom components**
- V2: `st.components.v2.component(html=HTML, js=JS)` + npm package `@streamlit/component-v2-lib`
- V1: `declare_component(name, path)`, `st.components.v1.html(...)`, `st.components.v1.iframe(...)`

**Configuration**
- `.streamlit/config.toml` — default app settings
- `st.get_option(...)` / `st.set_option(...)` — read/write a config option
- `st.set_page_config(page_title=..., page_icon=...)` — page-level settings

---

## Developer Tools — App Testing

`st.testing.v1.AppTest` simulates a running app for tests:

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("streamlit_app.py")
at.secrets["WORD"] = "Foobar"
at.run()
assert not at.exception

at.text_input("word").input("Bazbat").run()
assert at.warning[0].value == "Try again."
```

Constructors: `AppTest.from_file(...)`, `AppTest.from_string(...)`, `AppTest.from_function(...)`

Element/container representations available on `at` (each with simulated interactions, then `.run()`):

- **Block** — containers: `st.chat_message`, `st.columns`, `st.sidebar`, `st.tabs`, main body
- **Element** — base class for display elements: `st.title`, `st.header`, `st.markdown`, `st.dataframe`
- **Button** — `at.button[0].click().run()`
- **ChatInput** — `at.chat_input[0].set_value("...").run()`
- **Checkbox** — `at.checkbox[0].check().run()`
- **ColorPicker** — `at.color_picker[0].pick("#FF4B4B").run()`
- **DateInput** — `at.date_input[0].set_value(date(2023,10,26)).run()`
- **Multiselect** — `at.multiselect[0].select("New York").run()`
- **NumberInput** — `at.number_input[0].increment().run()`
- **Radio** — `at.radio[0].set_value("New York").run()`
- **SelectSlider** — `at.select_slider[0].set_range("A","C").run()`
- **Selectbox** — `at.selectbox[0].select("New York").run()`
- **Slider** — `at.slider[0].set_range(2,5).run()`
- **TextArea** — `at.text_area[0].input("Streamlit is awesome!").run()`
- **TextInput** — `at.text_input[0].input("Streamlit").run()`
- **TimeInput** — `at.time_input[0].increment().run()`
- **Toggle** — `at.toggle[0].set_value(True).run()`

---

*Source: condensed from the official [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference). Reference images, "Third-party components" promo blocks, and footer/nav clutter stripped out — code examples and descriptions preserved.*
