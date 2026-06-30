#UI

Streamlit is an open-source app framework that is simple and easy-to-use
(https://streamlit.io/)

Installed like any other python library
Good for testing programs without deploying to web
Streamlit builds upon three simple principles
- Embrace scripting
	- Build an app in a few lines of code with a simple [[streamlit-api-reference]]. Then see it automatically update as you iteratively save the source file.
-  Weave in interaction
	- Adding a widget is the same as [declaring a variable](https://docs.streamlit.io/library/get-started/main-concepts#widgets). No need to write a backend, define routes, handle HTTP requests, connect a frontend, write HTML, CSS, JavaScript, ...

Pick a number

0

100

`[number = st.slider("Pick a number", 0, 100)](https://docs.streamlit.io/library/api-reference/widgets/st.slider)`

Pick a date

June2026

Su

Mo

Tu

We

Th

Fr

Sa

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

`[date = st.date_input("Pick a date")](https://docs.streamlit.io/library/api-reference/widgets/st.date_input)`

## Deploy instantly

The choice is yours — show off your public apps for free on [Streamlit Community Cloud](https://share.streamlit.io/?utm_source=streamlit&utm_medium=referral&utm_campaign=main&utm_content=-ss-streamlit-io-deployinstantly), go with [Snowflake](https://docs.snowflake.com/developer-guide/streamlit/about-streamlit) for enterprise‑grade deployment, or pick [something else entirely!](https://docs.streamlit.io/deploy/tutorials)

Features:
- Isn't a normal web framework. There's no routing, no request handlers, no templates. The Python script is the entire app, top to bottom, and Streamlit reruns the whole file every time something happens. That's the single fact that explains almost everything else about how it behaves. Every st.* call doesn't just "draw" something — it sends an instruction over a WebSocket to the browser saying "render a title here," "render a text input here," etc. The browser (running React under the hood) draws those components. Since the whole script reruns on every interaction, normal Python variables don't persist between runs. That's why Streamlit has `st.session_state`.

`session_state` is a dict that _survives_ reruns (tied to that browser session), while everything else gets wiped and recomputed.
	```python
	if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")
	```