import pandas as pd
import dateutil.parser

df = pd.read_csv("P6-40-correct.csv")#GT file

occurred_at = []
space_name = []
state = []

#save occurred_at timestamps to list
occurred_at_list = pd.to_datetime(df['occurred_at']).tolist()
#format occurred_at 
occurred_at_list = [t1.strftime("%d/%m/%Y %H:%M:%S") for t1 in occurred_at_list]

#assuming last 8 columns are space names
space_list = list((df[df.columns[-8:]]).columns.values)

#add space_name for each timestamps
for t in occurred_at_list:
    for s in space_list:
        occurred_at.append(t)
        space_name.append(s.lower().replace(" ", "_"))

#add state at each timestamp for each space
for index, row in df.iterrows():
    row_states = [row[s] for s in space_list]
    for r in row_states:
        state.append(r.upper())

#add occurred_at, space_name, state to df
new_df = pd.DataFrame(list(zip(occurred_at, space_name, state)),columns=['occurred_at','space_name', 'state'])

#write to csv
new_df.to_csv("m0_P6_2017-03-06.csv", index=False)

            
