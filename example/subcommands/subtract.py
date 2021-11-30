from psme.subcommand import BaseSubcommand

class Subtract(BaseSubcommand):
	def name(self):
		return "subtract"

	def register_args(self, subparser):
		subparser.add_argument("operand_one", type=int, help="First operand to subtract.")
		subparser.add_argument("operand_two", type=int, help="Second operand to subtract.")

	def run(self, args):
		print(f"{args.get('operand_one')} - {args.get('operand_two')} = {args.get('operand_one') - args.get('operand_two')}")