operands = ['+','-','*','/','//','%']
for operand in operands:
    if operand == '//':
        print('// is a floor division operand')
        #continue
        break
    print(operand, 'is an operand')