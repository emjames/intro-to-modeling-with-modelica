import argparse
import glob
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
    file_parent_dir = str(pathlib.Path(args.file_path).parent)
    # File name with extension
    file_name_ext = str(pathlib.Path(args.file_path).name)
    # File name alone
    file_name = str(file_name_ext.split('.')[0])

    # Run the Modelica compiler with arguments
    if args.action == 'compile':
        log(f'Compiling {args.file_path}...')

        log('===== OMC output BEGIN =====')
        subprocess.run(['omc',                  # OpenModelica compiler
                        '-s',                   # Simulate flag
                        '-d=initialization',
                        file_name_ext,
                        ],
                       cwd=file_parent_dir,     # Change working dir
                       )
        log('===== OMC output END =====')

        log('===== Makefile BEGIN =====')
        subprocess.run(['make', '-f', f'{file_name}.makefile'], cwd=file_parent_dir)
        log('===== Makefile END =====')


    elif args.action == 'clean':
        log('cleaning')
        # File extensions to keep
        file_ext_to_keep = ['*.mo', '*.csv', '*.mat']

        for ext in file_ext_to_keep:
            files = subprocess.check_output(['find', '.', '-type', 'f', '-name', ext],
                                            cwd=file_parent_dir).decode('utf-8')
            log(f'FILES: {str(files)}')

    elif args.action == 'run':
        log(f'Running: {file_name}')

        subprocess.run([
            f'./{file_name}',
            '-port=39279',
            '-logFormat=xmltcp',
            '-override=startTime=0,stopTime=2,stepSize=0.004,tolerance=1e-6,solver=dassl,outputFormat=csv',
        ], cwd=file_parent_dir)
    elif args.action == 'plot':
        log(f'Plotting results for {file_name}')
        plot_result(file_parent_dir, file_name)
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
                            'run',              # Run the compiled simulation
                        ],
                        )
    main()