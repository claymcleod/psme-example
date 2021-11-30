from psme.engine import Engine
from .subcommands.add import Add
from .subcommands.subtract import Subtract

def main():
	e = Engine(
		'psme-example',
		[Add(), Subtract()],
		description="Python subcommands made easy tutorial.")
	e.run()

if __name__ == "__main__":
	main()