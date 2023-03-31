import pandas as pd
import numpy as np

def schedule(appliance_data):
    df = csv_creator(appliance_data)
    columns = df.columns
    ratings = ratings_extractor(appliance_data)
    freq_dict = {}
    for i in columns[2:]:
        freq_dict[i] = (ratings[i], appliance_data[i]["duration"]//15)
    df = df.sort_values(by="MCP (Rs/kWh)*")
    df = df.reset_index()

    # Filling out first appliance's column
    initial_appliance = columns[2]
    for i in range(freq_dict[initial_appliance][1]):
        df[initial_appliance][i] = df["MCP (Rs/kWh)*"][i] * \
            freq_dict[initial_appliance][0]

    # Calling the actual algorithm
    processor(df, freq_dict)
    reconverter(df)

    # reconverting the first appliance manually
    for i in range(freq_dict[initial_appliance][1]):
        df[initial_appliance][i] = 1

    df.set_index("index", inplace=True)
    df = df.sort_values(by="index")
    df = df.to_dict('list')
    del df["MCP (Rs/kWh)*"]
    return df


def processor(mat, freq_dict):
    for col in range(4, len(mat.columns)):
        # print(mat.columns[col])
        mat[mat.columns[col]] = mat[mat.columns[col]] + mat[mat.columns[col-1]]
        costs_in_current_column = {}
        for j in range(len(mat[mat.columns[col]])):
            cost = mat[mat.columns[col]][j] + \
                mat["MCP (Rs/kWh)*"][j]*freq_dict[mat.columns[col]][0]
            if cost not in costs_in_current_column:
                # if the cost of this appliance for the current MCP (Rs/kWh)* is not in the costs_in_current_column dict
                # add that cost, and the value will be the index where its first entry is detected.
                costs_in_current_column[cost] = j
    # Now we start with filling process
    # costs is a sorted list containing sorted tuples of key value pairs of original costs_in_current_column dict.
    # c_iter iterates through the sorted list
    # itr iterates through the column. This will be changing its position as per the requirement of filling.
        costs = sorted(costs_in_current_column.items())
        c_itr = 0
        itr = costs[c_itr][1]
    # present_cost keeps track of the change in the cost while traversing.

        for _ in range(freq_dict[mat.columns[col]][1]):
            present_cost = mat[mat.columns[col]][itr] + \
                (mat["MCP (Rs/kWh)*"][itr]*freq_dict[mat.columns[col]][0])
            if present_cost != costs[c_itr][0] and c_itr < len(costs)-1:
                c_itr += 1
                itr = costs[c_itr][1]
            mat[mat.columns[col]][itr] = present_cost

            if itr < 95:
                itr += 1
            else:
                c_itr += 1
                itr = costs[c_itr][1]


def csv_creator(appliance_data):
    original_pricing = pd.read_csv(
        "https://raw.githubusercontent.com/Vidyutee/load_fetcher/main/data.csv")
    # new_cols = {}
    # for i in appliance_data.keys():
    #     data = [0]*96
    #     new_cols[i] = data
    columns = sorted(appliance_data.keys(),
                     key=lambda x: appliance_data[x]["rating"], reverse=True)
    mat = pd.DataFrame(np.zeros((96, len(columns))),
                       dtype="int", columns=columns)
    # cols = pd.DataFrame(mat)
    df = original_pricing.join(mat)
    return df


def ratings_extractor(appliance_data):
    ratings = {}
    for i in appliance_data.keys():
        ratings[i] = appliance_data[i]["rating"]
    return ratings


def reconverter(mat):
    for col in range(len(mat.columns) - 1, 3, -1):
        mat[mat.columns[col]] = mat[mat.columns[col]] - mat[mat.columns[col-1]]
        for j in range(len(mat[mat.columns[col]])):
            if mat[mat.columns[col]][j] != 0:
                mat[mat.columns[col]][j] = int(1)
            else:
                mat[mat.columns[col]][j] = int(0)


if __name__ == "__main__":
    print(schedule(
        {
            "Fridge": {
                "duration": 15,
                "rating": 0.12
            },
            "TV": {
                "duration": 45,
                "rating": 0.189
            },
            "Chocolate": {
                "duration": 60,
                "rating": 0.2
            },
            "PC": {
                "duration": 1425,
                "rating": 0.10
            },
        }
    ))
