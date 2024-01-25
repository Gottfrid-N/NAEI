import sys

glyphs = {'.Bp': '\\U0000e000', '.Bpl': '\\U0000e001', '.Bp!': '\\U0000e002', '.Bp!l': '\\U0000e003', '.B!p': '\\U0000e004', '.B!pl': '\\U0000e005', '.B!b': '\\U0000e006', '.B!bl': '\\U0000e007', '.Bn': '\\U0000e008', '.Bnl': '\\U0000e009', '.Br': '\\U0000e00a', '.Brl': '\\U0000e00b', ".B'r": '\\U0000e00c', ".B'rl": '\\U0000e00d', '.B.': '\\U0000e00e', '.B.l': '\\U0000e00f', '.Bu': '\\U0000e010', '.Bul': '\\U0000e011', '.p>p': '\\U0000e012', '.p>pl': '\\U0000e013', '.p>p!': '\\U0000e014', '.p>p!l': '\\U0000e015', '.p>!p': '\\U0000e016', '.p>!pl': '\\U0000e017', '.p>!b': '\\U0000e018', '.p>!bl': '\\U0000e019', '.p>n': '\\U0000e01a', '.p>nl': '\\U0000e01b', '.p>r': '\\U0000e01c', '.p>rl': '\\U0000e01d', ".p>'r": '\\U0000e01e', ".p>'rl": '\\U0000e01f', '.p>.': '\\U0000e020', '.p>.l': '\\U0000e021', '.p>u': '\\U0000e022', '.p>ul': '\\U0000e023', '.b>p': '\\U0000e024', '.b>pl': '\\U0000e025', '.b>p!': '\\U0000e026', '.b>p!l': '\\U0000e027', '.b>!p': '\\U0000e028', '.b>!pl': '\\U0000e029', '.b>!b': '\\U0000e02a', '.b>!bl': '\\U0000e02b', '.b>n': '\\U0000e02c', '.b>nl': '\\U0000e02d', '.b>r': '\\U0000e02e', '.b>rl': '\\U0000e02f', ".b>'r": '\\U0000e030', ".b>'rl": '\\U0000e031', '.b>.': '\\U0000e032', '.b>.l': '\\U0000e033', '.b>u': '\\U0000e034', '.b>ul': '\\U0000e035', '.p-p': '\\U0000e036', '.p-pl': '\\U0000e037', '.p-p!': '\\U0000e038', '.p-p!l': '\\U0000e039', '.p-!p': '\\U0000e03a', '.p-!pl': '\\U0000e03b', '.p-!b': '\\U0000e03c', '.p-!bl': '\\U0000e03d', '.p-n': '\\U0000e03e', '.p-nl': '\\U0000e03f', '.p-r': '\\U0000e040', '.p-rl': '\\U0000e041', ".p-'r": '\\U0000e042', ".p-'rl": '\\U0000e043', '.p-.': '\\U0000e044', '.p-.l': '\\U0000e045', '.p-u': '\\U0000e046', '.p-ul': '\\U0000e047', '.b-p': '\\U0000e048', '.b-pl': '\\U0000e049', '.b-p!': '\\U0000e04a', '.b-p!l': '\\U0000e04b', '.b-!p': '\\U0000e04c', '.b-!pl': '\\U0000e04d', '.b-!b': '\\U0000e04e', '.b-!bl': '\\U0000e04f', '.b-n': '\\U0000e050', '.b-nl': '\\U0000e051', '.b-r': '\\U0000e052', '.b-rl': '\\U0000e053', ".b-'r": '\\U0000e054', ".b-'rl": '\\U0000e055', '.b-.': '\\U0000e056', '.b-.l': '\\U0000e057', '.b-u': '\\U0000e058', '.b-ul': '\\U0000e059', '.|-p': '\\U0000e05a', '.|-pl': '\\U0000e05b', '.|-p!': '\\U0000e05c', '.|-p!l': '\\U0000e05d', '.|-!p': '\\U0000e05e', '.|-!pl': '\\U0000e05f', '.|-!b': '\\U0000e060', '.|-!bl': '\\U0000e061', '.|-n': '\\U0000e062', '.|-nl': '\\U0000e063', '.|-r': '\\U0000e064', '.|-rl': '\\U0000e065', ".|-'r": '\\U0000e066', ".|-'rl": '\\U0000e067', '.|-.': '\\U0000e068', '.|-.l': '\\U0000e069', '.|-u': '\\U0000e06a', '.|-ul': '\\U0000e06b', '.rp': '\\U0000e06c', '.rpl': '\\U0000e06d', '.rp!': '\\U0000e06e', '.rp!l': '\\U0000e06f', '.r!p': '\\U0000e070', '.r!pl': '\\U0000e071', '.r!b': '\\U0000e072', '.r!bl': '\\U0000e073', '.rn': '\\U0000e074', '.rnl': '\\U0000e075', '.rr': '\\U0000e076', '.rrl': '\\U0000e077', ".r'r": '\\U0000e078', ".r'rl": '\\U0000e079', '.r.': '\\U0000e07a', '.r.l': '\\U0000e07b', '.ru': '\\U0000e07c', '.rul': '\\U0000e07d', '.kp': '\\U0000e07e', '.kpl': '\\U0000e07f', '.kp!': '\\U0000e080', '.kp!l': '\\U0000e081', '.k!p': '\\U0000e082', '.k!pl': '\\U0000e083', '.k!b': '\\U0000e084', '.k!bl': '\\U0000e085', '.kn': '\\U0000e086', '.knl': '\\U0000e087', '.kr': '\\U0000e088', '.krl': '\\U0000e089', ".k'r": '\\U0000e08a', ".k'rl": '\\U0000e08b', '.k.': '\\U0000e08c', '.k.l': '\\U0000e08d', '.ku': '\\U0000e08e', '.kul': '\\U0000e08f', '.hp': '\\U0000e090', '.hpl': '\\U0000e091', '.hp!': '\\U0000e092', '.hp!l': '\\U0000e093', '.h!p': '\\U0000e094', '.h!pl': '\\U0000e095', '.h!b': '\\U0000e096', '.h!bl': '\\U0000e097', '.hn': '\\U0000e098', '.hnl': '\\U0000e099', '.hr': '\\U0000e09a', '.hrl': '\\U0000e09b', ".h'r": '\\U0000e09c', ".h'rl": '\\U0000e09d', '.h.': '\\U0000e09e', '.h.l': '\\U0000e09f', '.hu': '\\U0000e0a0', '.hul': '\\U0000e0a1', '.bp': '\\U0000e0a2', '.bpl': '\\U0000e0a3', '.bp!': '\\U0000e0a4', '.bp!l': '\\U0000e0a5', '.b!p': '\\U0000e0a6', '.b!pl': '\\U0000e0a7', '.b!b': '\\U0000e0a8', '.b!bl': '\\U0000e0a9', '.bn': '\\U0000e0aa', '.bnl': '\\U0000e0ab', '.br': '\\U0000e0ac', '.brl': '\\U0000e0ad', ".b'r": '\\U0000e0ae', ".b'rl": '\\U0000e0af', '.b.': '\\U0000e0b0', '.b.l': '\\U0000e0b1', '.bu': '\\U0000e0b2', '.bul': '\\U0000e0b3', '.Gp': '\\U0000e0b4', '.Gpl': '\\U0000e0b5', '.Gp!': '\\U0000e0b6', '.Gp!l': '\\U0000e0b7', '.G!p': '\\U0000e0b8', '.G!pl': '\\U0000e0b9', '.G!b': '\\U0000e0ba', '.G!bl': '\\U0000e0bb', '.Gn': '\\U0000e0bc', '.Gnl': '\\U0000e0bd', '.Gr': '\\U0000e0be', '.Grl': '\\U0000e0bf', ".G'r": '\\U0000e0c0', ".G'rl": '\\U0000e0c1', '.G.': '\\U0000e0c2', '.G.l': '\\U0000e0c3', '.Gu': '\\U0000e0c4', '.Gul': '\\U0000e0c5', '.Jp': '\\U0000e0c6', '.Jpl': '\\U0000e0c7', '.Jp!': '\\U0000e0c8', '.Jp!l': '\\U0000e0c9', '.J!p': '\\U0000e0ca', '.J!pl': '\\U0000e0cb', '.J!b': '\\U0000e0cc', '.J!bl': '\\U0000e0cd', '.Jn': '\\U0000e0ce', '.Jnl': '\\U0000e0cf', '.Jr': '\\U0000e0d0', '.Jrl': '\\U0000e0d1', ".J'r": '\\U0000e0d2', ".J'rl": '\\U0000e0d3', '.J.': '\\U0000e0d4', '.J.l': '\\U0000e0d5', '.Ju': '\\U0000e0d6', '.Jul': '\\U0000e0d7', '.Lp': '\\U0000e0d8', '.Lpl': '\\U0000e0d9', '.Lp!': '\\U0000e0da', '.Lp!l': '\\U0000e0db', '.L!p': '\\U0000e0dc', '.L!pl': '\\U0000e0dd', '.L!b': '\\U0000e0de', '.L!bl': '\\U0000e0df', '.Ln': '\\U0000e0e0', '.Lnl': '\\U0000e0e1', '.Lr': '\\U0000e0e2', '.Lrl': '\\U0000e0e3', ".L'r": '\\U0000e0e4', ".L'rl": '\\U0000e0e5', '.L.': '\\U0000e0e6', '.L.l': '\\U0000e0e7', '.Lu': '\\U0000e0e8', '.Lul': '\\U0000e0e9', '.|^p': '\\U0000e0ea', '.|^pl': '\\U0000e0eb', '.|^p!': '\\U0000e0ec', '.|^p!l': '\\U0000e0ed', '.|^!p': '\\U0000e0ee', '.|^!pl': '\\U0000e0ef', '.|^!b': '\\U0000e0f0', '.|^!bl': '\\U0000e0f1', '.|^n': '\\U0000e0f2', '.|^nl': '\\U0000e0f3', '.|^r': '\\U0000e0f4', '.|^rl': '\\U0000e0f5', ".|^'r": '\\U0000e0f6', ".|^'rl": '\\U0000e0f7', '.|^.': '\\U0000e0f8', '.|^.l': '\\U0000e0f9', '.|^u': '\\U0000e0fa', '.|^ul': '\\U0000e0fb', '.|vp': '\\U0000e0fc', '.|vpl': '\\U0000e0fd', '.|vp!': '\\U0000e0fe', '.|vp!l': '\\U0000e0ff', '.|v!p': '\\U0000e100', '.|v!pl': '\\U0000e101', '.|v!b': '\\U0000e102', '.|v!bl': '\\U0000e103', '.|vn': '\\U0000e104', '.|vnl': '\\U0000e105', '.|vr': '\\U0000e106', '.|vrl': '\\U0000e107', ".|v'r": '\\U0000e108', ".|v'rl": '\\U0000e109', '.|v.': '\\U0000e10a', '.|v.l': '\\U0000e10b', '.|vu': '\\U0000e10c', '.|vul': '\\U0000e10d', ',Bp': '\\U0000e10e', ',Bpl': '\\U0000e10f', ',Bp!': '\\U0000e110', ',Bp!l': '\\U0000e111', ',B!p': '\\U0000e112', ',B!pl': '\\U0000e113', ',B!b': '\\U0000e114', ',B!bl': '\\U0000e115', ',Bn': '\\U0000e116', ',Bnl': '\\U0000e117', ',Br': '\\U0000e118', ',Brl': '\\U0000e119', ",B'r": '\\U0000e11a', ",B'rl": '\\U0000e11b', ',B.': '\\U0000e11c', ',B.l': '\\U0000e11d', ',Bu': '\\U0000e11e', ',Bul': '\\U0000e11f', ',p>p': '\\U0000e120', ',p>pl': '\\U0000e121', ',p>p!': '\\U0000e122', ',p>p!l': '\\U0000e123', ',p>!p': '\\U0000e124', ',p>!pl': '\\U0000e125', ',p>!b': '\\U0000e126', ',p>!bl': '\\U0000e127', ',p>n': '\\U0000e128', ',p>nl': '\\U0000e129', ',p>r': '\\U0000e12a', ',p>rl': '\\U0000e12b', ",p>'r": '\\U0000e12c', ",p>'rl": '\\U0000e12d', ',p>.': '\\U0000e12e', ',p>.l': '\\U0000e12f', ',p>u': '\\U0000e130', ',p>ul': '\\U0000e131', ',b>p': '\\U0000e132', ',b>pl': '\\U0000e133', ',b>p!': '\\U0000e134', ',b>p!l': '\\U0000e135', ',b>!p': '\\U0000e136', ',b>!pl': '\\U0000e137', ',b>!b': '\\U0000e138', ',b>!bl': '\\U0000e139', ',b>n': '\\U0000e13a', ',b>nl': '\\U0000e13b', ',b>r': '\\U0000e13c', ',b>rl': '\\U0000e13d', ",b>'r": '\\U0000e13e', ",b>'rl": '\\U0000e13f', ',b>.': '\\U0000e140', ',b>.l': '\\U0000e141', ',b>u': '\\U0000e142', ',b>ul': '\\U0000e143', ',p-p': '\\U0000e144', ',p-pl': '\\U0000e145', ',p-p!': '\\U0000e146', ',p-p!l': '\\U0000e147', ',p-!p': '\\U0000e148', ',p-!pl': '\\U0000e149', ',p-!b': '\\U0000e14a', ',p-!bl': '\\U0000e14b', ',p-n': '\\U0000e14c', ',p-nl': '\\U0000e14d', ',p-r': '\\U0000e14e', ',p-rl': '\\U0000e14f', ",p-'r": '\\U0000e150', ",p-'rl": '\\U0000e151', ',p-.': '\\U0000e152', ',p-.l': '\\U0000e153', ',p-u': '\\U0000e154', ',p-ul': '\\U0000e155', ',b-p': '\\U0000e156', ',b-pl': '\\U0000e157', ',b-p!': '\\U0000e158', ',b-p!l': '\\U0000e159', ',b-!p': '\\U0000e15a', ',b-!pl': '\\U0000e15b', ',b-!b': '\\U0000e15c', ',b-!bl': '\\U0000e15d', ',b-n': '\\U0000e15e', ',b-nl': '\\U0000e15f', ',b-r': '\\U0000e160', ',b-rl': '\\U0000e161', ",b-'r": '\\U0000e162', ",b-'rl": '\\U0000e163', ',b-.': '\\U0000e164', ',b-.l': '\\U0000e165', ',b-u': '\\U0000e166', ',b-ul': '\\U0000e167', ',|-p': '\\U0000e168', ',|-pl': '\\U0000e169', ',|-p!': '\\U0000e16a', ',|-p!l': '\\U0000e16b', ',|-!p': '\\U0000e16c', ',|-!pl': '\\U0000e16d', ',|-!b': '\\U0000e16e', ',|-!bl': '\\U0000e16f', ',|-n': '\\U0000e170', ',|-nl': '\\U0000e171', ',|-r': '\\U0000e172', ',|-rl': '\\U0000e173', ",|-'r": '\\U0000e174', ",|-'rl": '\\U0000e175', ',|-.': '\\U0000e176', ',|-.l': '\\U0000e177', ',|-u': '\\U0000e178', ',|-ul': '\\U0000e179', ',rp': '\\U0000e17a', ',rpl': '\\U0000e17b', ',rp!': '\\U0000e17c', ',rp!l': '\\U0000e17d', ',r!p': '\\U0000e17e', ',r!pl': '\\U0000e17f', ',r!b': '\\U0000e180', ',r!bl': '\\U0000e181', ',rn': '\\U0000e182', ',rnl': '\\U0000e183', ',rr': '\\U0000e184', ',rrl': '\\U0000e185', ",r'r": '\\U0000e186', ",r'rl": '\\U0000e187', ',r.': '\\U0000e188', ',r.l': '\\U0000e189', ',ru': '\\U0000e18a', ',rul': '\\U0000e18b', ',kp': '\\U0000e18c', ',kpl': '\\U0000e18d', ',kp!': '\\U0000e18e', ',kp!l': '\\U0000e18f', ',k!p': '\\U0000e190', ',k!pl': '\\U0000e191', ',k!b': '\\U0000e192', ',k!bl': '\\U0000e193', ',kn': '\\U0000e194', ',knl': '\\U0000e195', ',kr': '\\U0000e196', ',krl': '\\U0000e197', ",k'r": '\\U0000e198', ",k'rl": '\\U0000e199', ',k.': '\\U0000e19a', ',k.l': '\\U0000e19b', ',ku': '\\U0000e19c', ',kul': '\\U0000e19d', ',hp': '\\U0000e19e', ',hpl': '\\U0000e19f', ',hp!': '\\U0000e1a0', ',hp!l': '\\U0000e1a1', ',h!p': '\\U0000e1a2', ',h!pl': '\\U0000e1a3', ',h!b': '\\U0000e1a4', ',h!bl': '\\U0000e1a5', ',hn': '\\U0000e1a6', ',hnl': '\\U0000e1a7', ',hr': '\\U0000e1a8', ',hrl': '\\U0000e1a9', ",h'r": '\\U0000e1aa', ",h'rl": '\\U0000e1ab', ',h.': '\\U0000e1ac', ',h.l': '\\U0000e1ad', ',hu': '\\U0000e1ae', ',hul': '\\U0000e1af', ',bp': '\\U0000e1b0', ',bpl': '\\U0000e1b1', ',bp!': '\\U0000e1b2', ',bp!l': '\\U0000e1b3', ',b!p': '\\U0000e1b4', ',b!pl': '\\U0000e1b5', ',b!b': '\\U0000e1b6', ',b!bl': '\\U0000e1b7', ',bn': '\\U0000e1b8', ',bnl': '\\U0000e1b9', ',br': '\\U0000e1ba', ',brl': '\\U0000e1bb', ",b'r": '\\U0000e1bc', ",b'rl": '\\U0000e1bd', ',b.': '\\U0000e1be', ',b.l': '\\U0000e1bf', ',bu': '\\U0000e1c0', ',bul': '\\U0000e1c1', ',Gp': '\\U0000e1c2', ',Gpl': '\\U0000e1c3', ',Gp!': '\\U0000e1c4', ',Gp!l': '\\U0000e1c5', ',G!p': '\\U0000e1c6', ',G!pl': '\\U0000e1c7', ',G!b': '\\U0000e1c8', ',G!bl': '\\U0000e1c9', ',Gn': '\\U0000e1ca', ',Gnl': '\\U0000e1cb', ',Gr': '\\U0000e1cc', ',Grl': '\\U0000e1cd', ",G'r": '\\U0000e1ce', ",G'rl": '\\U0000e1cf', ',G.': '\\U0000e1d0', ',G.l': '\\U0000e1d1', ',Gu': '\\U0000e1d2', ',Gul': '\\U0000e1d3', ',Jp': '\\U0000e1d4', ',Jpl': '\\U0000e1d5', ',Jp!': '\\U0000e1d6', ',Jp!l': '\\U0000e1d7', ',J!p': '\\U0000e1d8', ',J!pl': '\\U0000e1d9', ',J!b': '\\U0000e1da', ',J!bl': '\\U0000e1db', ',Jn': '\\U0000e1dc', ',Jnl': '\\U0000e1dd', ',Jr': '\\U0000e1de', ',Jrl': '\\U0000e1df', ",J'r": '\\U0000e1e0', ",J'rl": '\\U0000e1e1', ',J.': '\\U0000e1e2', ',J.l': '\\U0000e1e3', ',Ju': '\\U0000e1e4', ',Jul': '\\U0000e1e5', ',Lp': '\\U0000e1e6', ',Lpl': '\\U0000e1e7', ',Lp!': '\\U0000e1e8', ',Lp!l': '\\U0000e1e9', ',L!p': '\\U0000e1ea', ',L!pl': '\\U0000e1eb', ',L!b': '\\U0000e1ec', ',L!bl': '\\U0000e1ed', ',Ln': '\\U0000e1ee', ',Lnl': '\\U0000e1ef', ',Lr': '\\U0000e1f0', ',Lrl': '\\U0000e1f1', ",L'r": '\\U0000e1f2', ",L'rl": '\\U0000e1f3', ',L.': '\\U0000e1f4', ',L.l': '\\U0000e1f5', ',Lu': '\\U0000e1f6', ',Lul': '\\U0000e1f7', ',|^p': '\\U0000e1f8', ',|^pl': '\\U0000e1f9', ',|^p!': '\\U0000e1fa', ',|^p!l': '\\U0000e1fb', ',|^!p': '\\U0000e1fc', ',|^!pl': '\\U0000e1fd', ',|^!b': '\\U0000e1fe', ',|^!bl': '\\U0000e1ff', ',|^n': '\\U0000e200', ',|^nl': '\\U0000e201', ',|^r': '\\U0000e202', ',|^rl': '\\U0000e203', ",|^'r": '\\U0000e204', ",|^'rl": '\\U0000e205', ',|^.': '\\U0000e206', ',|^.l': '\\U0000e207', ',|^u': '\\U0000e208', ',|^ul': '\\U0000e209', ',|vp': '\\U0000e20a', ',|vpl': '\\U0000e20b', ',|vp!': '\\U0000e20c', ',|vp!l': '\\U0000e20d', ',|v!p': '\\U0000e20e', ',|v!pl': '\\U0000e20f', ',|v!b': '\\U0000e210', ',|v!bl': '\\U0000e211', ',|vn': '\\U0000e212', ',|vnl': '\\U0000e213', ',|vr': '\\U0000e214', ',|vrl': '\\U0000e215', ",|v'r": '\\U0000e216', ",|v'rl": '\\U0000e217', ',|v.': '\\U0000e218', ',|v.l': '\\U0000e219', ',|vu': '\\U0000e21a', ',|vul': '\\U0000e21b', 'oBp': '\\U0000e21c', 'oBpl': '\\U0000e21d', 'oBp!': '\\U0000e21e', 'oBp!l': '\\U0000e21f', 'oB!p': '\\U0000e220', 'oB!pl': '\\U0000e221', 'oB!b': '\\U0000e222', 'oB!bl': '\\U0000e223', 'oBn': '\\U0000e224', 'oBnl': '\\U0000e225', 'oBr': '\\U0000e226', 'oBrl': '\\U0000e227', "oB'r": '\\U0000e228', "oB'rl": '\\U0000e229', 'oB.': '\\U0000e22a', 'oB.l': '\\U0000e22b', 'oBu': '\\U0000e22c', 'oBul': '\\U0000e22d', 'op>p': '\\U0000e22e', 'op>pl': '\\U0000e22f', 'op>p!': '\\U0000e230', 'op>p!l': '\\U0000e231', 'op>!p': '\\U0000e232', 'op>!pl': '\\U0000e233', 'op>!b': '\\U0000e234', 'op>!bl': '\\U0000e235', 'op>n': '\\U0000e236', 'op>nl': '\\U0000e237', 'op>r': '\\U0000e238', 'op>rl': '\\U0000e239', "op>'r": '\\U0000e23a', "op>'rl": '\\U0000e23b', 'op>.': '\\U0000e23c', 'op>.l': '\\U0000e23d', 'op>u': '\\U0000e23e', 'op>ul': '\\U0000e23f', 'ob>p': '\\U0000e240', 'ob>pl': '\\U0000e241', 'ob>p!': '\\U0000e242', 'ob>p!l': '\\U0000e243', 'ob>!p': '\\U0000e244', 'ob>!pl': '\\U0000e245', 'ob>!b': '\\U0000e246', 'ob>!bl': '\\U0000e247', 'ob>n': '\\U0000e248', 'ob>nl': '\\U0000e249', 'ob>r': '\\U0000e24a', 'ob>rl': '\\U0000e24b', "ob>'r": '\\U0000e24c', "ob>'rl": '\\U0000e24d', 'ob>.': '\\U0000e24e', 'ob>.l': '\\U0000e24f', 'ob>u': '\\U0000e250', 'ob>ul': '\\U0000e251', 'op-p': '\\U0000e252', 'op-pl': '\\U0000e253', 'op-p!': '\\U0000e254', 'op-p!l': '\\U0000e255', 'op-!p': '\\U0000e256', 'op-!pl': '\\U0000e257', 'op-!b': '\\U0000e258', 'op-!bl': '\\U0000e259', 'op-n': '\\U0000e25a', 'op-nl': '\\U0000e25b', 'op-r': '\\U0000e25c', 'op-rl': '\\U0000e25d', "op-'r": '\\U0000e25e', "op-'rl": '\\U0000e25f', 'op-.': '\\U0000e260', 'op-.l': '\\U0000e261', 'op-u': '\\U0000e262', 'op-ul': '\\U0000e263', 'ob-p': '\\U0000e264', 'ob-pl': '\\U0000e265', 'ob-p!': '\\U0000e266', 'ob-p!l': '\\U0000e267', 'ob-!p': '\\U0000e268', 'ob-!pl': '\\U0000e269', 'ob-!b': '\\U0000e26a', 'ob-!bl': '\\U0000e26b', 'ob-n': '\\U0000e26c', 'ob-nl': '\\U0000e26d', 'ob-r': '\\U0000e26e', 'ob-rl': '\\U0000e26f', "ob-'r": '\\U0000e270', "ob-'rl": '\\U0000e271', 'ob-.': '\\U0000e272', 'ob-.l': '\\U0000e273', 'ob-u': '\\U0000e274', 'ob-ul': '\\U0000e275', 'o|-p': '\\U0000e276', 'o|-pl': '\\U0000e277', 'o|-p!': '\\U0000e278', 'o|-p!l': '\\U0000e279', 'o|-!p': '\\U0000e27a', 'o|-!pl': '\\U0000e27b', 'o|-!b': '\\U0000e27c', 'o|-!bl': '\\U0000e27d', 'o|-n': '\\U0000e27e', 'o|-nl': '\\U0000e27f', 'o|-r': '\\U0000e280', 'o|-rl': '\\U0000e281', "o|-'r": '\\U0000e282', "o|-'rl": '\\U0000e283', 'o|-.': '\\U0000e284', 'o|-.l': '\\U0000e285', 'o|-u': '\\U0000e286', 'o|-ul': '\\U0000e287', 'orp': '\\U0000e288', 'orpl': '\\U0000e289', 'orp!': '\\U0000e28a', 'orp!l': '\\U0000e28b', 'or!p': '\\U0000e28c', 'or!pl': '\\U0000e28d', 'or!b': '\\U0000e28e', 'or!bl': '\\U0000e28f', 'orn': '\\U0000e290', 'ornl': '\\U0000e291', 'orr': '\\U0000e292', 'orrl': '\\U0000e293', "or'r": '\\U0000e294', "or'rl": '\\U0000e295', 'or.': '\\U0000e296', 'or.l': '\\U0000e297', 'oru': '\\U0000e298', 'orul': '\\U0000e299', 'okp': '\\U0000e29a', 'okpl': '\\U0000e29b', 'okp!': '\\U0000e29c', 'okp!l': '\\U0000e29d', 'ok!p': '\\U0000e29e', 'ok!pl': '\\U0000e29f', 'ok!b': '\\U0000e2a0', 'ok!bl': '\\U0000e2a1', 'okn': '\\U0000e2a2', 'oknl': '\\U0000e2a3', 'okr': '\\U0000e2a4', 'okrl': '\\U0000e2a5', "ok'r": '\\U0000e2a6', "ok'rl": '\\U0000e2a7', 'ok.': '\\U0000e2a8', 'ok.l': '\\U0000e2a9', 'oku': '\\U0000e2aa', 'okul': '\\U0000e2ab', 'ohp': '\\U0000e2ac', 'ohpl': '\\U0000e2ad', 'ohp!': '\\U0000e2ae', 'ohp!l': '\\U0000e2af', 'oh!p': '\\U0000e2b0', 'oh!pl': '\\U0000e2b1', 'oh!b': '\\U0000e2b2', 'oh!bl': '\\U0000e2b3', 'ohn': '\\U0000e2b4', 'ohnl': '\\U0000e2b5', 'ohr': '\\U0000e2b6', 'ohrl': '\\U0000e2b7', "oh'r": '\\U0000e2b8', "oh'rl": '\\U0000e2b9', 'oh.': '\\U0000e2ba', 'oh.l': '\\U0000e2bb', 'ohu': '\\U0000e2bc', 'ohul': '\\U0000e2bd', 'obp': '\\U0000e2be', 'obpl': '\\U0000e2bf', 'obp!': '\\U0000e2c0', 'obp!l': '\\U0000e2c1', 'ob!p': '\\U0000e2c2', 'ob!pl': '\\U0000e2c3', 'ob!b': '\\U0000e2c4', 'ob!bl': '\\U0000e2c5', 'obn': '\\U0000e2c6', 'obnl': '\\U0000e2c7', 'obr': '\\U0000e2c8', 'obrl': '\\U0000e2c9', "ob'r": '\\U0000e2ca', "ob'rl": '\\U0000e2cb', 'ob.': '\\U0000e2cc', 'ob.l': '\\U0000e2cd', 'obu': '\\U0000e2ce', 'obul': '\\U0000e2cf', 'oGp': '\\U0000e2d0', 'oGpl': '\\U0000e2d1', 'oGp!': '\\U0000e2d2', 'oGp!l': '\\U0000e2d3', 'oG!p': '\\U0000e2d4', 'oG!pl': '\\U0000e2d5', 'oG!b': '\\U0000e2d6', 'oG!bl': '\\U0000e2d7', 'oGn': '\\U0000e2d8', 'oGnl': '\\U0000e2d9', 'oGr': '\\U0000e2da', 'oGrl': '\\U0000e2db', "oG'r": '\\U0000e2dc', "oG'rl": '\\U0000e2dd', 'oG.': '\\U0000e2de', 'oG.l': '\\U0000e2df', 'oGu': '\\U0000e2e0', 'oGul': '\\U0000e2e1', 'oJp': '\\U0000e2e2', 'oJpl': '\\U0000e2e3', 'oJp!': '\\U0000e2e4', 'oJp!l': '\\U0000e2e5', 'oJ!p': '\\U0000e2e6', 'oJ!pl': '\\U0000e2e7', 'oJ!b': '\\U0000e2e8', 'oJ!bl': '\\U0000e2e9', 'oJn': '\\U0000e2ea', 'oJnl': '\\U0000e2eb', 'oJr': '\\U0000e2ec', 'oJrl': '\\U0000e2ed', "oJ'r": '\\U0000e2ee', "oJ'rl": '\\U0000e2ef', 'oJ.': '\\U0000e2f0', 'oJ.l': '\\U0000e2f1', 'oJu': '\\U0000e2f2', 'oJul': '\\U0000e2f3', 'oLp': '\\U0000e2f4', 'oLpl': '\\U0000e2f5', 'oLp!': '\\U0000e2f6', 'oLp!l': '\\U0000e2f7', 'oL!p': '\\U0000e2f8', 'oL!pl': '\\U0000e2f9', 'oL!b': '\\U0000e2fa', 'oL!bl': '\\U0000e2fb', 'oLn': '\\U0000e2fc', 'oLnl': '\\U0000e2fd', 'oLr': '\\U0000e2fe', 'oLrl': '\\U0000e2ff', "oL'r": '\\U0000e300', "oL'rl": '\\U0000e301', 'oL.': '\\U0000e302', 'oL.l': '\\U0000e303', 'oLu': '\\U0000e304', 'oLul': '\\U0000e305', 'o|^p': '\\U0000e306', 'o|^pl': '\\U0000e307', 'o|^p!': '\\U0000e308', 'o|^p!l': '\\U0000e309', 'o|^!p': '\\U0000e30a', 'o|^!pl': '\\U0000e30b', 'o|^!b': '\\U0000e30c', 'o|^!bl': '\\U0000e30d', 'o|^n': '\\U0000e30e', 'o|^nl': '\\U0000e30f', 'o|^r': '\\U0000e310', 'o|^rl': '\\U0000e311', "o|^'r": '\\U0000e312', "o|^'rl": '\\U0000e313', 'o|^.': '\\U0000e314', 'o|^.l': '\\U0000e315', 'o|^u': '\\U0000e316', 'o|^ul': '\\U0000e317', 'o|vp': '\\U0000e318', 'o|vpl': '\\U0000e319', 'o|vp!': '\\U0000e31a', 'o|vp!l': '\\U0000e31b', 'o|v!p': '\\U0000e31c', 'o|v!pl': '\\U0000e31d', 'o|v!b': '\\U0000e31e', 'o|v!bl': '\\U0000e31f', 'o|vn': '\\U0000e320', 'o|vnl': '\\U0000e321', 'o|vr': '\\U0000e322', 'o|vrl': '\\U0000e323', "o|v'r": '\\U0000e324', "o|v'rl": '\\U0000e325', 'o|v.': '\\U0000e326', 'o|v.l': '\\U0000e327', 'o|vu': '\\U0000e328', 'o|vul': '\\U0000e329', 'xBp': '\\U0000e32a', 'xBpl': '\\U0000e32b', 'xBp!': '\\U0000e32c', 'xBp!l': '\\U0000e32d', 'xB!p': '\\U0000e32e', 'xB!pl': '\\U0000e32f', 'xB!b': '\\U0000e330', 'xB!bl': '\\U0000e331', 'xBn': '\\U0000e332', 'xBnl': '\\U0000e333', 'xBr': '\\U0000e334', 'xBrl': '\\U0000e335', "xB'r": '\\U0000e336', "xB'rl": '\\U0000e337', 'xB.': '\\U0000e338', 'xB.l': '\\U0000e339', 'xBu': '\\U0000e33a', 'xBul': '\\U0000e33b', 'xp>p': '\\U0000e33c', 'xp>pl': '\\U0000e33d', 'xp>p!': '\\U0000e33e', 'xp>p!l': '\\U0000e33f', 'xp>!p': '\\U0000e340', 'xp>!pl': '\\U0000e341', 'xp>!b': '\\U0000e342', 'xp>!bl': '\\U0000e343', 'xp>n': '\\U0000e344', 'xp>nl': '\\U0000e345', 'xp>r': '\\U0000e346', 'xp>rl': '\\U0000e347', "xp>'r": '\\U0000e348', "xp>'rl": '\\U0000e349', 'xp>.': '\\U0000e34a', 'xp>.l': '\\U0000e34b', 'xp>u': '\\U0000e34c', 'xp>ul': '\\U0000e34d', 'xb>p': '\\U0000e34e', 'xb>pl': '\\U0000e34f', 'xb>p!': '\\U0000e350', 'xb>p!l': '\\U0000e351', 'xb>!p': '\\U0000e352', 'xb>!pl': '\\U0000e353', 'xb>!b': '\\U0000e354', 'xb>!bl': '\\U0000e355', 'xb>n': '\\U0000e356', 'xb>nl': '\\U0000e357', 'xb>r': '\\U0000e358', 'xb>rl': '\\U0000e359', "xb>'r": '\\U0000e35a', "xb>'rl": '\\U0000e35b', 'xb>.': '\\U0000e35c', 'xb>.l': '\\U0000e35d', 'xb>u': '\\U0000e35e', 'xb>ul': '\\U0000e35f', 'xp-p': '\\U0000e360', 'xp-pl': '\\U0000e361', 'xp-p!': '\\U0000e362', 'xp-p!l': '\\U0000e363', 'xp-!p': '\\U0000e364', 'xp-!pl': '\\U0000e365', 'xp-!b': '\\U0000e366', 'xp-!bl': '\\U0000e367', 'xp-n': '\\U0000e368', 'xp-nl': '\\U0000e369', 'xp-r': '\\U0000e36a', 'xp-rl': '\\U0000e36b', "xp-'r": '\\U0000e36c', "xp-'rl": '\\U0000e36d', 'xp-.': '\\U0000e36e', 'xp-.l': '\\U0000e36f', 'xp-u': '\\U0000e370', 'xp-ul': '\\U0000e371', 'xb-p': '\\U0000e372', 'xb-pl': '\\U0000e373', 'xb-p!': '\\U0000e374', 'xb-p!l': '\\U0000e375', 'xb-!p': '\\U0000e376', 'xb-!pl': '\\U0000e377', 'xb-!b': '\\U0000e378', 'xb-!bl': '\\U0000e379', 'xb-n': '\\U0000e37a', 'xb-nl': '\\U0000e37b', 'xb-r': '\\U0000e37c', 'xb-rl': '\\U0000e37d', "xb-'r": '\\U0000e37e', "xb-'rl": '\\U0000e37f', 'xb-.': '\\U0000e380', 'xb-.l': '\\U0000e381', 'xb-u': '\\U0000e382', 'xb-ul': '\\U0000e383', 'x|-p': '\\U0000e384', 'x|-pl': '\\U0000e385', 'x|-p!': '\\U0000e386', 'x|-p!l': '\\U0000e387', 'x|-!p': '\\U0000e388', 'x|-!pl': '\\U0000e389', 'x|-!b': '\\U0000e38a', 'x|-!bl': '\\U0000e38b', 'x|-n': '\\U0000e38c', 'x|-nl': '\\U0000e38d', 'x|-r': '\\U0000e38e', 'x|-rl': '\\U0000e38f', "x|-'r": '\\U0000e390', "x|-'rl": '\\U0000e391', 'x|-.': '\\U0000e392', 'x|-.l': '\\U0000e393', 'x|-u': '\\U0000e394', 'x|-ul': '\\U0000e395', 'xrp': '\\U0000e396', 'xrpl': '\\U0000e397', 'xrp!': '\\U0000e398', 'xrp!l': '\\U0000e399', 'xr!p': '\\U0000e39a', 'xr!pl': '\\U0000e39b', 'xr!b': '\\U0000e39c', 'xr!bl': '\\U0000e39d', 'xrn': '\\U0000e39e', 'xrnl': '\\U0000e39f', 'xrr': '\\U0000e3a0', 'xrrl': '\\U0000e3a1', "xr'r": '\\U0000e3a2', "xr'rl": '\\U0000e3a3', 'xr.': '\\U0000e3a4', 'xr.l': '\\U0000e3a5', 'xru': '\\U0000e3a6', 'xrul': '\\U0000e3a7', 'xkp': '\\U0000e3a8', 'xkpl': '\\U0000e3a9', 'xkp!': '\\U0000e3aa', 'xkp!l': '\\U0000e3ab', 'xk!p': '\\U0000e3ac', 'xk!pl': '\\U0000e3ad', 'xk!b': '\\U0000e3ae', 'xk!bl': '\\U0000e3af', 'xkn': '\\U0000e3b0', 'xknl': '\\U0000e3b1', 'xkr': '\\U0000e3b2', 'xkrl': '\\U0000e3b3', "xk'r": '\\U0000e3b4', "xk'rl": '\\U0000e3b5', 'xk.': '\\U0000e3b6', 'xk.l': '\\U0000e3b7', 'xku': '\\U0000e3b8', 'xkul': '\\U0000e3b9', 'xhp': '\\U0000e3ba', 'xhpl': '\\U0000e3bb', 'xhp!': '\\U0000e3bc', 'xhp!l': '\\U0000e3bd', 'xh!p': '\\U0000e3be', 'xh!pl': '\\U0000e3bf', 'xh!b': '\\U0000e3c0', 'xh!bl': '\\U0000e3c1', 'xhn': '\\U0000e3c2', 'xhnl': '\\U0000e3c3', 'xhr': '\\U0000e3c4', 'xhrl': '\\U0000e3c5', "xh'r": '\\U0000e3c6', "xh'rl": '\\U0000e3c7', 'xh.': '\\U0000e3c8', 'xh.l': '\\U0000e3c9', 'xhu': '\\U0000e3ca', 'xhul': '\\U0000e3cb', 'xbp': '\\U0000e3cc', 'xbpl': '\\U0000e3cd', 'xbp!': '\\U0000e3ce', 'xbp!l': '\\U0000e3cf', 'xb!p': '\\U0000e3d0', 'xb!pl': '\\U0000e3d1', 'xb!b': '\\U0000e3d2', 'xb!bl': '\\U0000e3d3', 'xbn': '\\U0000e3d4', 'xbnl': '\\U0000e3d5', 'xbr': '\\U0000e3d6', 'xbrl': '\\U0000e3d7', "xb'r": '\\U0000e3d8', "xb'rl": '\\U0000e3d9', 'xb.': '\\U0000e3da', 'xb.l': '\\U0000e3db', 'xbu': '\\U0000e3dc', 'xbul': '\\U0000e3dd', 'xGp': '\\U0000e3de', 'xGpl': '\\U0000e3df', 'xGp!': '\\U0000e3e0', 'xGp!l': '\\U0000e3e1', 'xG!p': '\\U0000e3e2', 'xG!pl': '\\U0000e3e3', 'xG!b': '\\U0000e3e4', 'xG!bl': '\\U0000e3e5', 'xGn': '\\U0000e3e6', 'xGnl': '\\U0000e3e7', 'xGr': '\\U0000e3e8', 'xGrl': '\\U0000e3e9', "xG'r": '\\U0000e3ea', "xG'rl": '\\U0000e3eb', 'xG.': '\\U0000e3ec', 'xG.l': '\\U0000e3ed', 'xGu': '\\U0000e3ee', 'xGul': '\\U0000e3ef', 'xJp': '\\U0000e3f0', 'xJpl': '\\U0000e3f1', 'xJp!': '\\U0000e3f2', 'xJp!l': '\\U0000e3f3', 'xJ!p': '\\U0000e3f4', 'xJ!pl': '\\U0000e3f5', 'xJ!b': '\\U0000e3f6', 'xJ!bl': '\\U0000e3f7', 'xJn': '\\U0000e3f8', 'xJnl': '\\U0000e3f9', 'xJr': '\\U0000e3fa', 'xJrl': '\\U0000e3fb', "xJ'r": '\\U0000e3fc', "xJ'rl": '\\U0000e3fd', 'xJ.': '\\U0000e3fe', 'xJ.l': '\\U0000e3ff', 'xJu': '\\U0000e400', 'xJul': '\\U0000e401', 'xLp': '\\U0000e402', 'xLpl': '\\U0000e403', 'xLp!': '\\U0000e404', 'xLp!l': '\\U0000e405', 'xL!p': '\\U0000e406', 'xL!pl': '\\U0000e407', 'xL!b': '\\U0000e408', 'xL!bl': '\\U0000e409', 'xLn': '\\U0000e40a', 'xLnl': '\\U0000e40b', 'xLr': '\\U0000e40c', 'xLrl': '\\U0000e40d', "xL'r": '\\U0000e40e', "xL'rl": '\\U0000e40f', 'xL.': '\\U0000e410', 'xL.l': '\\U0000e411', 'xLu': '\\U0000e412', 'xLul': '\\U0000e413', 'x|^p': '\\U0000e414', 'x|^pl': '\\U0000e415', 'x|^p!': '\\U0000e416', 'x|^p!l': '\\U0000e417', 'x|^!p': '\\U0000e418', 'x|^!pl': '\\U0000e419', 'x|^!b': '\\U0000e41a', 'x|^!bl': '\\U0000e41b', 'x|^n': '\\U0000e41c', 'x|^nl': '\\U0000e41d', 'x|^r': '\\U0000e41e', 'x|^rl': '\\U0000e41f', "x|^'r": '\\U0000e420', "x|^'rl": '\\U0000e421', 'x|^.': '\\U0000e422', 'x|^.l': '\\U0000e423', 'x|^u': '\\U0000e424', 'x|^ul': '\\U0000e425', 'x|vp': '\\U0000e426', 'x|vpl': '\\U0000e427', 'x|vp!': '\\U0000e428', 'x|vp!l': '\\U0000e429', 'x|v!p': '\\U0000e42a', 'x|v!pl': '\\U0000e42b', 'x|v!b': '\\U0000e42c', 'x|v!bl': '\\U0000e42d', 'x|vn': '\\U0000e42e', 'x|vnl': '\\U0000e42f', 'x|vr': '\\U0000e430', 'x|vrl': '\\U0000e431', "x|v'r": '\\U0000e432', "x|v'rl": '\\U0000e433', 'x|v.': '\\U0000e434', 'x|v.l': '\\U0000e435', 'x|vu': '\\U0000e436', 'x|vul': '\\U0000e437'}


def parse(input_file):
    index = 0
    output = ""
    while index != len(input_file):
        match input_file[index]:
            case "{":
                index += 1
                glyph = ""
                while input_file[index] != "}":
                    glyph += input_file[index]
                    index += 1
                try:
                    output += glyphs[glyph]
                except KeyError:
                    print(f"Invalid glyph at index: {index}!")
        index += 1
    return output


if __name__ == '__main__':
    try:
        input_file = open(sys.argv[1], "r").read()
    except IndexError:
        input_file = open("default-input.naei", "r").read()

    print(input_file)
    print(parse(input_file))
