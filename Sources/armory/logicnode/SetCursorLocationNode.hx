package armory.logicnode;

class SetCursorLocationNode extends LogicNode {

	public function new(tree: LogicTree) {
		super(tree);
	}

	override function run(from: Int) {
		#if (kha_krom)
		Krom.setMousePosition(0,inputs[1].get(),inputs[2].get());
		runOutput(0);
		#else
		trace("This platform doesn't support the setting of mouse cursor coordinates.");
		#end
	}
}
