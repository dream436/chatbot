import streamlit as st

class Layout:
    
    def show_header(self, types_files):
        """
        Displays the header of the app
        """
        st.markdown(
            f"""
            <div style="display: flex;justify-content: center;">
            <img src="https://static.wixstatic.com/media/42f43b_9a634dde85f641ca91f1096ceb17b0a2~mv2.png/v1/fill/w_163,h_101,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logo_transparent_background%20(1).png"/>
            </div>
            <h1 style='text-align: center;'> Ask GQI GPT about your {types_files} files ! 😁</h1>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        """
        Displays a message if the user has not entered an API key
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Enter your <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API key</a> to start chatting</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="Ask me anything about the document...",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Send")
            
            is_ready = submit_button and user_input
        return is_ready, user_input
    
