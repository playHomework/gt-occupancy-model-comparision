import pandas as pd
import dateutil.parser

df = pd.read_csv("P6-40-correct.csv")

occurred_at_list = pd.to_datetime(df['occurred_at']).tolist()
occurred_at_list = [t1.strftime("%d/%m/%Y %H:%M:%S") for t1 in occurred_at_list]

space_list = list((df[df.columns[-8:]]).columns.values)

occurred_at = []
space_name = []

for t in occurred_at_list:
    for s in space_list:
        occurred_at.append(t)
        space_name.append(s.lower().replace(" ", "_"))

print len(occurred_at)
print len(space_name)

state = []

for index, row in df.iterrows():
    row_states = [row[s] for s in space_list]
    for r in row_states:
        state.append(r.upper())

new_df = pd.DataFrame(list(zip(occurred_at, space_name, state)),columns=['occurred_at','space_name', 'state'])

new_df.to_csv("m0_P6_2017-03-06.csv", index=False)

            
