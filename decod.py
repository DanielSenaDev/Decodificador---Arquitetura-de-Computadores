"""def transformar_16bits_string(codigo_entrada_str):
	codigo_16bits = codigo_entrada_str.zfill(16)
	return codigo_16bits

def def_opcode (codigo_16bits):
	opcode = ""
	opcode = codigo_16bits[0:4]
	return opcode

def instrucao (opcode):
	
	tipo_instrucao = "nenhuma instrucao registrada"

	if opcode == "0001":
		tipo_instrucao = "mov"
	elif opcode == "0010":
		tipo_instrucao = "add"
	elif opcode == "0000":
		tipo_instrucao = "none"

	return tipo_instrucao


def realizar_operacao (tipo_instrucao, codigo_16bits):
	rg1 = ""
	rg2 = ""
	resultado = []

	if tipo_instrucao == "mov":
		rg1 = codigo_16bits[4:10]
		rg2 = codigo_16bits[10:17]
		
	elif tipo_instrucao == "add":
		rg1 = codigo_16bits[4:10]
		rg2 = codigo_16bits[10:17]

	else:
		rg1 = codigo_16bits[4:10]
		rg2 = codigo_16bits[10:17]

	resultado.append(tipo_instrucao)
	resultado.append(rg1)
	resultado.append(rg2)

	return resultado




codigo_entrada = 0

while codigo_entrada != -1:
	
	print("\n----------\n")


	codigo_entrada = int(input("Digite o Codigo de Entrada em Binario(-1 para cancelar): ")) #entrada para números Binarios

	codigo_entrada_str = str(codigo_entrada)
	codigo_16bits = transformar_16bits_string(codigo_entrada_str)
	
	
	codigo_entrada_int = int(codigo_16bits,2)

	print("\n====\nDados entrada: ")
	print ("\nCodigo entrada Int:\t",codigo_entrada_int)
	print ("Codigo Em Bin:  \t",bin(codigo_entrada_int))
	print ("CODIGO 16 bits: \t",codigo_16bits)
	print("====")



	opcode = def_opcode(codigo_16bits)
	
	tipo_instrucao = instrucao(opcode)

	resultado_operacao = realizar_operacao(tipo_instrucao, codigo_16bits)
	
	
	print ("\nOPCODE: ",opcode)
	print ("Tipo da Instrução: \t", tipo_instrucao)
	print ("Registrador 1:     \t", resultado_operacao[1])
	print ("Registrador 2:     \t", resultado_operacao[2])
	
	print ("OPCODE RG1 RG2")
	print (opcode+" "+resultado_operacao[1]+" "+resultado_operacao[2])

	print ("\nInstrução RG1 RG2")
	print (tipo_instrucao+" "+resultado_operacao[1]+" "+resultado_operacao[2])
"""


def tipo_instrucao_funcao(opcode):
	instrucao = "none"
	if opcode == 1:
		instrucao = "mov"
	elif opcode == 2:
		instrucao = "add"
	else:
		instrucao = "none"

	return instrucao

def opcode_funcao(codigo):
	opcode_valor = codigo >> 12
	return (opcode_valor)

def registradores_funcao (codigo):
	codigo_base_rg1 = 4032		# = 0b0000111111000000
	codigo_base_rg2 = 63 		# = 0b0000000000111111

	rg1 = (codigo & codigo_base_rg1) >> 6
	rg2 = codigo & codigo_base_rg2

	return([rg1, rg2])

#16BITS
# 0000000000000000
#	OPCODE 	#REG1 	#REG2
#	0000 	000000 	000000
#inteiro 4161 = 0b0001000001000001'
#inteiro 8257 = 0b0010000001000001
# 61505= 0b1111000001000001


codigo_entrada = 0
while codigo_entrada != -1:

	print("\n----------\n")
	codigo_entrada = int(input("Digite o Codigo de Entrada em Inteiro(-1 para cancelar): "))
	if codigo_entrada == -1:
		print("\n----------\nFECHANDO PROGRAMA (-1)\n----------")
		break

	codigo_entrada_bin = bin(codigo_entrada)[2:].zfill(16)

	print("\n====\nDados entrada: ")
	print ("\nCodigo entrada Inteiro:\t",codigo_entrada)
	print ("Codigo entrada BIN:\t",codigo_entrada_bin)
	print ("Codigo entrada BIN:\t",codigo_entrada_bin[0:4]," ",codigo_entrada_bin[4:10]," ",codigo_entrada_bin[10:])

	
	print("\n====DECODIFICAÇÃO====")

	opcode = opcode_funcao(codigo_entrada)			
	tipo_instrucao = tipo_instrucao_funcao(opcode)
	registradores = registradores_funcao(codigo_entrada)
	rg1 = bin(registradores[0])[2:].zfill(6)
	rg2 = bin(registradores[1])[2:].zfill(6)

	
	print("\nOPCODE Inteiro:\t",opcode)
	print("OPCODE BIN:\t",bin(opcode)[2:].zfill(4))

	print("TIPO DA INSTRUCAO:", tipo_instrucao)


	print ("\nRegistrador 1 Inteiro:",registradores[0])
	print ("Registrador 1 BIN:",rg1)
	print ("Registrador 2 Inteiro:",registradores[1])
	print ("Registrador 2 BIN:",rg2)





	
