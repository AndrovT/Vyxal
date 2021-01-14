codepage = "λ¬∧⟑∨⟇÷«»°\n․⍎½∆øÏÔÇæʀʁɾɽÞƈ∞⫙ß⎝⎠ !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~⎡⎣⨥⨪∺❝ð£¥§¦¡∂ÐřŠč√∖ẊȦȮḊĖẸṙ∑Ṡİ•\t"
codepage += "Ĥ⟨⟩ƛıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘŚśŜŝŞşšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽžſƀƁƂƃƄƅƆƇƊƋƌƍƎ¢≈Ωªº"

command_dict = {

    "!": ("stack.push(len(stack))", 0),
    '"': ("stack = iterable_shift(stack, ShiftDirections.RIGHT)", 0),
    "'": ("stack = iterable_shift(stack, ShiftDirections.LEFT)", 0),
    "$": ("top = pop(stack); over = pop(stack); stack += [top, over]", 2),
    "%": ("rhs, lhs = pop(stack, 2); stack.append(modulo(lhs, rhs))", 2),
    "*": ("rhs, lhs = pop(stack, 2); stack.append(multiply(lhs, rhs))", 2),
    "+": ("rhs, lhs = pop(stack, 2); stack.append(add(lhs, rhs))", 2),
    ",": ("VY_print(pop(stack)); printed = True", 1),
    "-": ("rhs, lhs = pop(stack, 2); stack.append(subtract(lhs, rhs))", 2),
    "/": ("rhs, lhs = pop(stack, 2); stack.append(divide(lhs, rhs))", 2),
    ":": ("temp = deref(pop(stack)); stack += [temp]*2", 1),
    "<": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN))", 2),
    ">": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN))", 2),
    "=": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.EQUALS))", 2),
    "?": ("stack.append(get_input())", 0),
    "A": ("stack.append(int(all(iterable(pop(stack)))))", 1),
    "B": ("stack.append(VY_int(pop(stack), 2))", 1),
    "C": ("stack.append(chrord(pop(stack)))", 1),
    "D": ("temp = deref(pop(stack)); stack += [temp]*3", 1),
    "E": ("stack.append(VY_eval(pop(stack)))", 1),
    "F": ("fn, vector = pop(stack, 2); stack.append(VY_filter(fn, vector))", 2),
    "G": ("stack.append(max(iterable(pop(stack))))", 1),
    "H": ("stack.append(VY_int(pop(stack), 16))", 1),
    "I": ("stack.append(VY_int(pop(stack)))", 1),
    "J": ("rhs, lhs = pop(stack, 2); stack.append(join(lhs, rhs))", 2),
    "K": ("stack.append(divisors_of(pop(stack)))", 1),
    "L": ("stack.append(len(iterable(pop(stack))))", 1),
    "M": ("fn, vector = pop(stack, 2); stack.append(VY_map(fn, vector))", 2),
    "N": ("stack.append(multiply(pop(stack), -1))", 1),
    "O": ("needle, haystack = pop(stack, 2); stack.append(iterable(haystack).count(needle))", 2),
    "P": ("rhs, lhs = pop(stack, 2); stack.append(str(lhs).strip(str(rhs)))", 2),
    "Q": ("exit()", 0),
    "R": ("fn, vector = pop(stack, 2); stack.append(VY_reduce(fn, vector))", 2),
    "S": ("stack.append(str(pop(stack)))", 1),
    "T": ("stack.append([n for n in pop(stack) if bool(n)])", 1),
    "U": ("stack.append(uniquify(pop(stack)))", 1),
    "V": ("replacement, needle, haystack = pop(stack, 3); stack.append(replace(haystack, needle, replacement))", 3),
    "W": ("stack = [deref(stack)]", 0),
    "X": ("context_level += 1", 0),
    "Y": ("rhs, lhs = pop(stack, 2); stack.append(interleave(lhs, rhs))", 2),
    "Z": ("rhs, lhs = pop(stack, 2); stack.append(Generator(zip(iterable(lhs), iterable(rhs))))", 2),
    "a": ("stack.append(int(any(iterable(pop(stack)))))", 1),
    "b": ("stack.append(VY_bin(pop(stack)))", 1),
    "c": ("rhs, lhs = pop(stack, 2); stack.append(int(lhs in interable(rhs)))", 2),
    "d": ("stack.append(multiply(pop(stack), 2))", 1),
    "e": ("rhs, lhs = pop(stack, 2); stack.append(exponate(lhs, rhs))", 2),
    "f": ("stack.append(flatten(iterable(pop(stack))))", 1),
    "g": ("stack.append(min(iterable(pop(stack))))", 1),
    "h": ("stack.append(iterable(pop(stack))[0])", 1),
    "i": ("rhs, lhs = pop(stack, 2); stack.append(iterable(lhs)[rhs])", 2),
    "j": ("rhs, lhs = pop(stack, 2); stack.append(str(lhs).join([str(x) for x in rhs]))", 2),
    "l": ("stack.append([])", 0),
    "m": ("item = pop(stack); stack.append(add(item, reverse(item)))", 1),
    "n": ("stack.append(context_values[context_level % len(context_values)])", 0),
    "o": ("needle, haystack = pop(stack, 2); stack.append(str(haystack).replace(str(needle)))", 2),
    "p": ("rhs, lhs = pop(stack, 2); stack.append(str(lhs).startswith(str(rhs)))", 2),
    "q": ("stack.append('`' + str(pop(stack)) + '`')", 1),
    "r": ("rhs, lhs = pop(stack, 2); stack.append(orderless_range(lhs, rhs))", 2),
    "s": ("stack.append(VY_sorted(pop(stack)))", 1),
    "t": ("stack.append(iterable(pop(stack))[-1])", 1),
    "u": ("stack.append(VY_sorted(uniquify(pop(stack))))", 1),
    "w": ("stack.append([pop(stack)])", 1),
    "x": ("context_level -= 1", 0),
    "y": ("stack += uninterleave(pop(stack))", 1),
    "z": ("fn, vector = pop(stack, 2); stack.append(VY_zipmap(fn, vector))", 2),
    "~": ("stack.append(random.randint(-32768, 32768))", 0),
    "¬": ("stack.append(int(not pop(stack)))", 1),
    "∧": ("rhs, lhs = pop(stack, 2); stack.append(lhs and rhs)", 2),
    "⟑": ("rhs, lhs = pop(stack, 2); stack.append(int(not (lhs and rhs)))", 2),
    "∨": ("rhs, lhs = pop(stack, 2); stack.append(lhs or rhs)", 2),
    "⟇": ("rhs, lhs = pop(stack, 2); stack.append(int(not (lhs or rhs)))", 2),
    "÷": ("for item in iterable(pop(stack)): stack.append(item)", 1),
    "⍎": ("fn = pop(stack); stack += fn(stack)", 1),
    "Ṛ": ("rhs, lhs = pop(stack, 2); stack.append(random.randint(lhs, rhs))", 2),
    "Ï": ("rhs, lhs = pop(stack, 2); stack.append(iterable(lhs).find(rhs))", 2),
    "Ô": ("stack.append(Generator(lambda x: (2 * (x - 1)) + 1))", 0),
    "∞": ("stack.append(Generator(lambda x: x))", 0),
    "Ç": ("stack.append(subtract(1, pop(stack)))", 1),
    "æ": ("stack.append(int(is_prime(pop(stack))))", 1),
    "ʀ": ("stack.append(Generator(range(0, int(add(pop(stack), 1)))))", 1),
    "ʁ": ("stack.append(Generator(range(0, int(pop(stack)))))", 1),
    "ɾ": ("stack.append(Generator(range(1, int(add(pop(stack), 1)))))", 1),
    "ɽ": ("stack.append(Generator(range(1, int(pop(stack)))))", 1),
    "Þ": ("tos = iterable(pop(stack)); stack.append(int(tos == tos[::-1]))", 1),
    "Ð": ("alphabet, number = pop(stack, 2); stack.append(utilities.to_ten(number, alphabet))", 2),
    "Š": ("alphabet, number = pop(stack, 2); stack.append(utilities.from_ten(number, alphabet))", 2),
    "ř": ("rhs, lhs = pop(stack, 2); stack.append(repeat(lhs, rhs))", 2),
    "∺": ("stack.append(modulo(pop(stack), 2))", 1),
    "⨥": ("stack.append(add(pop(stack), 1))", 1),
    "⨪": ("stack.append(subtract(pop(stack), 1))", 1),
    "Ĥ": ("stack.append(100)", 0),
    "Ĵ": ("stack.append(''.join([str(x) for x in pop(stack)]))", 1),
    "Ĳ": ("stack.append('\\n'.join([str(x) for x in pop(stack)]))", 1),
    "ĳ": ("stack.append(10)", 0),
    "ĵ": ("x = pop(stack); stack.append(multiply(x, x))", 1),
    "∑": ("stack.append(summate(pop(stack)))", 0),
    "Ķ": ("rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])", 2),
    "č": ("stack.append(int(pop(stack) != 1))", 1),
    "½": ("stack.append(divide(pop(stack), 2))", 1),
    "❝": ("stack.append('')", 0),
    "ð": ("stack.append(' ')", 0),
    "č": ("stack.append(pop(stack) != 1)", 1),
    "√": ("stack.append(exponate(pop(stack), 0.5))", 1),
    "∖": ("rhs, lhs = pop(stack, 2); stack.append(lhs // rhs)", 2),
    "Ẋ": ("rhs, lhs = pop(stack, 2); stack.append(int((lhs or rhs) and not (lhs and rhs)))", 2),
    "Ȧ": ("stack.append(abs(pop(stack)))", 1),
    "Ȯ": ("stack.append(oct(pop(stack)))", 1),
    "ĸ": ("value, vector = pop(stack, 2); stack.append(distribute(vector, value))", 2),
    "Ĺ": ("stack.append('\\n')", 0),
    "ĺ": ("stack.append(vertical_join(pop(stack)))", 1),
    "Ļ": ("padding, vector = pop(stack, 2); stack.append(vertical_join(vector, padding))", 2),
    "Ń": ("n, fn = pop(stack, 2); stack.append(first_n(fn, n))", 2),
    "ń": ("stack.append(first_n(pop(stack)))", 1),
    "Ň": ("stack.append(math.factorial(pop(stack)))", 1),
    "ņ": ("stack.appned(sums(iterable(pop(stack))))", 1),
    "≈": ("stack.append(int(len(set(iterable(pop(stack)))) == 1))", 1),
    "ň": ("stack.append(counts(pop(stack)))", 1),
    "ŉ": ("stack.append(reverse(pop(stack)))", 1),
    "Ŋ": ("stack.append(iterable(pop(stack), str)[:-1])", 1),
    "⎝": ("stack.append(min(pop(stack), key=lambda x: x[-1]))", 1),
    "⎠": ("stack.append(max(pop(stack), key=lambda x: x[-1]))", 1),
    "ŋ": ("stack = [summate(stack)]", 0),
    "Ō": ("stack.append(graded(pop(stack)))", 1),
    "ō": ("stack.append(reverse(graded(pop(stack))))", 1),
    "Ŏ": ("stack.append(None)", 0),
    "ŏ": ("vector, fn = pop(stack, 2); stack.append(indexes_where(fn, iterable(vector)))", 2),
    "Ő": ("vector, fn = pop(stack, 2); stack.append(VY_sorted(iterable, key=fn))", 2),
    "ő": ("register = pop(stack)", 1),
    "Œ": ("indexes, vector = pop(stack, 2); stack.append(indexed_into(iterable(vector), indexes))", 2),
    "œ": ("rhs, lhs = pop(stack, 2); stack.append(compare(modulo(lhs, rhs), 0, Comparitors.EQUALS))", 2),
    "Ŕ": ("rhs, lhs = pop(stack, 2); stack.append(vectorising_equals(lhs, rhs))", 2),
    "ŕ": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.NOT_EQUALS))", 2),
    "Ŗ": ("stack.append(register)", 0),
    "ŗ": ("rhs, lhs = pop(stack, 2); stack.append(iterable(lhs)[rhs:])", 2),
    "Ř": ("rhs, lhs = pop(stack, 2); stack.append(lshift(lhs, rhs))", 2),
    "Ś": ("rhs, lhs = pop(stack, 2); stack.append(rshift(lhs, rhs))", 2),
    "ś": ("rhs, lhs = pop(stack, 2); stack.append(bit_and(lhs, rhs))", 2),
    "Ŝ": ("rhs, lhs = pop(stack, 2); stack.append(bit_or(lhs, rhs))", 2),
    "ŝ": ("rhs, lhs = pop(stack, 2); stack.append(bit_xor(lhs, rhs))", 2),
    "Ş": ("stack.append(bit_not(pop(stack)))", 1),
    "ş": ("item, vector = pop(stack, 2); stack.append(prepend(iterable(vector), item))", 2),
    "š": ("item, index, vector = pop(stack, 3); stack.append(inserted(vector, item, index))", 3),
    "Ţ": ("stack.append(random.choice(iterable(pop(stack))))", 1),
    "ţ": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.LESS_THAN_EQUALS))", 2),
    "Ť": ("rhs, lhs = pop(stack, 2); stack.append(compare(lhs, rhs, Comparitors.GREATER_THAN_EQUALS))", 2),
    "ť": ("if len(stack) >= 2: stack.append(stack[-2])\nelse: stack.append(get_input())", 0),
    "Ŧ": ("value, index, vector = pop(stack, 3); stack.append(assigned(iterable(vector), index, value))", 3),
    "ŧ": ("stack.append(Generator(partition(pop(stack))))", 1),
    "Ũ": ("stack.append(Generator(itertools.permutation(iterable(pop(stack)))))", 1),
    "ũ": ("stack.append(integer_list(pop(stack)))", 1),
    "Ū": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[0:index])", 2),
    "ū": ("index, vector = pop(stack, 2); stack.append(iterable(vector)[1:index])", 2),
    "Ŭ": ("code = VyCompile(pop(stack)); exec(code);", 1),
    "ŭ": ("obj = iterable(pop(stack)); stack.append(Generator(range(1, len(obj) + 1)))", 1),
    "Ů": ("stack.append(group_consecutive(iterable(pop(stack))))", 1),
    "ů": ("string, new, original = pop(stack, 3); stack.append(transilterate(iterable(original), iterable(new), iterable(string)))", 3),
    "Ű": ("stack.append(truthy_indexes(pop(stack)))", 1),
    "ű": ("rhs, lhs = pop(stack, 2); stack.append(Generator(itertools.product(iterable(lhs), iterable(rhs))))", 2),
    "Ų": ("stack.append(deltas(pop(stack)))", 1),
    "ų": ("stack.append(sign_of(pop(stack)))", 1),
    "Ŵ": ("length, vector = pop(stack, 2); vector = iterable(vector)\nif type(vector) is str: vector = list(vector)\nstack.append(Generator(itertools.combinations(vector, length)))", 2),
    "ŵ": ("if inputs: stack.append([inputs])\nelse:\n    s, x = [], input()\n    while x:\n        s.append(Vy_eval(x)); x = input()", 0),
    "Ŷ": ("VY_print(stack[-1]); printed = True", 0),
    "ŷ": ("time.sleep(pop(stack))", 1),
    "Ÿ": ("transpose(iterable(pop(stack)))", 1),
    "Ź": ("obj = iterable(pop(stack)); stack.append(Generator(range(0, len(obj))))", 1),
    "ź": ("stack.append(input_values[input_level][0][-1])", 0),
    "Ż": ("rhs, lhs = pop(stack, 2); stack.append(split(lhs, rhs, True))", 2),
    "ż": ("rhs = pop(stack)\nif VY_type(rhs) in [list, Generator]: stack.append(gcd(rhs))\nelse: stack.append(gcd([pop(stack), rhs]))", 1),
    "ž": ("c, b, a = pop(stack, 3); stack.append(c); stack.append(a); stack.append(b)", 3),
    "ſ": ("fn, n = pop(stack, 2);\nfor _ in range(n):stack += fn(stack)", 2),
    "ƀ": ("""top = pop(stack)
if VY_type(top) is Number:
    limit = int(top)
else:
    limit = -1
vector, fn = pop(stack, 2)
stack.append(Generator(fn, limit=limit, initial=iterable(vector)))
""", 2)
}

math_command_dict = {
    "q": ("coeff_a, coeff_b = pop(stack, 2); stack.append(polynomial([coeff_a, coeff_b, 0]))", 2),
    "Q": ("coeff_b, coeff_c = pop(stack, 2); stack.append(polynomial([1, coeff_b, coeff_c]))", 2),
    "P": ("coeff = iterable(pop(stack)); stack.append(polynomial(coeff));", 1)
}