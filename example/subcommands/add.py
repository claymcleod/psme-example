from psme.subcommand import BaseSubcommand

class Add(BaseSubcommand):
	def name(self):
		return "add"

	def register_args(self, subparser):
		subparser.add_argument("operand_one", type=int, help="First operand to add together.")
		subparser.add_argument("operand_two", type=int, help="Second operand to add together.")

	def run(self, args):
		print(f"{args.get('operand_one')} + {args.get('operand_two')} = {args.get('operand_one') + args.get('operand_two')}")