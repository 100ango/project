
from fasthtml.common import *

app,rt = fast_app(live=True)
@rt("/")
def get():
    page = Html(
                Head(
                    Meta(charset="utf-8"),
                    Meta(name="viewport",content="width=device-width"),
                    Title("Fasthtml demo"),
                    Link(rel="stylesheet", type="text/css", href="css/main.css"),
                    Link(href="favicon.ico", rel="icon",type="image/x-icon"),
                    lang="en-us"
                ),

                Body(mk_header(), mk_content())
    )
    
    return page

def mk_header():
    header = Header(
                    Section(
                        Nav(
                            Img(src="images/logo.svg",cls="logo"),
                            Ul(
                                Li(A("Cloud", hx_get=f"/",cls="nav-link")),
                                Li(A("Gallery", hx_get=f"/",cls="nav-link")),
                                Li(A("Components", hx_get=f"/",cls="nav-link")),
                                Li(A("Generative AI", hx_get=f"/",cls="nav-link")),
                                Li(A("Community", hx_get=f"/",cls="nav-link")),
                                Li(A("Docs", hx_get=f"/",cls="nav-link")),
                                Li(A("Blog", hx_get=f"/",cls="nav-link"))
                            )
                        ), cls="clearfix"
                    ), cls="page-header"
    )

    return header

def mk_content():
    content = Main(
               Div(
                    Table(
                        Tr(Td(B("A faster way to build and share web apps"))),
                        Tr(Td("Streamlit turns data scripts into shareable web apps in minutes")),
                        Tr(Td("All in pure Python. No front‑end experience required")),
                        Tr(Td(A("Try streamlit now", hx_get="/"),
                        A("Deploy on community cloud (it is free)", hx_get="/"))),
                        cls="text"
                    ),
                    Video(Source(src="https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4", type="video/mp4"),width="750px",controls="",autoplay="",loop="",muted="",cls="clip"),
                    cls="top-section clearfix"
               ),
               Section(
                    Div("Learn more:"),
                    A("Why Generative AI + Streamlit are a perfect match",hx_get="/"),
                    Div("Trusted by ",B("over 80% of Fortune 50"),"companies"),
                    Span("as of January 9th 2023"),
                    cls="second-section"
               ),
               Div(
                    Section(
                        H2("Get started in under a minute"),
                        Div("Streamlit’s",A("open-source ",hx_get="/"),"app framework is a breeze to get started with. Just choose your adventure:"),
                        
                        Div("And you're ready to go!")
                        
                    ),Div("or..."),
                    Div(
                        Div("Skip installation! Use Community Cloud"),
                        Ul(
                            Li("Code in a side-by-side browser editor"),
                            Li("Share instantly")
                        ),
                        Div(
                            A(
                                Img(src="images/git.svg",cls="git"),
                                "Sign up with Github"
                            )
                        )
                    )
                ),
               Section(
                    H2("Streamlit builds upon"),
                    Div(U("three simple principles")),
                    H2("Embrace scripting"),
                    Div("Build an app in a few lines of code with our",
                        A("magically simple API.", hx_get="/"), "Then see it automatically update as you iteratively save the source file."),
                    Div(
                            Div(
                                Img(Src="images/copy.svg",cls="copy-button",id="copy-button"), 
                                B(u'\u2705',cls="check",id="check"),
                                Pre(
                                    
                                    "import streamlit as st",
                                    "import pandas as pd",
                                    "",
                                    'st.write("""',
                                    "# My first app",
                                    "Hello *world!*",
                                    '"""")',
                                    "",
                                    "df = pd.read_csv('my_data.csv')",
                                    "st.line_chart(df)",
                                    cls="code-wrapper",id="code-wrapper"
                                ),cls="code-container"
                            )
                    ),
                    
                ),
                Div(
                    Img(src="images/d1.svg",cls="stats"),
                    Img(src="images/d2.svg",cls="stats")
                ),
                Script(src="javascript/script.js",type="text/javascript")
    ) 
    

    return content

serve()