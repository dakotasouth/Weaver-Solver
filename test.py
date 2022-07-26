from solver import solve
def main():
    wordPairs = [
    ['rain', 'snow', 6, ['rain', 'cain', 'chin', 'chon', 'chow', 'show', 'snow']],
    ['type', 'word', 4, ['type', 'tope', 'tore', 'wore', 'word']],
    ['open', 'shut', 6, ['open', 'oped', 'ohed', 'shed', 'shad', 'shat', 'shut']],
    ['ball', 'cube', 5, ['ball', 'bale', 'bake', 'cake', 'cuke', 'cube']],
    ['rock', 'dust', 4, ['rock', 'dock', 'duck', 'duct', 'dust']],
    ['poor', 'rich', 6, ['poor', 'boor', 'book', 'bock', 'rock', 'rick', 'rich']],
    ['monk', 'pray', 6, ['monk', 'mons', 'moas', 'boas', 'bras', 'bray', 'pray']],
    ['beer', 'wine', 5, ['beer', 'bees', 'bens', 'bene', 'bine', 'wine']],
    ['hide', 'seek', 6, ['hide', 'bide', 'bids', 'beds', 'bees', 'sees', 'seek']],
    ['tree', 'bark', 5, ['tree', 'tyee', 'tyre', 'byre', 'bare', 'bark']],
    ['taco', 'meat', 6, ['taco', 'tace', 'mace', 'male', 'malt', 'melt', 'meat']],
    ['slow', 'poke', 6, ['slow', 'plow', 'plod', 'pood', 'pond', 'pone', 'poke']],
    ['door', 'jamb', 6, ['door', 'doer', 'does', 'doms', 'dams', 'jams', 'jamb']],
    ['text', 'call', 5, ['text', 'teat', 'teal', 'tell', 'cell', 'call']],
    ['mind', 'soul', 6, ['mind', 'bind', 'bins', 'sins', 'sons', 'sous', 'soul']],
    ['lose', 'find', 4, ['lose', 'lone', 'line', 'fine', 'find']],
    ['gala', 'fete', 4, ['gala', 'gale', 'gate', 'fate', 'fete']],
    ['flat', 'tire', 6, ['flat', 'blat', 'boat', 'bort', 'bore', 'tore', 'tire']],
    ['pork', 'chop', 4, ['pork', 'cork', 'cook', 'coop', 'chop']],
    ['pink', 'blue', 7, ['pink', 'fink', 'fins', 'fens', 'feus', 'flus', 'flue', 'blue']],
    ['jail', 'free', 6, ['jail', 'bail', 'bait', 'brit', 'brie', 'bree', 'free']],
    ['frog', 'toad', 4, ['frog', 'trog', 'trod', 'trad', 'toad']],
    ['goof', 'ball', 5, ['goof', 'golf', 'gold', 'bold', 'bald', 'ball']],
    ['cole', 'slaw', 6, ['cole', 'bole', 'bolt', 'boat', 'blat', 'blaw', 'slaw']],
    ['dish', 'bowl', 5, ['dish', 'diss', 'doss', 'boss', 'bows', 'bowl']],
    ['bath', 'soap', 6, ['bath', 'bach', 'back', 'bock', 'sock', 'soak', 'soap']],
    ['wild', 'tame', 4, ['wild', 'wile', 'tile', 'tale', 'tame']],
    ['life', 'boat', 5, ['life', 'lift', 'loft', 'coft', 'coat', 'boat']],
    ['good', 'luck', 5, ['good', 'goof', 'loof', 'look', 'lock', 'luck'], '🍀', "Saint Patrick's Day", 'green'], # 3/17/2022 -- Saint Patrick's Day
    ['papa', 'bear', 5, ['papa', 'paps', 'peps', 'peas', 'pear', 'bear']],
    ['thin', 'mint', 6, ['thin', 'than', 'that', 'teat', 'tent', 'tint', 'mint']],
    ['what', 'ever', 7, ['what', 'that', 'thae', 'thee', 'tyee', 'tyer', 'eyer', 'ever']],
    ['slow', 'down', 5, ['slow', 'slot', 'soot', 'soon', 'sown', 'down']],
    ['hush', 'yell', 5, ['hush', 'husk', 'hulk', 'hull', 'hell', 'yell']],
    ['rock', 'sand', 4, ['rock', 'rack', 'rank', 'rand', 'sand']],
    ['fish', 'hook', 5, ['fish', 'fist', 'hist', 'host', 'hoot', 'hook']],
    ['solo', 'team', 5, ['solo', 'sols', 'sels', 'seas', 'seam', 'team']],
    ['town', 'city', 6, ['town', 'torn', 'corn', 'core', 'cire', 'cite', 'city']],
    ['atom', 'cell', 7, ['atom', 'atop', 'stop', 'step', 'seep', 'seel', 'sell', 'cell']],
    ['punt', 'kick', 4, ['punt', 'pint', 'pink', 'kink', 'kick']],
    ['camp', 'fire', 4, ['camp', 'came', 'care', 'cire', 'fire']],
    ['lies', 'fact', 5, ['lies', 'pies', 'pics', 'pacs', 'pact', 'fact']],
    ['peat', 'moss', 4, ['peat', 'meat', 'moat', 'moas', 'moss']],
    ['fool', 'joke', 5, ['fool', 'fowl', 'howl', 'howe', 'hoke', 'joke'], '🥸', "April Fool's Day", 'purple'], # 4/1/2022 -- April Fool's Day
    ['free', 'love', 6, ['free', 'tree', 'tyee', 'tyne', 'tone', 'lone', 'love']],
    ['home', 'brew', 7, ['home', 'come', 'cole', 'cold', 'coed', 'cred', 'bred', 'brew']],
    ['soft', 'firm', 4, ['soft', 'sort', 'fort', 'form', 'firm']],
    ['head', 'foot', 5, ['head', 'bead', 'beat', 'boat', 'boot', 'foot']],
    ['full', 'moon', 4, ['full', 'mull', 'moll', 'mool', 'moon']],
    ['slip', 'fall', 5, ['slip', 'flip', 'flir', 'fair', 'fail', 'fall']],
    ['home', 'sick', 5, ['home', 'dome', 'dime', 'dice', 'dick', 'sick']],
    ['palm', 'tree', 6, ['palm', 'pale', 'pare', 'pyre', 'tyre', 'tyee', 'tree']],
    ['over', 'come', 7, ['over', 'oyer', 'dyer', 'doer', 'does', 'doms', 'dome', 'come']],
    ['cows', 'milk', 4, ['cows', 'cols', 'mols', 'mils', 'milk']],
    ['neck', 'lace', 4, ['neck', 'beck', 'back', 'lack', 'lace']],
    ['news', 'cast', 5, ['news', 'mews', 'maws', 'mass', 'mast', 'cast']],
    ['page', 'book', 5, ['page', 'pace', 'pack', 'back', 'bock', 'book']],
    ['pray', 'amen', 7, ['pray', 'gray', 'grad', 'grid', 'arid', 'amid', 'amin', 'amen'], '🙏', "Good Friday and Passover (first day)", 'blue'], # 4/15/2022 -- Good Friday and Passover (first day)
    ['pawn', 'king', 5, ['pawn', 'paws', 'pans', 'pang', 'ping', 'king']],
    ['hide', 'eggs', 6, ['hide', 'aide', 'aids', 'ands', 'ends', 'engs', 'eggs'], '🐰', "Easter", 'pink'], # Sunday, 4/17/2022 -- Easter
    ['less', 'more', 4, ['less', 'loss', 'lose', 'lore', 'more']],
    ['soul', 'mate', 5, ['soul', 'saul', 'maul', 'mall', 'male', 'mate']],
    ['moon', 'star', 5, ['moon', 'boon', 'boor', 'boar', 'soar', 'star']],
    ['tiny', 'huge', 5, ['tiny', 'liny', 'line', 'lune', 'luge', 'huge']],
    ['root', 'tree', 4, ['root', 'toot', 'trot', 'tret', 'tree'], '🌎', "Earth Day", 'blue'], # 4/22/2022 -- Earth Day
    ['four', 'wine', 6, ['four', 'dour', 'dorr', 'dore', 'dire', 'dine', 'wine'], '🍷', "Passover (last day)", 'blue'], # 4/23/2022 -- Passover (last day)
    ['long', 'shot', 6, ['long', 'bong', 'bonk', 'book', 'boot', 'soot', 'shot']],
    # Monday
    ['hold', 'fast', 4, ['hold', 'holt', 'halt', 'hast', 'fast']],
    ['time', 'warp', 4, ['time', 'tame', 'tamp', 'tarp', 'warp']],
    ['tree', 'fort', 5, ['tree', 'tres', 'toes', 'tors', 'tort', 'fort']],
    ['bird', 'song', 4, ['bird', 'bind', 'bond', 'bong', 'song']],
    ['left', 'turn', 5, ['left', 'loft', 'toft', 'tort', 'torn', 'turn']],
    ['sink', 'swim', 6, ['sink', 'sank', 'sand', 'said', 'skid', 'skim', 'swim']],
    ['game', 'over', 7, ['game', 'gams', 'gaes', 'kaes', 'kyes', 'oyes', 'oyer', 'over']],
    # Monday
    ['lost', 'soul', 4, ['lost', 'lout', 'loup', 'soup', 'soul']],
    ['mind', 'game', 4, ['mind', 'mine', 'mane', 'gane', 'game']],
    ['shoe', 'sock', 4, ['shoe', 'shot', 'soot', 'sook', 'sock']],
    ['long', 'haul', 5, ['long', 'hong', 'hang', 'hant', 'haut', 'haul']],
    ['move', 'fast', 5, ['move', 'cove', 'cave', 'case', 'cast', 'fast']],
    ['wolf', 'pack', 6, ['wolf', 'rolf', 'role', 'pole', 'pale', 'pace', 'pack']],
    ['four', 'five', 6, ['four', 'dour', 'dorr', 'dore', 'dire', 'dive', 'five']],
    # Monday
    ['bank', 'roll', 4, ['bank', 'balk', 'ball', 'boll', 'roll']],
    ['junk', 'food', 4, ['junk', 'funk', 'fund', 'fond', 'food']],
    ['nice', 'easy', 5, ['nice', 'bice', 'bise', 'base', 'ease', 'easy']],
    ['lock', 'keys', 5, ['lock', 'lack', 'lacs', 'lays', 'kays', 'keys']],
    ['film', 'noir', 6, ['film', 'fill', 'bill', 'boll', 'boil', 'noil', 'noir']],
    ['talk', 'chat', 6, ['talk', 'calk', 'cask', 'cast', 'cost', 'coat', 'chat']],
    ['milk', 'eggs', 7, ['milk', 'mils', 'ails', 'aids', 'ands', 'ends', 'engs', 'eggs']],
    # Monday
    ['rise', 'fall', 4, ['rise', 'rile', 'file', 'fill', 'fall']],
    ['give', 'take', 4, ['give', 'dive', 'dike', 'tike', 'take']],
    ['foot', 'mile', 4, ['foot', 'moot', 'molt', 'milt', 'mile']],
    ['team', 'mate', 5, ['team', 'teas', 'tets', 'tats', 'mats', 'mate']],
    ['surf', 'wave', 5, ['surf', 'curf', 'cure', 'care', 'cave', 'wave']],
    ['quiz', 'test', 6, ['quiz', 'quit', 'duit', 'doit', 'dost', 'tost', 'test']],
    
    ['high', 'jump', 7, ['high', 'sigh', 'sinh', 'sins', 'sims', 'simp', 'jimp', 'jump']],
    # Monday
    ['fail', 'pass', 4, ['fail', 'fall', 'pall', 'pals', 'pass']],
    ['lion', 'tame', 4, ['lion', 'limn', 'lime', 'lame', 'tame']],
    ['note', 'book', 4, ['note', 'none', 'bone', 'bonk', 'book']],
    ['fist', 'bump', 5, ['fist', 'list', 'lisp', 'limp', 'lump', 'bump']],
    ['sumo', 'ring', 5, ['sumo', 'sums', 'rums', 'rims', 'rins', 'ring']],
    ['sunk', 'ship', 6, ['sunk', 'dunk', 'dunt', 'duit', 'suit', 'shit', 'ship']],
    ['nose', 'swab', 7, ['nose', 'hose', 'host', 'hest', 'heat', 'seat', 'swat', 'swab']],
    # Monday
    ['done', 'deal', 4, ['done', 'dene', 'dele', 'dell', 'deal']],
    ['wolf', 'howl', 4, ['wolf', 'woof', 'hoof', 'howf', 'howl']],
    ['bear', 'claw', 4, ['bear', 'beam', 'blam', 'blaw', 'claw']],
    ['pump', 'fake', 5, ['pump', 'dump', 'damp', 'dame', 'fame', 'fake']],
    ['code', 'hack', 5, ['code', 'cade', 'care', 'cark', 'hark', 'hack']],
    ['gosh', 'darn', 6, ['gosh', 'bosh', 'bash', 'base', 'bare', 'barn', 'darn']],
    ['kilo', 'gram', 7, ['kilo', 'kill', 'gill', 'gild', 'gold', 'goad', 'grad', 'gram']],
    # Monday
    ['coal', 'fire', 5, ['coal', 'foal', 'foam', 'form', 'firm', 'fire']],
    ['jump', 'rope', 5, ['jump', 'pump', 'pomp', 'pome', 'pope', 'rope']],
    ['lose', 'gain', 5, ['lose', 'lase', 'last', 'gast', 'gait', 'gain']],
    ['nick', 'name', 5, ['nick', 'dick', 'dice', 'dace', 'dame', 'name']],
    ['farm', 'oink', 5, ['farm', 'fare', 'fane', 'fine', 'fink', 'oink']],
    ['door', 'knob', 6, ['door', 'boor', 'boob', 'blob', 'slob', 'snob', 'knob']],
    ['mint', 'chip', 7, ['mint', 'dint', 'dunt', 'duit', 'suit', 'shit', 'chit', 'chip']],
    # Monday
    ['head', 'toes', 4, ['head', 'heed', 'hoed', 'hoes', 'toes']],
    ['duck', 'pond', 5, ['duck', 'buck', 'bock', 'bonk', 'bond', 'pond']],
    ['sail', 'boat', 5, ['sail', 'bail', 'baal', 'baas', 'boas', 'boat']],
    ['beta', 'test', 5, ['beta', 'bets', 'bees', 'beet', 'best', 'test']],
    ['tilt', 'spin', 6, ['tilt', 'silt', 'salt', 'sall', 'sail', 'sain', 'spin']],
    ['left', 'over', 6, ['left', 'deft', 'deet', 'deer', 'dyer', 'oyer', 'over']],
    ['acid', 'base', 7, ['acid', 'arid', 'grid', 'grit', 'brit', 'bait', 'bast', 'base']],
    # Monday
    ['long', 'time', 4, ['long', 'ling', 'line', 'lime', 'time']],
    ['solo', 'duet', 5, ['solo', 'sols', 'dols', 'does', 'dues', 'duet']],
    ['born', 'free', 6, ['born', 'bore', 'byre', 'tyre', 'tyee', 'tree', 'free']],
    ['show', 'tell', 6, ['show', 'shaw', 'sham', 'seam', 'seal', 'sell', 'tell']],
    ['slow', 'fast', 6, ['slow', 'flow', 'flaw', 'flat', 'feat', 'fest', 'fast']],
    ['skim', 'milk', 6, ['skim', 'skis', 'seis', 'sels', 'mels', 'mils', 'milk']],
    ['null', 'void', 7, ['null', 'cull', 'curl', 'curd', 'cord', 'lord', 'loid', 'void']],
    # Monday
    ['oust', 'outs', 4, ['oust', 'bust', 'buss', 'buts', 'outs']],
    ['zone', 'mark', 5, ['zone', 'bone', 'bane', 'bank', 'bark', 'mark']],
    ['rack', 'city', 5, ['rack', 'pack', 'pacy', 'paty', 'pity', 'city']],
    ['play', 'ball', 6, ['play', 'plan', 'pian', 'pial', 'pill', 'bill', 'ball']],
    ['swan', 'lake', 7, ['swan', 'span', 'spas', 'seas', 'leas', 'leks', 'leke', 'lake']],
    ['baby', 'step', 7, ['baby', 'gaby', 'gabs', 'gaes', 'gees', 'sees', 'seep', 'step']],
    ['crab', 'cake', 7, ['crab', 'crap', 'crop', 'coop', 'comp', 'camp', 'came', 'cake']],
    # Monday
    ['main', 'road', 5, ['main', 'lain', 'laid', 'loid', 'load', 'road']],
    ['vote', 'veto', 5, ['vote', 'rote', 'rete', 'rets', 'vets', 'veto']],
    ['lazy', 'loaf', 6, ['lazy', 'lacy', 'lack', 'lock', 'look', 'loof', 'loaf']],
    ['cold', 'play', 6, ['cold', 'bold', 'bolt', 'boat', 'blat', 'plat', 'play']],
    ['thug', 'life', 7, ['thug', 'thus', 'taus', 'tams', 'lams', 'lame', 'lime', 'life']],
    ['crab', 'cake', 7, ['crab', 'crap', 'crop', 'coop', 'comp', 'camp', 'came', 'cake']],
    ['quag', 'mire', 7, ['quag', 'quad', 'duad', 'dual', 'dial', 'dirl', 'dire', 'mire']],
    # Monday
    ['halo', 'ring', 5, ['halo', 'halt', 'hant', 'hang', 'rang', 'ring']],
    ['junk', 'mail', 5, ['junk', 'hunk', 'hank', 'haik', 'hail', 'mail']],
    ['tuna', 'fish', 6, ['tuna', 'luna', 'lunt', 'lint', 'list', 'fist', 'fish']],
    ['stag', 'solo', 6, ['stag', 'skag', 'skas', 'seas', 'sels', 'sols', 'solo']],
    ['hunk', 'stud', 7, ['hunk', 'huns', 'hues', 'hued', 'sued', 'sped', 'spud', 'stud']],
    ['wish', 'star', 7, ['wish', 'fish', 'fist', 'fest', 'feat', 'fear', 'sear', 'star']],
    ['stop', 'sign', 8, ['stop', 'step', 'seep', 'sees', 'sets', 'sits', 'sith', 'sigh', 'sign']],
    # Monday
    ['road', 'trip', 4, ['road', 'toad', 'trad', 'trap', 'trip']],
    ['gold', 'dust', 5, ['gold', 'bold', 'bolt', 'dolt', 'dost', 'dust']],
    ['ants', 'hill', 5, ['ants', 'aits', 'ails', 'fils', 'fill', 'hill']],
    ['cold', 'snow', 5, ['cold', 'colt', 'coot', 'soot', 'snot', 'snow']],
    ['when', 'ever', 6, ['when', 'then', 'thee', 'tyee', 'tyer', 'eyer', 'ever']],
    ['hand', 'soap', 6, ['hand', 'haed', 'hoed', 'hoer', 'hoar', 'soar', 'soap']],
    ['exit', 'ramp', 9, ['exit', 'emit', 'smit', 'shit', 'shin', 'sain', 'rain', 'rais', 'rams', 'ramp']],
    # Monday
    ['dawn', 'dusk', 4, ['dawn', 'dawk', 'dank', 'dunk', 'dusk']],
    ['blog', 'post', 5, ['blog', 'blot', 'boot', 'bort', 'port', 'post']],
    ['with', 'hold', 5, ['with', 'wite', 'wile', 'wild', 'wold', 'hold']],
    ['keep', 'lose', 5, ['keep', 'keet', 'leet', 'lest', 'lost', 'lose']],
    ['true', 'love', 6, ['true', 'tree', 'tyee', 'tyne', 'tone', 'lone', 'love']],
    ['area', 'code', 6, ['area', 'ares', 'tres', 'toes', 'tods', 'cods', 'code']],
    ['iamb', 'poet', 7, ['iamb', 'gamb', 'gamp', 'gasp', 'gast', 'past', 'post', 'poet']],
    # Monday
    ['dogs', 'bark', 4, ['dogs', 'bogs', 'bags', 'bars', 'bark']],
    ['fear', 'calm', 5, ['fear', 'feal', 'fell', 'cell', 'call', 'calm']],
    ['high', 'note', 5, ['high', 'sigh', 'sith', 'site', 'nite', 'note']],
    ['oaky', 'wine', 5, ['oaky', 'caky', 'cake', 'cane', 'cine', 'wine']],
    ['jean', 'gene', 5, ['jean', 'bean', 'bead', 'bend', 'bene', 'gene']],
    ['even', 'keel', 6, ['even', 'eves', 'eyes', 'pyes', 'pees', 'peel', 'keel']],
    ['nigh', 'near', 7, ['nigh', 'sigh', 'sith', 'sits', 'sets', 'seas', 'sear', 'near']],
    # Monday
    ['josh', 'joke', 4, ['josh', 'posh', 'pose', 'poke', 'joke']],
    ['trap', 'door', 5, ['trap', 'trop', 'prop', 'poop', 'poor', 'door']],
    ['vale', 'veil', 5, ['vale', 'bale', 'ball', 'bail', 'vail', 'veil']],
    ['math', 'whiz', 5, ['math', 'matt', 'watt', 'wait', 'whit', 'whiz']],
    ['wham', 'boom', 6, ['wham', 'cham', 'chat', 'coat', 'boat', 'boot', 'boom']],
    ['very', 'much', 6, ['very', 'vary', 'vars', 'mars', 'macs', 'mach', 'much']],
    ['stay', 'woke', 7, ['stay', 'stat', 'seat', 'sent', 'sene', 'sone', 'soke', 'woke']],
    # Monday
    ['soft', 'ware', 4, ['soft', 'sort', 'sore', 'wore', 'ware']],
    ['folk', 'song', 4, ['folk', 'holk', 'honk', 'hong', 'song']],
    ['rain', 'drop', 5, ['rain', 'gain', 'grin', 'grip', 'drip', 'drop']],
    ['grok', 'know', 5, ['grok', 'grow', 'glow', 'slow', 'snow', 'know']],
    ['palm', 'read', 5, ['palm', 'halm', 'helm', 'held', 'head', 'read']],
    ['gnaw', 'bite', 6, ['gnaw', 'gnat', 'goat', 'boat', 'bott', 'bitt', 'bite']],
    ['verb', 'noun', 7, ['verb', 'herb', 'hern', 'horn', 'born', 'boon', 'noon', 'noun']],
    # Monday
    ['gold', 'leaf', 4, ['gold', 'goad', 'load', 'lead', 'leaf']],
    ['yoke', 'yolk', 4, ['yoke', 'hoke', 'hole', 'holk', 'yolk']],
    ['half', 'moon', 5, ['half', 'hall', 'mall', 'moll', 'mool', 'moon']],
    ['gene', 'pool', 5, ['gene', 'gens', 'pens', 'pons', 'poos', 'pool']],
    ['lava', 'ooze', 5, ['lava', 'lave', 'laze', 'daze', 'doze', 'ooze']],
    ['club', 'soda', 6, ['club', 'slub', 'slur', 'sour', 'sous', 'sods', 'soda']],
    ['itch', 'skin', 9, ['itch', 'etch', 'each', 'bach', 'back', 'pack', 'paik', 'pain', 'sain', 'skin']]
    ]

    for pair in wordPairs:
        answer = solve(pair[0], pair[1])
        if answer == pair[3]:
            print('Pass')
        else:
            print('Fail: [', 'solver answer: ', answer, len(answer), 'correct answer', pair[3], len(pair[3]),']')

if __name__ == '__main__':
    main()