import sys
from supabase_client import supabase, get_bands, get_modes, get_countries
from models import QSO
from rich.console import Console
from rich.table import Table
import datetime

console = Console()

# Función para registrar un nuevo QSO
def new_qso():
    console.print("[bold green]Registrando nuevo QSO...[/bold green]")
    
    # Obtener datos de las tablas de Supabase
    bands = get_bands()
    modes = get_modes()
    countries = get_countries()
    
    # Muestra las bandas disponibles
    console.print("\n[bold]Bandas disponibles:[/bold]")
    for idx, band in enumerate(bands.data, 1):
        console.print(f"{idx}. {band['name']}")
    
    # Selección de banda
    band_idx = int(input("\nSelecciona el número de banda: ")) - 1
    band = bands.data[band_idx]['name']
    
    # Muestra los modos disponibles
    console.print("\n[bold]Modos disponibles:[/bold]")
    for idx, mode in enumerate(modes.data, 1):
        console.print(f"{idx}. {mode['name']}")
    
    # Selección de modo
    mode_idx = int(input("\nSelecciona el número de modo: ")) - 1
    mode = modes.data[mode_idx]['name']
    
    # Muestra los países disponibles
    console.print("\n[bold]Países disponibles:[/bold]")
    for idx, country in enumerate(countries.data, 1):
        console.print(f"{idx}. {country['name']}")
    
    # Selección de país
    country_idx = int(input("\nSelecciona el número de país: ")) - 1
    country = countries.data[country_idx]['name']
    
    operator = input("Operador: ")
    signal_report = input("Reporte de señal: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    qso = QSO(band, mode, country, operator, date, signal_report)
    console.print(f"\nQSO registrado: {qso}")

    # Aquí podrías almacenar el QSO en Supabase si lo deseas

# Función para listar los QSOs registrados
def list_qsos():
    console.print("[bold blue]QSOs registrados:[/bold blue]")
    
    # Aquí podrías hacer una consulta a Supabase para obtener los QSOs almacenados
    # Actualmente solo los mostramos de ejemplo
    qsos = [
        QSO("20m", "SSB", "Argentina", "LU1XYZ", "2025-04-20 14:32", "59+10dB"),
        QSO("40m", "CW", "Brasil", "PY2ABC", "2025-04-20 15:00", "59")
    ]
    
    # Mostrar tabla de QSOs
    table = Table(title="Lista de QSOs")
    table.add_column("Band", justify="center")
    table.add_column("Mode", justify="center")
    table.add_column("Country", justify="center")
    table.add_column("Operator", justify="center")
    table.add_column("Date", justify="center")
    table.add_column("Signal Report", justify="center")
    
    for qso in qsos:
        table.add_row(qso.band, qso.mode, qso.country, qso.operator, qso.date, qso.signal_report)
    
    console.print(table)

# Función principal que maneja el CLI
def main():
    if len(sys.argv) < 2:
        console.print("[bold red]¡Debes especificar una acción! Usa 'new-qso' o 'list-qsos'.[/bold red]")
        sys.exit(1)
    
    action = sys.argv[1]
    
    if action == "new-qso":
        new_qso()
    elif action == "list-qsos":
        list_qsos()
    else:
        console.print("[bold red]Acción no válida. Usa 'new-qso' o 'list-qsos'.[/bold red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
