import re, pyperclip

s = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(b),BinaryOp(/,BinaryOp(/,BinaryOp(*,Id(a),Id(f)),ArrayCell(Id(a),IntLiteral(0))),BinaryOp(/,BinaryOp(*,ArrayCell(Id(a),IntLiteral(1)),Id(b)),BinaryOp(*,BinaryOp(/,IntLiteral(1),IntLiteral(19090)),BinaryOp(*,BinaryOp(/,FloatLiteral(0.12),ArrayCell(Id(a),IntLiteral(7))),ArrayCell(Id(a),IntLiteral(2)))))))]))])"
varDecl_sub = re.sub(r'(VarDecl\()(\w+)', r'\1"\2"', s)
id_sub = re.sub(r'(Id\()(\w+)\)', r'\1"\2")', varDecl_sub)
type_sub = re.sub(r'([^Array]+Type)', r'\1()', id_sub)
array_type = re.sub(r'(ArrayType\()(\w+\(\)),(\d+)\)', r'\1\3,\2)', type_sub)
semi_sub = re.sub(r';', r',', array_type)
op_sub = re.sub(r'(<=|>=|!=|==|!|=|<|>|\+|\-|\*|\/|%|&&|\|\|)', r'"\1"',
                semi_sub)
string_lit = re.sub(r'(StringLiteral\()([\w|\s|:]+)(\W)', r'\1"\2"\3', op_sub)
true_ = re.sub(r'true', r'True', string_lit)
false_ = re.sub(r'false', r'False', true_)
array_pointer = re.sub(r'ArrayTypePointer', r'ArrayPointerType', false_)
pyperclip.copy(array_pointer)
