import papermill as pm
import argparse 

def main(fechas):
    pm.execute_notebook('./Prueba1.ipynb',
                    './out/output-prueba1.ipynb',
                    parameters=dict(first_date=fechas[0],end_date=fechas[1])
    )

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument(
        'date',
        help='fecha inicio y fin',
        type=str
    )

    arguments = args.parse_args()

    main([i for i in arguments.date.split(',')])