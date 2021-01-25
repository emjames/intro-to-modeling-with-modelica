import argparse
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pathlib
from .interactive import InteractiveLegend

parser = argparse.ArgumentParser(description='Plot Modelica results')


def plot_result(parent_dir, file_name, plot_vars = 'all'):
    # Make an image dir if it does not exist
    plots_dir = pathlib.Path(f'{parent_dir}/Plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    csv_path = f'{parent_dir}/{file_name}_res.csv'
    img_path = f'{plots_dir}/{file_name}.png'

    data = pd.read_csv(csv_path)

    fig, ax = plt.subplots()

    if plot_vars is not 'all':
        # Split to string list
        plot_vars_ = plot_vars.split(',')

        # Get the data to plot
        data = data[plot_vars_]

    for col in data.iloc[:,1:]:
        # X axis should always be the 0th col
        x = data[data.columns[0]]
        y = data[col]
        lbl = col
        ax.plot(x, y, label=lbl.title())

    plt.xlabel(data.columns[0].title())
    plt.grid()
    plt.legend()
    plt.savefig(f"{parent_dir}/Plots/{file_name}_{plot_vars.replace(',', '_')}.png")
    leg = InteractiveLegend()
    plt.show()


def main():
    # Get the arguments
    args = parser.parse_args()
    # Plot the results
    plot_result(args.file_path)


if __name__ == '__main__':
    # Parse the command line arguments
    parser.add_argument('file_path',
                        help='Specify the results file to plot',
                        type=str
                        )
    main()
