from dash import Dash, Input, Output, html, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.PULSE])

server = app.server

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("WITAJ NA STRONIE SUBSKRYBCJI NASZEGO SKLEPU!", style={"textAlign": "center"})
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/newsletter1.jpg", "img_style": {"max-height": "700px"}},
                    {"key": "2", "src": "/assets/newsletter2.jpg", "img_style": {"max-height": "700px"}},
                    {"key": "3", "src": "/assets/newsletter3.jpg", "img_style": {"max-height": "700px"}},
                ],
                controls=True,
                indicators=True,
                interval=2000,
                ride="carousel",
                className="carousel-fade"
            )
        ], width=8)
    ], justify="center"),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.H2("ZAPISZ SIĘ DO NEWSLETTERA!😊", style={"textAlign": "center"}),
            dbc.Container([
                dbc.FormFloating(
                    [
                        dbc.Input(id="name", placeholder="Enter name"),
                        dbc.Label("Enter name"),
                    ]
                ),
                dbc.FormFloating(
                    [
                        dbc.Input(id="email", placeholder="Enter e-mail"),
                        dbc.Label("Enter e-mail"),
                    ]
                ),
                dbc.Button(id="button1", children="Register Name"),
                dbc.Button(id="button2", children="Submit Application", className="ms-2"),
                html.Div(id="output_container", className="mt-4")
            ], fluid=True)
        ])
    ])
])


@app.callback(
    Output("output_container", "children"),
    [Input("button1", "n_clicks"), Input("button2", "n_clicks")],
    State("name", "value"),
    State("email", "value"),
    prevent_initial_call=True
)
def greet(button1_clicks, button2_clicks, name, email):
    if button1_clicks is not None:
        return f"Welcome {name}!" if name else "Please enter name"
    elif button2_clicks is not None:
        if name and email:
            return f"Your application has been submitted. Name: {name}, E-mail: {email}"
        else:
            return "Please enter name and e-mail"


if __name__ == '__main__':
    app.run_server(debug=True)
