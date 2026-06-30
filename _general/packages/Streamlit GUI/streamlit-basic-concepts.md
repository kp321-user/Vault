# Streamlit Basic Concepts

## Running an app

```bash
streamlit run your_script.py [-- script args]
```

This spins up a local server and opens the app in a new browser tab. The app is your canvas — charts, text, widgets, tables, etc. See the API reference for the full list of available commands. **Note:** custom script arguments must go after `--`, otherwise Streamlit interprets them as its own arguments.

Can also run as a module (useful for IDE configs like PyCharm):
```bash
python -m streamlit run your_script.py
# equivalent to:
streamlit run your_script.py
```

You can even pass a URL — handy with GitHub Gists:
```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```
## Data flow
Streamlit's defining trait: **any UI update reruns the entire script top to bottom.** This happens when:
1. You modify the app's source code, or
2. A user interacts with a widget (slider, text input, button, etc.)
If a widget has an `on_change` / `on_click` callback, that callback runs *before* the rest of the script reruns. To keep this fast, Streamlit relies heavily on `@st.cache_data` to skip expensive recomputation on rerun.

## Widgets

Widgets behave like variables — Streamlit reruns the script top to bottom on interaction, with the widget's current value bound on each run:
```python
import streamlit as st
x = st.slider('x')  # <- this is a widget
st.write(x, 'squared is', x * x)
```
Move the slider to 10 → script reruns → `x = 10` → output updates to "10 squared is 100".
### Keyed widgets → Session State
```python
import streamlit as st
st.text_input("Your name", key="name")

# Access the value at any point with:
st.session_state.name
```
Any widget given a `key` is automatically tracked in Session State.
### Checkbox to show/hide content
```python
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
```

### Selectbox
```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```
## Layout
Streamlit makes it easy to organize your widgets in a left panel sidebar with [`st.sidebar`](https://docs.streamlit.io/develop/api-reference/layout/st.sidebar). 
### Sidebar
Pin widgets to a left panel via `st.sidebar`:
```python
import streamlit as st

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
```
### Columns and expanders
`st.columns` places widgets side by side; `st.expander` hides content to save space.
```python
import streamlit as st

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
```
## Show Progress
When adding long running computations to an app, you can use [`st.progress()`](https://docs.streamlit.io/develop/api-reference/status/st.progress) to display status in real time.
```python
import streamlit as st
import time

'Starting a long computation...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
```

---

## See also
[[streamlit-api-reference]] — full command reference

*Source: condensed from the official [Streamlit "Basic Concepts" guide](https://docs.streamlit.io/get-started/fundamentals/basic-concepts). Nav/footer clutter and forum prompts stripped; content and code preserved.*
