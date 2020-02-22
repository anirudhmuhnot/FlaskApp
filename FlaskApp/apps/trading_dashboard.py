from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash
from flask import send_from_directory
import time
import datetime
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
from os import listdir
import plotly.graph_objs as go
from start import app

start_date_daily = str('15-02-2018')
end_date_daily = str('15-02-2019')


def generate_table(dataframe, max_rows=20000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


layout = html.Div(className='animated zoomIn flow-text', children=[
    html.Center(html.H3('Trading Dashboard')),
    html.Center(html.H5('Adjust Parameters and click view. Set scrip to "All" to view all stocks.')),
    html.Br(),
    # display container, layouts are returned to this container
    html.Div(className='container', children=[
        html.Div(className='row', children=[
            html.Div(className='input-field col l4 m6 s12', children=[
                html.I(className="material-icons prefix", children=['date_range']),
                dcc.Input(id='inputddate-1', type='text', value=start_date_daily),
                html.Label(className='active', htmlFor='inputddate-1', children=['Start Date'])
            ]),

            html.Div(className='input-field col l4 m6 s12', children=[
                html.I(className="material-icons prefix", children=['date_range']),
                dcc.Input(id='inputddate-2', type='text', value=end_date_daily),
                html.Label(className='active', htmlFor='inputddate-2', children=['End Date'])
            ]),
            html.Div(className='input-field col l4 m6 s12', children=[
                html.I(className="material-icons prefix", children=['dehaze']),
                dcc.Input(id='n_rows', type='text', value=10),
                html.Label(className='active', htmlFor='n_rows', children=['No. of Rows'])
            ])
        ]),

        html.H6('Set Range for Open Interest and Price: '),
        html.Div(className='row', children=[
            html.Div(className='input-field col l3 m6 s12', children=[
                html.I(className="material-icons prefix", children=['expand_more']),
                dcc.Input(id='gt_oi', type='text', value=100),
                html.Label(className='active', htmlFor='gt_oi', children=['OI <'])
            ]),

            html.Div(className='input-field col l3 m6 s12', children=[
                html.I(className="material-icons prefix", children=['expand_less']),
                dcc.Input(id='lt_oi', type='text', value=0),
                html.Label(className='active', htmlFor='lt_oi', children=['OI >'])
            ]),

            html.Div(className='input-field col l3 m6 s12', children=[
                html.I(className="material-icons prefix", children=['expand_more']),
                dcc.Input(id='gt_price', type='text', value=100),
                html.Label(className='active', htmlFor='gt_price', children=['Price <'])
            ]),

            html.Div(className='input-field col l3 m6 s12', children=[
                html.I(className="material-icons prefix", children=['expand_less']),
                dcc.Input(id='lt_price', type='text', value=0),
                html.Label(className='active', htmlFor='lt_price', children=['Price >'])
            ]),
            html.Div(className='col s12 m6 l6', children=[
                html.H5(className='blue-text', children=['Sector: ']),
                dcc.Dropdown(
                    id='sector',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Automotive', 'value': 'Automotive'},
                        {'label': 'Banking & Financial Services', 'value': 'Banking & Financial Services'},
                        {'label': 'Cement & Construction', 'value': 'Cement & Construction'},
                        {'label': 'Chemicals', 'value': 'Chemicals'},
                        {'label': 'Conglomerates', 'value': 'Conglomerates'},
                        {'label': 'Consumer Non-durables', 'value': 'Consumer Non-durables'},
                        {'label': 'Engineering & Capital', 'value': 'Engineering & Capital'},
                        {'label': 'Food & Beverages', 'value': 'Food & Beverages'},
                        {'label': 'Information Technology', 'value': 'Information Technology'},
                        {'label': 'Manufacturing', 'value': 'Manufacturing'},
                        {'label': 'Media & Entertainment', 'value': 'Media & Entertainment'},
                        {'label': 'Metals & Mining', 'value': 'Metals & Mining'},
                        {'label': 'Miscellaneous', 'value': 'Miscellaneous'},
                        {'label': 'Oil & Gas', 'value': 'Oil & Gas'},
                        {'label': 'Pharmaceuticals', 'value': 'Pharmaceuticals'},
                        {'label': 'Retail & Real Estate', 'value': 'Retail & Real Estate'},
                        {'label': 'Services', 'value': 'Services'},
                        {'label': 'Telecommunication', 'value': 'Telecommunication'},
                        {'label': 'Tobacco', 'value': 'Tobacco'},
                        {'label': 'Utilities', 'value': 'Utilities'}
                    ],
                    value='All'
                )
            ]),
            html.Div(className='col s12 m6 l6',children=[
            html.H5(className='blue-text', children=['Scrip: ']),
            html.Div(className='input-field', children=[
                html.I(className="material-icons prefix", children=['expand_less']),
                dcc.Input(id='scrip', type='text', value='ONGC'),
                html.Label(className='active', htmlFor='scrip', children=['Scrip'])
                ])
            ]),
            html.Div(className = 'col l12 m12 s12 ',children=[
            html.Center(className='',children=[
                html.Div(className='input-field', children=[
                    html.Button(className='waves-effect waves-light btn', children=['View'], id='my-button-daily')
                    ])
                ])
            ])
        ])
    ]),
    html.Div(id='daily_dashboard', style={'display': 'block'}, children=[]),
    html.Center(html.H6(
        "*Works for stocks from Jan 5th 2016 to 15th Feburary 2019. Since the moneycontrol.com has made changes in their website, so web scraping is not active."))

])


@app.callback(
    Output('daily_dashboard', 'children'),
    [Input('my-button-daily', 'n_clicks')],
    [State('inputddate-1', 'value'), State('inputddate-2', 'value'), State('n_rows', 'value'), State('lt_oi', 'value'),
     State('gt_oi', 'value'), State('lt_price', 'value'), State('gt_price', 'value'), State('sector', 'value'),
     State('scrip', 'value')]
)
def update_output(n_clicks, start_date, end_date, n, lt_oi, gt_oi, lt_price, gt_price, sector, scrip):
    if n_clicks:
        n = int(n)
        lt_oi = int(lt_oi)
        gt_oi = int(gt_oi)
        lt_price = int(lt_price)
        gt_price = int(gt_price)
        if lt_oi == None:
            lt_oi = 100
        if gt_oi == None:
            gt_oi = 0
        if lt_price == None:
            lt_price = 100
        if gt_price == None:
            gt_price = 0

        if lt_oi > gt_oi:
            lt_oi = 100
            gt_oi = 0

        if lt_price > gt_price:
            lt_price = 100
            gt_price = 0

        OI_hist = pd.read_csv('./apps/data/trading_data/OI_hist.csv')
        OI_hist['Date'] = pd.to_datetime(OI_hist['Date'])
        OI_data_moneycontrol = pd.read_csv(
            './apps/data/trading_data/OI_data_moneycontrol.csv')
        sday, smonth, syear = int(str(start_date).split('-')[0]), int(str(start_date).split('-')[1]), int(
            str(start_date).split('-')[2])
        eday, emonth, eyear = int(str(end_date).split('-')[0]), int(str(end_date).split('-')[1]), int(
            str(end_date).split('-')[2])
        start_date = datetime.datetime(syear, smonth, sday)
        end_date = datetime.datetime(eyear, emonth, eday)
        OI_hist_select = OI_hist.loc[:, ['Scrip', 'Date', 'Close', 'Cumulative OI', 'Sector']]
        OI_data_mc_select = OI_data_moneycontrol.loc[:, ['Scrip', 'CMP', 'Cumulative OI', 'Sector']]
        OI_data_mc_select.columns = ["Scrip", "Close", "Cumulative OI", 'Sector']
        OI_data_mc_select['Date'] = datetime.date.today()
        OI_data_mc_select['Date'] = pd.to_datetime(OI_data_mc_select['Date'])
        OI_hist_mc_merged = OI_hist_select.append(OI_data_mc_select, ignore_index=True)
        OI_hist_mc_merged['Price Change %'] = OI_hist_mc_merged.groupby('Scrip')['Close'].apply(
            lambda x: x.pct_change())
        OI_hist_mc_merged['Price Change %'] = OI_hist_mc_merged['Price Change %'].apply(lambda x: x * 100)
        OI_hist_mc_merged['OI Change %'] = OI_hist_mc_merged.groupby('Scrip')['Cumulative OI'].apply(
            lambda x: x.pct_change())
        OI_hist_mc_merged['OI Change %'] = OI_hist_mc_merged['OI Change %'].apply(lambda x: x * 100)
        OI_hist_mc_merged['Date'] = pd.to_datetime(OI_hist_mc_merged['Date'])
        OI_hist_mc_filtered = OI_hist_mc_merged.loc[np.logical_and(OI_hist_mc_merged['Date'] >= start_date,
                                                                   OI_hist_mc_merged['Date'] <= end_date), :]
        OI_hist_mc_filtered = OI_hist_mc_filtered.dropna()
        OI_hist_mc_filtered.loc[:, 'OI Percentile'] = OI_hist_mc_filtered.groupby('Scrip')['OI Change %'].rank(
            pct=True).mul(100).round(2)
        OI_hist_mc_filtered.loc[:, 'Price Percentile'] = OI_hist_mc_filtered.groupby('Scrip', group_keys=False)[
            'Price Change %'].rank(pct=True).mul(100).round(2)
        OI_hist_mc_filtered = OI_hist_mc_filtered.groupby('Scrip').tail(1)
        if sector != 'All':
            OI_hist_mc_filtered = OI_hist_mc_filtered[OI_hist_mc_filtered['Sector'] == sector]
        if scrip != 'All':
            OI_hist_mc_filtered = OI_hist_mc_filtered[OI_hist_mc_filtered['Scrip'] == scrip]
        OI_hist_filtered = OI_hist_mc_filtered
        OI_hist_filtered1 = OI_hist_filtered[
            (OI_hist_filtered['Price Percentile'] >= lt_price) & (OI_hist_filtered['Price Percentile'] <= gt_price)]
        OI_hist_filtered2 = OI_hist_filtered[
            (OI_hist_filtered['OI Percentile'] >= lt_oi) & (OI_hist_filtered['OI Percentile'] <= gt_oi)]
        OI_latest2 = OI_hist_filtered2.sort_values('OI Percentile').reset_index(drop=True)
        OI_percentile_low = OI_latest2.loc[:, ['Scrip', 'OI Percentile', 'Date', 'Sector']].head(n)
        OI_latest2 = OI_hist_filtered2.sort_values('OI Percentile', ascending=False).reset_index(drop=True)
        OI_percentile_high = OI_latest2.loc[:, ['Scrip', 'OI Percentile', 'Date', 'Sector']].head(n)
        OI_latest1 = OI_hist_filtered1.sort_values('Price Percentile').reset_index(drop=True)
        price_percentile_low = OI_latest1.loc[:, ['Scrip', 'Price Percentile', 'Date', 'Sector']].head(n)
        OI_latest1 = OI_hist_filtered1.sort_values('Price Percentile', ascending=False).reset_index(drop=True)
        price_percentile_high = OI_latest1.loc[:, ['Scrip', 'Price Percentile', 'Date', 'Sector']].head(n)
        OI_hist_c = OI_hist_filtered[
            (OI_hist_filtered['Price Percentile'] >= lt_price) & (OI_hist_filtered['Price Percentile'] <= gt_price)]
        OI_hist_c1 = OI_hist_c[(OI_hist_c['OI Percentile'] >= lt_oi) & (OI_hist_c['OI Percentile'] <= gt_oi)]
        OI_hist_c = OI_hist_c1.loc[:, ['Scrip', 'Price Percentile', 'OI Percentile', 'Date']].head(n)
        OI_hist_c = OI_hist_c1.loc[:, ['Scrip', 'Price Percentile', 'OI Percentile', 'Date']].head(n)
        OI_hist_select = OI_hist.loc[:, ['Scrip', 'Date', 'Close', 'Cumulative OI']]
        OI_data_mc_select = OI_data_moneycontrol.loc[:, ['Scrip', 'CMP', 'Cumulative OI']]
        OI_data_mc_select.columns = ["Scrip", "Close", "Cumulative OI"]
        OI_data_mc_select['Date'] = datetime.date.today()
        OI_data_mc_select['Date'] = pd.to_datetime(OI_data_mc_select['Date'])
        merged = OI_hist_select.append(OI_data_mc_select, ignore_index=True)
        merged.sort_values(['Date', 'Scrip'])
        merged['Price Change %'] = merged.groupby('Scrip')['Close'].apply(lambda x: x.pct_change())
        merged['Price Change %'] = merged['Price Change %'].apply(lambda x: x * 100)

        merged['OI Change %'] = merged.groupby('Scrip')['Cumulative OI'].apply(lambda x: x.pct_change())
        merged['OI Change %'] = merged['OI Change %'].apply(lambda x: x * 100)

        filtered = merged.loc[np.logical_and(merged['Date'] >= start_date, merged['Date'] <= end_date), :]

        filtered = filtered.dropna()

        filtered.loc[:, 'OI Percentile'] = filtered.groupby('Scrip')['OI Change %'].rank(pct=True).mul(100)
        filtered.loc[:, 'Price Percentile'] = filtered.groupby('Scrip', group_keys=False)['Price Change %'].rank(
            pct=True).mul(100)

        change = filtered.loc[np.logical_and(np.logical_and(filtered['Scrip'] == scrip,
                                                            filtered['Date'] >= start_date),
                                             filtered['Date'] <= end_date), :].reset_index(drop=True)

        layout1 = html.Div(className='animated zoomIn', children=[
            html.Div(className='row', children=[
                html.Div(className='col s12 m6 l6 z-depth-2', children=[
                    html.H5(className='blue-text', children=['Top OI Percentile: ']),
                    html.Div([generate_table(OI_percentile_high)])
                ]),
                html.Div(className='col s12 m6 l6 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Least OI Percentile: ']),
                    html.Div([generate_table(OI_percentile_low)])
                ]),
                html.Hr(),
                html.Div(className='col s12 m6 l6 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Top Price Percentile: ']),
                    html.Div([generate_table(price_percentile_high)])
                ]),
                html.Div(className='col s12 m6 l6 z-depth-2', children=[
                    html.H5(className='blue-text', children=['Least Price Percentile: ']),
                    html.Div([generate_table(price_percentile_low)])
                ]),
                html.Hr(),
                html.Div(className='col s12 m12 l12 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Combined Price and OI: ']),
                    html.Div([generate_table(OI_hist_c)]),
                ])
            ])
        ])
        layout2 = html.Div(className='animated zoomIn', children=[
            html.Div(className='row', children=[

                html.Div(className='col s12 m6 l6 z-depth-2', children=[
                    html.H5(className='blue-text', children=['Top OI Percentile: ']),
                    html.Div([generate_table(OI_percentile_high)])
                ]),
                html.Div(className='col s12 m6 l6 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Least OI Percentile: ']),
                    html.Div([generate_table(OI_percentile_low)])
                ]),
                html.Hr(),
                html.Div(className='col s12 m6 l6 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Top Price Percentile: ']),
                    html.Div([generate_table(price_percentile_high)])
                ]),
                html.Div(className='col s12 m6 l6 z-depth-2', children=[
                    html.H5(className='blue-text', children=['Least Price Percentile: ']),
                    html.Div([generate_table(price_percentile_low)])
                ]),
                html.Hr(),
                html.Div(className='col s12 m12 l12 z-depth-1', children=[
                    html.H5(className='blue-text', children=['Combined Price and OI: ']),
                    html.Div([generate_table(OI_hist_c)]),
                ])
            ]),
            html.Div(className='col s12 m7 l12', children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=[
                            go.Line(
                                x=change['Date'],
                                y=change['Close'],
                                name='Close',
                            ),
                        ],
                        layout=go.Layout(
                            title='Close of ' + str(scrip),
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            xaxis=dict(
                                tickfont=dict(
                                    size=7,
                                    color='rgb(107, 107, 107)'
                                )
                            )
                        )
                    ),
                    id='my-graph1',
                    style={'height': '',
                           'width': '100%'
                           }
                )
            ]),
            html.Div(className='col s12 m7 l12', children=[
                dcc.Graph(
                    figure=go.Figure(
                        data=[
                            go.Bar(
                                x=change['Date'],
                                y=change['Cumulative OI'],
                                name='Cumulative OI',
                            )
                        ],
                        layout=go.Layout(
                            title='Cumulative OI of ' + str(scrip),
                            showlegend=True,
                            legend=go.layout.Legend(
                                x=0,
                                y=1.0
                            ),
                            xaxis=dict(
                                tickfont=dict(
                                    size=7,
                                    color='rgb(107, 107, 107)'
                                )
                            )
                        )
                    ),
                    id='my-graph',
                    style={'height': '',
                           'width': '100%'
                           }
                )
            ])

        ])

        if (scrip == 'All' or scrip == 'all' or scrip == 'all ' or scrip == 'All '):
            return layout1
        else:
            return layout2
