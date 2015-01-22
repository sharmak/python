input = dict()
input["bjvg"] = ["dict", "jane", "spot"]
input["hxsn"] = ["dict", "jane", "spot"]
input["pnetfn"] = ["yertle"]
input["qymm"] = ["puff"];
input["rqat"] = ["dict", "jane", "spot"]
input["xsb"]  = ["and"]
print input

input_list = input.keys()
def possible_solution(out_dict, s):
    out_char_dict = dict()
    for k, v in out_dict.iteritems():
        for i, j in zip(k, v):
            out_char_dict[i] = j
    pos = input[s]
    out = list()
    for pos_string in pos:
        found = True
        for i, j in zip(s, pos_string):
            if out_char_dict.has_key(i):
                val = out_char_dict[i]
                if val != j:
                    found = False
        if found:
            out.append(pos_string)
    return out
    

def solve(input_strings, out_dict):
    if len(input_strings) == 0 and len(out_dict) == len(input_list):
        print out_dict
        return
    else:
        pos_sol = possible_solution(out_dict, input_strings[0])
        for sol in pos_sol:
            out_dict[input_strings[0]] = sol
            solve(input_strings[1:], out_dict)
            del out_dict[input_strings[0]]
d = dict()
solve(input_list,d)

