import click
import spotify

@click.group()
def mycommands():
    pass

TIME = {
    "s": "short_term",  # approximately the last 4 weeks
    "m": "medium_term",  # approximately the last 6 months
    "l": "long_term"     # the entire data availability
}

@click.command()
@click.option('-l', '--limit', type=click.IntRange(1, 50), default=10, help="Number of top tracks to retrieve (default: 10)")
@click.option('-t', '--time-range', type=click.Choice(TIME.keys()), default="l", help="Time range for top tracks (s, m, l)")
def top(limit, time_range):
    if not spotify.create_table(TIME[time_range], limit):
        print("Couldn't generate your top tracks list right now. Give it another shot later or check your input.")

mycommands.add_command(top)

if __name__ == "__main__":
    mycommands()