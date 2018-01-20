# recursive permute

def permute(s):

    out = []

    if len(s) <= 1:
        return s
    else:

        # for every letter in string

        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 & Step 3
            for perm in permute( s[:i] + s[i+1:]):

                # add it to output
                #print(perm, let)
                out += [let+perm]

    return out

print(permute('abc'))