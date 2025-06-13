# Install rich if not already installed:
# pip install rich
from rich.table import Table
from rich.console import Console

# Create a Console object
console = Console()
# Create a Table object
table = Table(title="User Table")
# Add columns
table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Email", style="green")
# Add rows
table.add_row("1", "Alice", "alice@example.com")
table.add_row("2", "Bob", "bob@example.com")
table.add_row("3", "Charlie", "charlie@example.com")

# Print the table to the console
console.print(table)
