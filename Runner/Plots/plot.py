import argparse
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import pathlib

parser = argparse.ArgumentParser(description='Plot Modelica results')


def plot_result(parent_dir, file_name):
    # Make an image dir if it does not exist
    plots_dir = pathlib.Path(f'{parent_dir}/Plots')
    plots_dir.mkdir(parents=True, exist_ok=True)
    csv_path = f'{parent_dir}/{file_name}_res.csv'
    img_path = f'{plots_dir}/{file_name}.png'

    df = pd.read_csv(csv_path)

    fig, ax = plt.subplots()

    for col in list(df.columns[1:]):
        x = df[df.columns[0]]
        y = df[col]
        ax.plot(x, y)

    plt.grid()
    plt.savefig(img_path)
    plt.legend(df.columns[1:])
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
