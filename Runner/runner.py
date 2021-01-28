import argparse
import os
import pathlib
import subprocess
from Plots.plot import plot_result

parser = argparse.ArgumentParser(description='Compile Modelica files')


def log(s):
    print(s)


def main():
    args = parser.parse_args()

    # Breaker that checks if the path has an existing file
    if not pathlib.Path(args.file_path).is_file():
        log('File does not exist')
        return

    # Change the working dir to the file path's folder
    file_parent_dir = str(pathlib.Path(args.file_path).parent.resolve())
    # File name with extension
    file_name_with_ext = str(pathlib.Path(args.file_path).name)
    # File name alone
    file_name = str(file_name_with_ext.split('.')[0])

    # Run the Modelica compiler with arguments
    if args.action == 'compile':
        log(f'Compiling {args.file_path}...')

        log('===== OMC output BEGIN =====')
        subprocess.run(['omc',                  # OpenModelica compiler
                        '-s',                   # Simulation code generation flag
                        '-d=initialization',    # -d[ebug] mode. Show additional information from initialization
                        file_name_with_ext,
                        ],
                       cwd=file_parent_dir,     # Change working dir
                       )
        log('===== OMC output END =====')

        log('===== Makefile BEGIN =====')
        subprocess.run(['make', '-f', f'{file_name}.makefile'], cwd=file_parent_dir)
        log('===== Makefile END =====')

    elif args.action == 'clean':
        log(f'Cleaning: {file_parent_dir}')

        # File extensions to keep
        #file_ext_to_keep = ['.mo', '.csv', '.mat']
        # File extensions to remove
        file_ext_to_remove = ['.c', '.h', '.o', '.json', '.xml', '.makefile']

        # Find the files in the parent path that have the extension we want to remove
        files = {p.resolve() for p in pathlib.Path(file_parent_dir).glob(
            '**/*') if p.suffix in file_ext_to_remove}

        # Remove (unlink) the file(s)
        for f in files:
            f.unlink()
        # Remove the executable (it does not have an extension)
        pathlib.Path(f'{file_parent_dir}/{file_name}').unlink()

    elif args.action == 'simulate':
        log(f'Running: {file_name}')

        overrides = f'outputFormat=csv'
        if args.override:
            overrides = f'outputFormat=csv,{args.override}'
        log(f'Override: {overrides}')

        subprocess.run([
            f'./{file_name}',
            #'-override=startTime=0,stopTime=4,stepSize=0.004,tolerance=1e-6,solver=dassl,outputFormat=csv',
            f'-override={overrides}'
        ], cwd=file_parent_dir)
    elif args.action == 'plot':
        log(f'Plotting results for {file_name}')
        plot_result(file_parent_dir, file_name, args.variables)
    else:
        log('Unknown option')


if __name__ == '__main__':
    # Parse command line arguments
    # Read the file path of the Modelica file to compile
    parser.add_argument('file_path',
                        help='Modelica file path',
                        type=str,
                        )
    parser.add_argument('action',
                        help='Action to make on the path',
                        choices=[
                            'clean',            # Remove all but .mo and .csv/mat files
                            'compile',          # Compile the .mo file
                            'plot',             # Plot the result data file
                            'simulate',         # Run the compiled simulation
                        ],
                        )
    parser.add_argument('-o', '--override',
                        help='Override parameters for executable',
                        type=str,
                        )

    parser.add_argument('-v', '--variables',
                        help='CSV variables to plot (e.g. x,y,z)',
                        default='all',
                        type=str)
    main()
