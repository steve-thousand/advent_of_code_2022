def build_monkey_tree(monkeys, key="root"):
    monkey_map = {}
    for monkey in monkeys:
        monkey_map[monkey[0]] = monkey[1]
    root = monkey_map[key]
    q = [root]
    while q:
        node = q.pop()
        if key == "root" or node[0] != 'humn':
            node_left = monkey_map[node[0]]
            node[0] = node_left
            if len(node_left) > 1:
                q.append(node_left)
        if key == "root" or node[1] != 'humn':
            node_right = monkey_map[node[2]]
            node[2] = node_right
            if len(node_right) > 1:
                q.append(node_right)
    return root


def calculate_monkey_tree(tree):
    if len(tree) == 1:
        return int(tree[0])
    else:
        left = calculate_monkey_tree(tree[0])
        right = calculate_monkey_tree(tree[2])
        if tree[1] == "+":
            return left + right
        if tree[1] == "-":
            return left - right
        if tree[1] == "*":
            return left * right
        if tree[1] == "/":
            return left // right


def tree_contains_human(tree):
    if tree == "humn":
        return True
    q = [tree]
    while q:
        tree = q.pop()
        if tree[0] == "humn":
            return True
        if len(tree) == 1:
            continue
        else:
            q.append(tree[0])
        if tree[2] == "humn":
            return True
        q.append(tree[2])
    return False


def calculate_human(monkeys):
    root_expression = next(x for x in monkeys if x[0] == 'root')[1]
    left = build_monkey_tree(monkeys, root_expression[0])
    right = build_monkey_tree(monkeys, root_expression[2])
    if tree_contains_human(left):
        human_tree = left
        constant_tree = right
    else:
        human_tree = right
        constant_tree = left

    constant_tree = [calculate_monkey_tree(constant_tree)]

    while human_tree != "humn":
        if tree_contains_human(human_tree[0]):
            right = [calculate_monkey_tree(human_tree[2])]
            sign = human_tree[1]
            human_tree = human_tree[0]
            if sign == "+":
                constant_tree = [constant_tree, "-", right]
            elif sign == "-":
                constant_tree = [constant_tree, "+", right]
            elif sign == "*":
                constant_tree = [constant_tree, "/", right]
            elif sign == "/":
                constant_tree = [constant_tree, "*", right]
            else:
                raise Exception("Unexpected operator " + sign)
        else:
            left = [calculate_monkey_tree(human_tree[0])]
            sign = human_tree[1]
            human_tree = human_tree[2]
            if sign == "+":
                constant_tree = [constant_tree, "-", left]
            elif sign == "-":
                constant_tree = [left, "-", constant_tree]
            elif sign == "*":
                constant_tree = [constant_tree, "/", left]
            elif sign == "/":
                constant_tree = [left, "/", constant_tree]
            else:
                raise Exception("Unexpected operator " + sign)

    return calculate_monkey_tree(constant_tree)


def solve(puzzle_input):
    monkeys = [(x[:4], x[6:].split(" "))
               for x in puzzle_input.strip().split("\n")]
    monkey_tree = build_monkey_tree(monkeys)
    print(calculate_monkey_tree(monkey_tree))

    monkeys = [(x[:4], x[6:].split(" "))
               for x in puzzle_input.strip().split("\n")]
    print(calculate_human(monkeys))

    return


solve('''
fchg: 5
fvhd: 4
hjpd: ntvg * ntpl
jhph: 7
fjlh: 4
tqsb: 2
slwq: zjzs + zctz
cqfs: 3
qtlm: 4
sdsb: 2
lfcq: 2
nlvv: 5
zgcl: wqgd * zfbp
tqvl: 4
qvds: wcmp * nsvf
npcg: 3
wlqd: 2
nslf: 4
vfsl: wfdf + qpts
tjft: wltb + jhdm
dhmp: rrwd * shpj
tbtc: 3
lgdv: 9
ftsd: vgqq + qsfp
ldfn: 5
tvbh: 4
jvht: jpqn * mlcb
jdvr: vlgs * nzwm
pjbm: 5
rzcl: chdb * tbfz
ltdt: fzgw + grlf
rwbt: zzpr * tlzs
bfrd: 14
dfwg: dpqr * tgff
wqwm: 3
vbmh: vtln * jbbw
rppb: gfgz * sjmz
dmrz: tjft / jtnw
wsjc: dwvm + bjsd
msqm: vpnm * jzzh
dwdv: 5
njsc: wngz * hdrg
fbzr: 14
wqdp: 5
dpzc: wsqn * zsrr
jgwr: 7
wfcz: mqrf - hbrq
rgfr: 3
fpgs: 2
tbfz: zfvz * fngz
mfbv: ltfv * mlzd
fmvh: cnmh + cljv
swft: bnlp * pdgl
mrnp: bldf + zhtv
wpms: rjnl + hnps
pzzm: dpls / cvgg
wpsf: 18
phtj: gbjw + wfmc
sptt: 12
wcjj: 2
hgmj: sstv + qzhb
fpnf: qmrq + bfcq
prwp: mdhb - nlfw
hzzf: jfpn + lvcm
jrrg: 5
rbwf: qqvm / sjsp
bpgt: 3
wngz: 4
sdjd: 3
hnbf: hddn / sghh
cvzn: 2
tnlj: lbgm + ghsw
jcqf: 2
shpj: lggg + wbcn
mwgp: 11
wrwt: cghm / nzgd
wpsm: 16
rprv: 5
nmcj: whhl * hjtv
jlnn: tdjl + lmmw
mlfr: 3
fjds: hblb + swft
bqns: qjng + rppb
tsrw: 3
gdhf: 3
gbsb: 5
qpgq: tgdl * vlzn
wdhn: 2
qfqv: 3
vvdb: 3
cfhv: 2
nqzd: bllq * jpgb
bjpv: tcrp * fhdl
thdm: 7
dthc: sdgf + ltfn
gndh: swtp * lfts
svjb: 12
dsqp: 4
fwhd: 3
ctlr: mljd + dhzm
fhmr: 3
frrd: nvpf * bgjp
mlcb: 4
gbjs: 2
gmcs: 2
jfpt: 5
nzbc: 5
rglv: scmj + lcbh
cjqh: 5
czdp: ndfm * szdh
jllb: 2
fcfv: rrtv * cgqj
mvmw: 4
rsrz: sdjz + llcg
rcrh: bcfp * rtjd
dfsw: 1
qmfh: fzrv + vgqs
tssz: 4
wphf: cvtc + hnfl
mztw: 2
bjwz: 5
dsmr: 4
mtqq: rhtv + sqfb
mbjm: phmb + snzb
nzds: vgdr + gnwt
jdrn: 9
wnsj: 2
zgqn: 2
tjnv: qbcg / csfn
fhcv: dctp * bhpw
pvgt: cnlj * rvww
fqlw: 5
tpbf: 4
crvv: ngsv - cwbn
pwtv: 7
mpss: 3
dbwp: rjst * tgnh
wzzd: lmvz * bfqg
qsnc: 14
mfjq: 5
nbcq: 4
rfvv: 3
vpnm: 5
dgwm: 5
btdd: 2
cbcl: vlts + mzcw
fjmd: nsqr * vfhr
njjw: vvzt * qgft
nmcr: fddz * wtzc
ggfr: 2
mczh: 4
zfbf: 10
dclg: 5
bzgj: 3
fggm: szjv + jmsw
bvww: 16
stvz: 7
szmh: 19
lclv: tpbc * zzsz
gwrh: jrrg + pvlp
mdhm: dthc * dwpr
svbj: 5
nzwm: 3
zfdg: ntgl * rgrw
wvwd: zhrt - tgfs
bqjt: 3
cqrh: 5
mwwt: cwgg * vmfd
bjdn: 2
bpwz: vtzr - cvrf
jgpt: 2
czfc: ntgv * bpgt
tdfb: hzgf * hpwz
lmzz: 3
vpcf: 1
ntwf: 7
dqcp: 2
jhts: 11
zrpn: lnpz * mllb
hdtp: cjbf * mmml
dlmt: cpcn * jzwp
qhsq: 4
hcpr: 3
rzfl: gchw * llrz
gzcn: ncmp * snfr
hrzh: 2
dfzf: 16
gmzb: 2
njcg: pzmn * vqqh
znwp: 4
nfzb: 3
dpjv: qfmh * gqsd
rvww: wpsf - rhrq
tqpv: 4
prbf: jgsz * cqzs
jttq: 10
zbsm: mhtn - bgbh
wpwr: 5
bnrz: gjdc + fqlw
bvzj: 3
lmjh: tcnv + prhw
lrjm: 4
ldqv: frgr + lqcb
qqwr: jdvr + tgwc
bmqp: 4
tzlp: tsrt * cwgp
grnp: 2
czwg: 2
pbcv: 3
mrbz: wqjf * fczv
wrlb: 5
cmdr: mmsh * npwz
mbdd: hpqc * vbww
jvfj: svvl + twch
mhjg: llff + bsnt
rgrv: 5
pzbv: 2
njgp: bzgj * rnqg
cjvp: 2
fgdv: qzbg * wszh
npcf: dclt * llzt
nzqw: 4
gsjq: 5
tvzz: cvnw * hvtg
bglm: 3
dcrc: rsdd * phft
cssf: zvhs + bhcp
bfln: 5
hjmh: 5
rjls: 4
tzrp: 5
trgm: dvtc - zhss
ghhj: jhtc * wrfq
bbll: 3
nzpt: ltdt + dbnv
slft: mmcn * fcwt
pnhc: 3
mpgt: mwqt + vlnh
wqjf: 3
nwfq: 3
vpqz: 11
gvlz: 3
hrlt: 3
psph: jbpv + thds
hbqq: 16
bqbt: 2
qdwv: trfc + cswj
qzsj: 19
gwnz: 3
vnvl: 5
tjrj: qpmc - hgjr
wvqf: 3
brws: 3
bsrr: 11
grst: 20
lvpf: gzsf + bvsm
lzcn: 2
fhvw: humn - jchs
jbmf: ggpd * bljw
gwwf: 3
pwpn: 2
ftnw: szbv + sdws
lcvf: bdbh - rnft
mqqr: fbmb * jjqs
nqgd: jflp - rmmb
rssw: 4
dcjs: wnjm * rssw
rscg: fdhj * zcvc
lsvp: trhb * znvd
bqlh: jwvq * nhrq
rltm: 4
hcsb: 9
mvgc: 2
wrnn: rthw + jwnt
bprw: 3
jzvl: 4
fvct: 2
hrdp: lvpz * lfgv
chdb: hwbf * mmbt
blwr: 3
jvlz: 7
cjnw: gngd * fwmw
sqcr: scvq * dmzl
nbqm: pjnl - zgmg
sgpw: qmwq * bfnt
jjtn: ldjm + nvld
pznw: 4
dpzm: zwqv - ffqb
mlbf: jhrz * mcqq
bjzb: 2
nlps: 15
phwz: mcmg - rfrr
mgsd: 4
bcbd: brqw / dwhp
shhc: hrbm / sfdp
lmlr: 2
lpmh: 4
rswb: mpgt + dsvv
chbm: pwpn * djsq
gpwj: bltz + trvb
phmp: slbb * dqnm
scwl: fwpr + ntdl
gmbj: 5
gmgn: ftnw * bcmt
vrcs: 1
rbgm: jttt + zdpn
pmtw: 3
npvz: ltmq - zqgd
lddb: 10
dfnc: dcjm + dwwv
fftm: 5
lchj: 9
qwwh: 6
lngv: pmbl * wgdc
wnsd: jfgq * pvnc
cqzf: 1
wcmp: 2
fczv: whjf * ffwp
vpvb: hlzb * bnvt
lvls: 5
lmfw: dlnf / ddtn
pdtj: 2
hnmp: 2
dhhw: flwn + jsmh
ngmh: 2
dzff: 7
wlzs: zzng * cvrt
pgwj: 1
mcqn: glht * cfhv
qptt: 2
jrhp: jlpm + tcwm
dmmr: bzlt * jjpv
rwpg: 13
qhgh: mdzr * zbcs
pqwr: phqq - ctdq
sjbt: 5
mtbg: 12
vbrc: fhmr + rmvl
nrww: 3
dlfj: hhsz + cpzc
jtcj: 8
whpl: 5
bltw: cssf - plrv
ffdn: rnjh - zmmp
bmhn: 2
bqtb: qhlp * dnrn
dsgj: 2
dwsp: 3
njnq: 9
jpqn: 2
vflt: zpcw + dcjp
cvqw: ztdq * rgrv
tcrp: psnc / lhfg
pqwf: 3
jllq: 5
hppd: rswb * pfnd
mrtl: 16
pvlp: 3
dwpr: 11
fpvb: 2
bjrj: mcqn + jzgp
hdsp: ttdt * mczm
hrsn: 3
dmqv: 2
zbfv: lnbr * zfdw
vwdj: drfv * ncjd
rjst: mzcf + zldn
bdsp: qclb + qrjr
pmqr: 1
lpjz: brhh - zdjv
dfpv: llhn * wpzc
pwjn: nmvg + szrd
qsll: 4
jsbw: 5
wgdr: rpmz + qbdz
clgl: fjss / gbjs
wrfr: pzpz * lfwp
pnvj: qrjc / zlpf
btmp: lbdb * fzwh
dbmd: 11
wszs: nnjm * lcdn
lbgm: vnpf * wzlh
mvgt: rsrz * sbzp
wlnf: 9
tfvm: drvf * cmrg
rmbn: cbnq + crwn
gszb: vqpf + brbg
tcbw: 3
hsvl: 1
mtbv: gbhm + hlfl
gwld: gmqt / mdgn
wzww: dwhq + hfch
zldn: zlbm * mwls
jcjj: 3
zzzc: 2
gdvz: 13
zzpg: 3
mlrp: 2
mqng: 2
nntf: 5
cqbr: 5
nhrt: 3
zgdg: 3
qrjc: tvbh * ngng
cbcf: 6
hrtp: 6
nssj: gslf * tcsl
llff: 7
dlgh: 13
lswr: lmrl * nvwj
gqws: 2
ncjd: frsc * jcng
bgzs: 6
tgwc: fcjj / mlrp
wwsc: 4
whgn: hgbb * qpsr
qhvs: tsrw * vmqz
fbdg: jlgj * mlfr
qdbt: 2
cmbw: ggsl + dlfg
qwwg: bnlg * gbtv
nvwj: 5
brwm: tqhm - pvpm
dtfj: zsfr - hdjh
snfr: 2
pmfs: 2
bljw: 2
mczm: 3
bhmj: jcpz * dqfd
fswn: qcvv - fbsb
ptff: dbjl * bvvd
cwch: hgjq * wfhm
ggvb: wgrl + cqzf
prgh: qggf * nwsv
tmqv: bhjq + hsvn
wldt: 2
hfsw: fzvw / dgzg
ttwd: 2
ctzw: 13
rwss: hcjw / rvpf
cgdd: jhts + zbfv
sghh: 2
mhws: srft * lhmq
qfcf: pzzm - jtrs
pdsj: mvjf * hshp
bhcp: rnwm + bsfr
vsvb: 9
lsbc: rtmg + gtjw
lmrn: 17
vlnh: lltb * ggfr
cgrs: 1
trwt: 5
vbww: 3
bzps: bqbm * fpvt
dddb: 3
qsnq: rzbs + dhmp
nzgd: 2
tnbj: 10
rtlf: wpnd * hpdb
mdhq: 4
qnzf: gbjm * slrq
lfnn: jsfv * flwj
dmtr: wfft * gwmn
mmcn: 3
rqwt: tmvt * drml
rvbv: 2
zrnf: 3
gszl: 2
lnwp: 2
ldlt: prgr * tpzc
rdsv: rjls + lwbb
sstv: cdtv * qmdj
lhrp: sdzn + lwsp
tcwm: tqsb * pbsd
rrtr: njcm * nnzg
zrjq: nznr / bccw
wfps: 8
hpwz: jcpq * ttrs
qmwq: 3
qgft: 2
fmjl: 5
jcfg: 17
bngt: 7
wzgz: 9
pdqp: 3
mncm: 19
fzzp: qjqr * spnd
mcmj: vqrw + ccpr
jdfz: 2
nhjs: mjdq + mdhq
bpwh: 1
fzgw: nrrr * ngmh
hqsf: svbj * pjch
rflz: 4
zhrt: wlzs + qvhf
glqg: 9
qdhg: 1
whqf: jdlj * mwmv
dhwc: lsbc + brcv
psws: nzzh + nfwb
rswg: rtnc + zgcl
trfr: 2
dnzt: bqgb * hbtf
nhgc: nvfr * fcnl
jmdf: 5
psnc: vflt * jcsc
mlhj: pwtv * nhrt
tsrt: 4
ltdw: 5
sjsp: 3
mwls: 7
hmnm: 10
gjcw: 3
fwpr: pswr + bcbg
lhcm: vzrs * jbqj
llhn: 3
hwnm: tlgw + qdwv
rchm: 2
sttd: 3
dhgd: pzwm + bzhc
lcfj: 17
bcdt: btbc / rzgq
vnhf: bgql + nzqz
fhnr: 4
jtlf: jbjl * vncg
qnqz: jglm * bjvw
dctp: 2
jnbv: hshd + nscv
qnst: 2
vsdt: qpdh * dmqq
lffg: thtq / tsbm
stsz: 14
qfhf: 3
njcm: lmfw + mlgg
pfsq: 2
ppcf: qjfj + bnrb
pgmj: gvnz + zmqr
nwsv: 5
qhgc: 5
jltt: fgdv + zbhp
vplr: tpbf * ffbj
brdn: chfb + hcsb
rjrf: 4
mlzd: 2
hmgn: djbw * hzwp
rhrq: 4
btbc: hfsw - stdj
lwnq: 11
jsfv: 4
fpvt: grmh * jgsv
dmqq: 3
trms: nvsf + qfst
bhpw: mssb / wgvh
lmdn: 2
ggvl: mrtl + jgtq
pqvv: lflw * mtqq
jmsw: 3
lnhh: zbjp + btqs
sfdp: 2
qhjl: 3
dpqg: 2
qrff: 2
gsch: 4
nvhd: jjtn * gmcs
dzdq: 4
tzvw: 8
lvmh: bdfs * wbqz
jtmt: hqrm / lmdn
gjfh: ffgz / nqsv
cpzp: qncm + wdwf
nzzw: 3
pwdf: 7
wjrt: 2
ffdf: mqqr / zpzp
dsrz: 2
ddjn: 5
cljj: nljj + gzch
hcwd: gtqp - jlwb
scfs: qsnq - pblr
pgbh: mznv + sldh
rpmz: tght + dlfz
qpzb: vnrf * mfnp
vqdd: 7
jmnz: lpzl * fpgs
stfm: 4
mjdq: hpzw / twrn
gdww: bfsb / cjqh
fdvd: 2
rscn: 11
bsdh: fbfg * mfbv
zphm: psnv * tsvc
ttds: vhpg * pmhs
cvtc: 1
sptq: 4
jchv: 8
jwnv: 3
tfdh: 2
ndph: slcv + rrvj
jtwc: cngl * fdvd
nggs: 6
cmrg: vpvz * ppvh
gtqp: qjqd / lvls
tflh: 4
tshp: cnlh + hsvl
slht: 5
lnpw: 2
mzdb: jqng + ghlb
jzlh: 2
zqzw: vnrz * cqpj
nsqr: 4
nwvw: 3
htqz: 8
vlzn: zssf + tnnc
fcwt: vhmn / cqtt
tjlv: 3
jszs: zztq * mgjb
bmvb: hrbj * cmdr
vlgs: tvzh * zjvw
tgtg: thnc / cdgd
ghsw: bdzl * qdmt
cwgg: gmbs + mchq
cvnw: 12
zhgz: 2
rtmg: 2
tlzs: 2
srqs: 5
wnwq: jbnf - zwrn
nlnw: hzhf + ztvc
drvf: 13
mfnz: 5
lqtm: trqf + mlhj
dhnp: 2
dtrf: gwws * jhnh
ggml: rmbm + tjdp
mggf: 3
zfdd: 2
npwz: 3
zlbm: 9
dzcg: 2
hshp: 3
cntz: dclg * jvht
mrgs: dmcl - zmql
slpm: tqlz + jfpz
ggmm: 3
mcqq: 7
nnfb: gflj * smfn
dhzm: hbjt + rmbr
pzdl: 2
zcvv: szfd + msqm
trhb: 2
rdvh: 7
pwpl: 2
qddq: 5
vpgp: 5
vssc: zwqj * cmbv
dmhj: flqq - cwvp
gbsr: 2
jzrg: 10
vgwn: 2
hqft: 10
cqzs: 5
sbzd: 4
btdt: phtj - ndlf
flmc: wwss + zdvp
svfr: qzwt + nhgz
jhnh: htfq * qbzh
bfvq: 3
zrzv: lnnq + gnjv
wbvm: 2
tqzf: 3
nvvv: dgbn * spcb
sqjf: 3
dmhb: 2
vvlw: 3
wmcv: mdqz * ctmt
hbgd: hspj * sbcs
vpss: zrfv + nvtd
zztq: 3
wnlr: ddlb + qpgq
vlfp: 2
plqr: vhjz + cbcl
mjdp: ljpr * nbcq
scjv: hdrp * cmnq
jgtq: hgbw * hmgn
vzlt: gcjm + jjch
twpl: jtmh + pgwj
jfmw: 3
jcpq: hjmh + wwhp
fqss: jgpt * sgrn
dbfb: nhwd * tzzw
lrtt: 7
whjf: vbmh + pqwf
lmrz: 2
bcbg: bbll * nbsm
twbn: 19
chmd: 3
vtdt: 5
jhrz: 11
tvzh: 3
vbqt: 2
fwqc: czfc - rrzv
ltmj: 5
hdfz: dhtf / fjmd
glfw: 3
wsjt: hcwd * bbdf
jrpm: 4
vgmt: lfbg + wfps
nwjp: lfbm / fbgq
qlrc: 2
bhcl: 3
qmsm: mrbz / nlwl
nhvw: 5
ndfm: lhlp * bhcl
lgrv: lzfz + tlsq
bvwd: 2
gtgv: snvw / jtmt
ttrs: 2
pgpb: bhmj * nssh
qrnh: bmvj + zhth
prhw: lpbs * dqbq
jmqd: 4
rqjg: 3
hvdj: vwqb + qgnt
bnlg: 3
pmpl: 2
cwqv: 14
gzwc: 3
tnbb: 2
jdlt: hzpm / lnwp
sfqj: 4
bzdc: qsjj * rfwp
vmnl: qbrf / mpdd
mdmd: 2
bbhm: 7
vsmd: btmp * hgmr
hccl: gdzl / trfr
pvtr: 9
dmwb: slwq + qbqs
qqhs: hqft + gdvz
dtpc: rgrf + rftg
bdwd: 13
grlf: qcrv * bbhq
pzlw: 5
hjqb: 2
bgvq: hwtj + ltzc
vrzd: 4
zqmf: qfzj - msnn
mgtt: bbhm * fpvb
tbzr: 3
ndhs: tnlj + hdvz
qzfj: 4
vtmn: tqmb * bbvl
znnf: rvbv * rscn
lncs: qzsj - ngjc
ntgl: 5
jpsg: 7
cjbf: fzwg + rsqm
djfz: vjlz + hhtb
ztdq: 5
qpdh: 3
qmrq: 2
qzwt: 3
cwvj: 17
cmnh: 3
dzqj: 6
bdfs: tghr + mwhf
lndz: 7
lbpg: 4
vcgb: glnl * blwr
hrwm: 2
rvwz: lshr + lnmz
vpwg: 16
wslc: bdcv * jdrn
jtqr: qvds + pdsj
zmqr: lhpr * qldd
fprp: 11
jqrh: 2
vnvw: 2
vlss: 2
qpgm: whhb * vmrr
wmzq: spwg / wghp
qjqr: dtrf - rlzd
qpbl: 5
qbhd: pjbm * sjwq
vnmd: gjgs * ghhj
nsjz: jbqr + vhzd
wfmc: jnwq / vnbp
mdmv: mvns + vdjc
hcjw: rsfb * rvfw
nwmp: hrwm * qfcf
gwmn: 5
zhss: 3
qgpl: 10
pfnd: sqjf * fmjh
rsfb: nvhd / tfcr
clrl: 2
vnrf: 3
hzgf: 3
dhqz: sdpp + fdtp
hscz: 2
brzt: 18
qnhh: zzfj + hgtp
lgzs: 5
zvhs: hdsp * zwff
dzfr: 2
wzlh: 2
lnbr: 8
vzqg: 3
mhcm: 14
mhsz: gftz + zsqb
jwtg: lqgn + gqtd
qbzh: 5
slpf: 2
pzpz: 4
jjzv: brwm * rgfr
zfzt: 5
mmml: rgvf * tnbr
llnc: 2
vsqp: pjmr + cmlh
sjbj: ppvc * gsjq
hfvv: wslc - whqf
rthw: 11
bldf: nmrt * fldp
nntd: 6
jnzb: csfh * rfmr
dlfd: fjds * ltld
vhht: 3
mfbs: rmdr + ftsd
dbqm: vsvb + zptg
wshh: 4
vjln: 2
stzh: wrpm * qtlm
hqrm: mlsc * jpsg
swcq: 2
ndgc: 7
fmvz: hbbq * czwg
gqcz: 13
ztdn: tnmd + npqp
cpnv: nbqm / tgtg
mpbs: 2
cmtt: 4
rrzv: nnfq + cmtt
vdgf: mqcq * qhvn
wzrt: lngv - zpfz
hzcm: rsnb * vpll
qtdg: fbfh + wngv
gnfz: dwsp + dfzf
ndvf: 19
bdfc: qgff + tlhq
zjvw: btsb - trgm
wtmt: wtqc * pmtw
lvcm: 5
rnwt: nwpf * qgzj
pzgh: 2
gnwb: 7
bdbh: dbmd * vbgc
gphc: cdlq * tbzt
fmjh: 2
rmpd: 12
bgjj: 11
qpqh: tzds + hjzv
dvtc: zfzt + slht
fwzp: 3
hvtg: 4
bzhc: bhlh * fqvz
npbc: fmvh + hwrj
bfcq: jrmq * clwh
bbbm: tmbj * cjfg
dhdz: vcrt * tsbj
hgzm: 2
whfd: htzb + zfgc
lttm: 2
lrnh: 5
hnst: sbbv * bjhh
vbjz: sldf * gwwf
gqmp: 5
szbv: rjdm + jttj
zjrv: dhhw * pdtj
qmtz: zqvq * zdjn
cfch: twbn + pgbb
ttfc: lmvh * wmbv
jwnt: lmrz * svfr
nqhm: 13
qnwn: czwj / hgmg
gcds: 5
thjf: rwns * nczd
ztbw: rlcm + vsrf
gnfc: 3
fqmn: 13
fglb: lcpf * cgqs
sltt: nztr * hpnp
fttp: 2
nsfp: zlvt + qzzm
zhth: lqld + bvww
tght: cvff * wszs
rhqz: 2
gjdc: btfw + njcc
dphc: zhvf + fvlq
cswj: plvg - fmth
jnwq: bdnr * fvct
cngl: 8
snjd: 9
jcng: 2
rstn: nfbt + tsgb
shzb: mfmv * dmgs
ndlf: ngfz + gbpd
vcrl: lswr / rrbl
pjmr: tmnn - mwgb
nwrq: nsfp * mqng
drml: 4
rjwg: qgpl + fjnt
qtfw: 4
dqnm: gtcw * bjbt
cnmh: dwph * tqzf
szdh: ddbh * bdfc
zbnv: tjnv * qlfg
glnl: cgcm + wjsb
gbjm: tnzz * dmfw
rjsj: gszl * bshw
cjrh: wjrt * gzwc
snzb: thgv * bfln
hwpq: 2
rsqv: 2
qgff: ffdf * tcfw
lhvj: 5
vrcg: nwjp + bqtb
tlsc: 3
wltb: snvj * prqz
rsrb: 2
hhch: 5
pbfn: hhch * mdbh
hcgs: 18
hvjb: cmql + mgtt
wsmd: 2
rjtc: 2
ctjg: pnqn + dfwh
gflj: fggm * hljd
glzb: vpcf + vlmj
btrb: nzds * rhtd
ptrb: 2
zfrq: 5
sbcs: 2
tnhf: 2
dgbn: 2
hfch: 11
zwgp: 2
rnsn: 3
psjq: 6
jmln: 9
mgnw: 4
hcsf: hzcm / dpcj
fqjt: qtbp + nfcp
jlwb: dvrg * wwsc
rgrf: pzcv + cfzn
chth: tlgz * rgnt
trqf: zmhp * ltwn
cphq: 2
mnrt: qqjf + fwlc
cqtt: vqws * dhjp
mjms: gwsq + glzb
ffbj: 2
hwtj: wgss + hzmw
bfct: jszs / ltbc
zlvt: 18
lldv: rbgm + dgwm
wlcr: vdgf + gllg
hljd: 2
sjpq: 1
bvzm: qbhd - rttm
gmvc: rpzm * nntp
fvzh: 14
trmz: tqqh * vpff
prtw: 20
pvvt: hlzl + dlmt
qmdj: nmcr + spcv
nlwf: pqfh * csct
bqgb: 4
bvnq: mztw * cbnw
sdfb: swwc + dzhw
cwmz: 2
swwc: stcn / wdqz
zfgc: jmnh * mdmm
ltdh: 3
jwdv: zfcr * dhjw
hddn: fmjl * sptt
bsfr: wtmt + fwfq
rzwp: 5
zzfj: 6
bbwp: tflh + jtcj
rmbr: snjd + qwwh
nvsf: mhsb + rscg
fwzc: shtm - mvmw
njsw: dccg * mzvs
rlzd: crpd + tstq
rbcb: czbw - tqpv
cnlh: dhtj * bpjv
rlcm: 1
twqn: 3
csvm: 7
fhqw: qcbc / rsrb
vllt: 3
wgvh: ppzb + zmss
jmnh: wzww + vqdr
pgsd: 2
whhb: vlpr * nzzw
fnrq: dlfd - tjjh
ttcb: qrff * gphc
sglf: mjgq * dtpc
mhtn: djhj * lbpg
vvmd: 2
qctq: lncs + tqjz
ltvl: 12
cmsl: qgbs + qtvs
gnhm: brvq + vldd
qsdz: 3
dnqf: 3
lcbh: 8
spnd: 5
wpzc: 11
pjsf: qzpn * rzwp
rhht: qtfw + nhld
fgbl: 15
fqvz: zhfh + vfmq
dbmf: 3
flwj: 4
rmzh: 3
rjgc: 4
snpq: cfch + fjtz
zqjr: 2
htsd: 5
qjqd: mzvc + wwmv
gfpc: 2
dfrp: lrmn * llql
ppvh: 2
rmhm: vnhf * pmlw
vhgd: zjfs * zgtw
rfrr: 5
zhcf: ffdv * qzqh
rmzr: bcbd + gqcb
qvfb: trqs * njgp
qgmr: 5
sncv: vjnf * gszb
cwmw: 3
wtnn: vpbr - fcfv
zfvc: 13
gztr: dcvd - dgnd
sptr: 4
hwrr: dbfb + rjsj
zsrr: hfvv + pfwc
slrq: 2
twrn: 2
qpsr: 7
fdjt: 3
pwvl: ptcl + fwqh
csct: 7
vtcl: jbwr + rbdh
phlq: 2
ntpl: wnnc * pwjn
zzpr: 9
bpjv: 7
hpzw: jqss * zfdd
lbdb: 2
bvbp: 4
gllg: wlcn * tqzz
hdlj: 1
vdgc: 14
dbbw: twmt * vhgd
gpdv: 2
plfn: cwmz * gvlz
ldhd: wsgj * ffdn
cgtp: 2
bbqc: 4
znsz: pngn * qvsp
dcjp: tcjp + lzgf
wnml: 14
gbcl: bgzs + gzvn
mgjb: 4
tcvr: 5
nhtm: 3
jmnv: rvmz + bvzm
vncg: dnzt + strv
ddff: 10
twfn: qbnc * tvtg
zjzs: 2
vgqq: 4
mwnv: 2
cdlq: 3
tvtg: 5
wpnd: pqvq + qqhs
dtbc: jwtj * vsqp
mjgq: 13
ffqb: 8
gbhm: 3
hbtg: mjcr * mqmq
zgtw: qnzf - nlqv
lsdg: 2
qlfg: 3
grff: 5
jbjl: 2
qwsj: 3
zhfh: 6
psnv: 3
zfzp: 12
vhzd: 17
nnqn: stfm * nmgp
gght: hscz * lrtg
rtzl: qhhc * rcbb
gcwd: 2
tssg: 2
qsgr: sgcc * wpdr
jhdm: mjdp * fjlh
lnmz: dfwg + vcbz
hmnh: wchg / qhgc
bwbl: 1
bgql: 4
bjbt: hhbl + dbpn
nhpv: 2
lrdv: rzfl + hwdd
hjbf: 3
vwng: 4
vmrc: hgff * tbjv
hvpt: rqwt + pfnq
lwqz: hvww / zrwf
rqzl: 2
qzqg: 2
zhlj: ndsm / rvnn
lstf: hfws * cwvj
wtqc: 9
jzpr: qwwg * pzgh
lwwb: 2
wgqs: rnws / mvmf
pcjl: 15
wrfq: 2
njsn: jmln + mrgs
vbhn: rmhm + jjns
zmss: 5
vmrr: 3
vcrt: wpbb * hvgq
qnvz: slnd * dlqv
zwbl: 4
fjtz: 6
vgqs: 2
zdnj: 2
flrj: 9
fzrv: 5
qfmh: vssc + hccl
ljpr: 5
djqv: 2
jzwp: 2
mwhf: fdvq * ssps
lqgn: tzlp + fnfs
pgbb: 4
nfwb: dsgj * bgvq
cscp: 2
ltld: 3
zhvf: 3
rfwp: 3
sswd: ftlh + fplh
gbvl: 1
brps: 2
pnqn: 4
vfnh: 2
dqbq: 3
tzpt: 1
jpvl: 2
cbrg: 4
csfh: bgwv + mjjz
tcqg: rbwf + vpwg
ztvc: 1
ngng: mdbg * nwsd
dqsh: pzlw * wcjj
dzjq: 4
bjhh: 2
vlts: qwfj * mlfd
vtgm: 4
gqcb: wclj * lhrp
pqfp: bcbv + lhbr
cqcm: cmpm * wmfv
qbhr: wnml * cbzs
brhh: nhtm * rfvr
hgmr: 2
pgrq: hdtp + psws
pftt: 2
gztw: 3
gtqm: qczq + dzdq
wwpw: qqtj * rzml
vltb: 2
pgvp: tssg * jnbv
cghm: tvsv * dbwp
lhmq: 2
vlmj: bzdc + bssz
mcvt: 2
hhsz: dtpg * prbf
ppzb: 1
czbc: tczr + slpf
nnzg: 4
lwtd: vzmc * ttwd
pbln: vgvp * gjbd
ffrs: 2
vqqh: zhrn / zgdg
grqp: 2
hbrq: jfmw * djqv
tqnd: 6
rmvl: 8
jfpz: jqrh * jjmv
rmwh: 11
lvzt: fglb - fqss
bdcr: 4
lzfz: wmdq - shql
mpvb: vprd - vcfn
ccch: 18
bzlt: 3
zrfv: 5
ggdg: cphq * dmbs
gjgm: pzdl * blzn
cmpm: 5
hbtf: 2
wlzl: czdw * nnsj
fdtp: qgmr + wphf
mthm: jmcg + dlfj
dfwh: 3
ntvg: 17
rzbs: lnsv * pmtp
ngsv: gqws * vshz
hhbl: sgbt * wgzn
jdgh: wrbt / pmfs
qtvs: mfrs * fvfs
bnvt: 5
dlbt: 4
phqq: nttr + zlzq
jqbl: 3
cfzn: 13
dszn: 5
qtgg: 1
zmmp: dhwc - rwss
zbhp: cqrh + jmnv
tblf: njjw / jpvl
ndjh: 3
hztf: 3
rrbw: 2
dqfd: 3
vvzt: prcj + hrhl
pspq: dsvz * bqcz
drnl: bpsz * ssdw
wclj: 15
lmmw: rwpg * dzhz
qqtj: 3
zpfn: dbqm + dbrd
cbnw: 11
qcvv: vfzp * jwdv
zjmw: zflg + bzrn
pfnq: 1
mmbt: 2
wlcn: pwbl * dzqj
jhtc: 3
qbdz: 8
mfrs: nwfq * bvwd
hgbw: 20
qrsq: ggvl + mfbs
mbbm: jjcl * gncw
qzhw: hjpd - jzvr
dlqv: 7
bwsq: mpss + jmgj
vqws: 2
qdqr: nfgv * rglv
dchw: 3
wrpm: 3
fzwg: lfcq * bbqc
lpdr: jgwr * stvz
mmsh: 3
jglm: 2
frjt: nqhm * vddb
hzvv: zblw + njrm
hzwp: 3
czzm: 1
jqng: gbhn + tqvl
qvhf: rrbw + zntq
dfzz: szsh + cwch
lmnn: jvbh * fdjt
hsrf: mbps / ptpl
wdqz: 5
cbrv: 7
dmfw: gdhf + mtzt
jmll: 2
fhfg: zqdl - dfsw
ntmv: 19
rnwp: hfdc + vpqp
lwbq: jswd * gcds
mjcr: jbtb + gmwl
zsfr: zprb + mqtv
rvnn: 2
vbfz: pqgb * mcmj
fzvw: dfrp * fmvz
nvmb: mzdb * tzqz
fvlq: 4
nwss: 5
drzg: jtlf + mhvn
snzj: pgvp / hmrd
hwgh: 3
wszh: nqbm * hrtp
mdvf: wpds * qhgh
cqqr: bstf - mwgt
cjgp: hrzb + jdlt
wwmv: hwrr + rzqd
tgzw: 5
gbwj: zvgh * wvfg
jmcg: wcvt * npwq
jfpf: plqr + ldhd
sdtm: tnbb * nmdg
ddlb: zcrl / bglm
qbsh: 9
lcdn: 9
zrff: 2
gtzb: fqrm + grqp
snbb: 2
wwss: 11
vpvz: 5
bhzf: pgpb * tmwt
pnnt: 6
cfgq: 3
qtbp: 4
bhfj: 13
vnbp: 2
rlrr: 4
dcwm: gchz + prgh
hcbt: 2
tsgb: 4
lrtg: 5
pqgb: 3
pvpm: 1
fplh: bcdt * zrnf
stcn: snzj * cvqw
csgw: gjzp / lnpw
zfvz: 13
nthv: 5
cthp: 10
jmgj: 4
mnfq: 2
lvpz: 19
rgrw: 2
whtn: 5
gcjm: gvss * dlbf
tgfs: cljj * zfdg
rmdr: bzcl * szmh
vhpg: ndph + nvmb
pmbl: hzls + gdjg
gpsj: 13
fnfs: pcjl + llqn
tpzc: 3
phwf: tdfb + dzdf
tvwc: 1
gqsd: dcwm * bscb
nhld: 3
tmzz: 2
lnnq: 14
cnww: gcrr * wnsj
mljd: pfvv - fvfc
bqcz: 5
dpcj: 2
cvgg: 3
sdjz: 6
fhdl: 3
qvrg: 1
llbf: 2
gftz: lsvp * sswd
bdcv: 9
sjgf: bjwz * wdhn
nhrq: tttm + ltmj
qftw: vcdg * wnlr
zjnw: fhvw / qptt
wvvn: jzrg * nggs
dbrd: dnmq * twgf
lmvh: 14
zjfs: 3
mqcj: fbzr * pzfd
bqbm: 2
tcjp: 2
ncsp: 2
dgzg: 2
czrw: mrzj * tptp
fbfh: gnwb * gdww
frsc: qfjv / rfvv
wnjd: pqvv + cthp
ctqj: vrcs + tnbj
cnsr: 5
hpzq: 4
jztg: tvzz - tgzw
ngfz: qgwz + wdwg
dznm: gztw + srqs
wdwg: nsgd * jdth
bfnt: 3
vcjv: hrdh + nrww
jpgb: 2
czdw: ppcf * mthg
ftft: 3
lfbg: qvcr + drnl
wsgj: 11
hmwp: 2
cmlh: prtw + fqjt
fspt: tnwz + jttq
zzvp: crrl + zhpb
wgrl: 10
nczd: lgdv + tmfb
nssh: 3
pdgl: vhht * zmth
tqlz: 5
slnd: 2
tftj: zpfn + crqs
htrg: npvz / cghg
fmth: 1
vlcl: 3
zmcz: mbqp * gmhw
gmqt: nsjz + ppvr
wgpc: 5
wfts: fwzp * pgrq
ccfq: gnfc * fjrv
tmnn: gpmz + pvqj
vnpf: 6
lqcb: 13
tsbm: lfnn / cscp
rhtd: 2
lwfm: qtgg + jvfj
nztr: 4
humn: 721
zrtr: 3
wmdq: vhmw * mpvb
sqfw: 2
nntp: 3
jczp: 5
gjgr: ngsz + tznr
vddb: 7
cqpj: lpvq * lbjf
vhst: bmjj + zrpn
hshd: 4
vgdr: 15
rpgs: 6
tmbj: jqbl * bnfw
llqn: vfnh * rjgc
hrbm: zcvv + nbrt
tmzp: 2
hwbf: 3
vprd: ldmv + ldlt
qpts: zlpv + czrw
jlgj: 3
pzwm: 4
qmzb: wlcc + dcbm
ztbc: 4
vtsh: jvfm * bglc
wmfv: 2
mbps: dztc + tplh
pslj: hvdr * fqfv
mtzt: 4
hwdd: dmhb * tnmj
pwjq: 3
tcsl: chbm + nbfl
gvnz: pbln / mbmd
zvhh: 1
nbch: hnbf - dqsh
sbbv: dmmr / cgzf
vwmb: mdvf + bcwn
dnqh: 5
wfhm: tpdj + vlcl
hrhl: vvmd * dbns
lrhp: shhc + gtwp
wzzv: pwpl * gvnb
qhhr: 15
dclt: zbsm + brdn
rbdh: 14
bjsd: 15
ltwn: 4
nbrn: ttvd * tmzp
lrmn: 2
swtp: jzpr + bsrr
jpsm: 2
btfw: 6
rvjq: lqjn + vpgp
mqrf: nmcj + msfn
dncn: qsgr - lrjm
mwsp: 11
zcpw: 2
qbnc: 2
ssps: 3
rjqm: cghs * jzdv
tjjl: ghtd + cbcf
hjmn: cpzp + hcvz
zgmg: btbb * pqwr
mflh: 5
tqmb: wmzq + clqj
lflw: 2
vhjz: jbfl * qnvz
svvl: 3
qcgt: ztdn - zjtq
zptg: vtdt * rwrh
qcrv: 3
tnmj: 4
frpz: 4
brbg: 4
bgmc: wcfz + pvwn
qltz: 5
root: hppd + czdp
crwj: pdqp + sjgf
srnz: 5
fqrm: cwmw * sbrn
rnqg: pnvj - zvhh
pflr: bgmc + qnhh
cbnq: bdwd + jzhp
sbzp: 3
mghf: 4
hvsz: 13
hcjq: jhbj + ztqz
mznv: 6
slcv: grst + qzbv
gmsz: pbcv * ttcb
wgmq: qpqd * dbvm
zqdl: 7
dbns: ldgn + vsdt
hgtp: qwnd * dslw
ddbh: dcrc + mthm
npjg: 6
zbjp: cntb * gnhm
ffbn: 2
mdqz: smmq / qhvs
pzfd: bwsq * rdsv
bdzl: 7
ftwr: 4
fwfq: vbfz + snpq
gwsq: 3
ngzn: mgdb + fhqw
blzn: zcws * fttp
jsdt: jfzh + dwdv
cvrf: btbd * dmrz
lzgf: 4
hgjq: 3
gnfg: qnqz * qwsj
wnfd: rqjg * jnzb
nhwd: 5
vvvs: 4
gdsd: pvgt / rvqh
mllb: brjj + vcjv
brqw: gwlf * nzpt
dwph: mslq - jfjf
hwqr: 2
dbnv: jnsh - gjgr
pmhs: mngp + qdhg
cfwz: jltc + bngt
gtwp: zvmf + jmnz
ptcl: 1
ctmt: 3
qmjh: 4
fcmr: jzlh * zrzv
mzqt: 3
cbzs: 2
thgv: bfhg + bzts
rvpf: 2
gbjw: zmsn * wwmm
jpjv: 9
rglj: lcfj + nbch
rzgq: 6
mnld: 2
rlmt: cntz + wnjd
rrbl: 5
trmd: 3
mfqp: jcjj * tcqg
thds: gmvc + tzpt
fdvq: 7
hdqg: 12
bssg: vsmd * hptn
dmnl: wzzv + lldv
mngp: hbbd * mdmd
hptn: 2
pbpf: 2
hbbd: 3
jflp: tshp - bwdn
sgtj: dvnn - sbzd
ldlr: 2
lmrl: zzpp * vlfp
ltht: 9
smfn: 2
vshz: jfpt * tgnl
dhjw: 5
nvtm: 2
pvnc: zhgz + mmmq
ltfn: cvhr * twqn
cpzc: ntwf * lhtf
hjvp: 5
mthw: vmrc + smpr
jfgq: 2
qzbv: 13
tznr: 15
bwqn: 3
wghp: 2
dwhq: 2
nltl: 3
strv: 1
cqws: 3
qbcg: pgbh * zzvp
mgfn: qmzb + cqcm
gmbs: 11
vbgj: 4
crqs: cfjg + whmn
szsh: ttfc + blsf
trqs: 14
ngsz: sjdd / pmpl
djvg: cpnv + tvrv
lwbb: 3
gzch: 14
ghtd: 5
dwwv: jhzj * dhgd
tgff: bjpv - rltm
hhqb: hmnm + zmrf
twmt: dmqv * gjcw
jbqr: bdsp + wgdr
vhmw: 5
dpqr: qmjh * gfvf
plrv: gczc / tmcj
bncf: 2
gjgs: 19
bbtr: sdtm + fhtv
lwwj: lhvj + mdbr
srtj: 4
tmwt: 6
nfbt: 3
bdvg: 13
czbw: 17
sgjl: gtzb * qnwm
dmpl: 3
qpqd: 3
rtcm: 5
dvrg: ggml + sjbj
zzrq: wfmw + lrhp
mflt: 2
sfvc: 6
jtnf: 4
cgzf: 3
hrbj: 3
vprg: 14
gslf: 3
fvfj: 3
zcfz: 6
gnwt: 2
rsqm: 5
zblw: cbtd + pnnt
hpqc: mzqt * nfzb
tbjv: 5
gbzp: wjrb * tqwn
ttfw: jlnn - mthw
nnsh: 11
jbtb: 9
qpmc: 9
mhvn: 10
bnrr: dqwn * zcfz
qbzf: 3
dsvv: qzhw / ffbn
dsvz: 2
twjr: 2
rrvj: lgqf * wtlf
trfs: 2
cmnq: 5
mrpz: mhzh * dbmf
spcv: 5
lzrz: dpzm * wvwd
nvtd: mbbm * pznw
thnc: hfdb * lzdv
gqtd: 6
zlzq: qvqz + zfvc
pbhs: 2
sqzj: mrbj * jhph
qgzj: 3
wcfz: nqzd * crph
jpzz: 4
tdjl: 4
btbd: 3
jdlj: 2
hvlt: sglv - zfzp
zssf: wrnn * ndvf
zbcs: 4
wngv: twfn * bvnq
lnsv: vtcl * bbdh
dmpf: vnmd + jnsf
hltd: 4
jfzh: 2
bccw: 2
bnrb: njsw * lwqz
frst: rcnm * ccfq
vzrs: nbrn / pwjq
npnt: 4
jqbh: sltt + wqdp
bzcl: 3
qggf: hlwh * crdm
nbsm: 2
fzqs: 3
mgdb: jgnr * hcbt
ggpd: 6
zmhp: 2
hgvq: rnwt - pjss
nttr: 5
qhlp: wmzg * zlmz
nmwc: twwv * rpwg
vpff: 4
hjqh: gscz + nqgd
vnsp: vjsg + crwb
gncw: 3
dcvp: slfg * pgsd
scvs: tbzr * mncm
nzzh: mczh * wrlb
rnwm: hcgp / nvtm
qncm: rjdl * lssr
gwws: pftt * cfgg
nlqv: 5
zfbp: 2
dzdf: fchg * jchv
qbrf: dctw + pbfn
lggg: ttds + lgrv
hpnp: 6
mfnj: 2
wvfg: 2
cqfg: 5
gztj: hgzm * qsvf
csbg: hqhm + bfvq
jzzh: 5
vlpr: 3
whsj: 3
cmbv: rzcl + sbzz
brjj: lcjr * zhcf
ftlh: 11
qgnt: mwnv + cbrg
nmdg: 4
sldf: 2
zspq: swqh * mhlv
whhl: 2
bnfv: 14
thrc: qctq + htqz
bblj: qftw * mhsz
zhtv: gbwj / zbpj
mvjf: 3
njzs: sljl + wpwr
wchg: ctjg * tzrp
dvnn: 15
mqtv: rtwt + pnhv
lzcp: mbqg + tfdh
snvj: zzpg * jjmj
qzqh: vzqg + fzqs
bzts: cfdf * gsch
fbmb: 2
fhtv: wnsd + dtbs
mwqt: fzzp + crvv
bvvd: pbbp + ngzn
sqgr: hjqh * bqfr
pnhv: cqws * qhnp
hpcs: vhst * gbsr
nfcp: njsn + qqvl
jgsv: dfnc / jrpm
hdrp: 2
dmbs: clvh - ltht
mbqg: qzvh + hdlj
tghr: 10
whmn: sqcr + lpdr
nsvf: 17
twns: vllt * dmpf
gdjg: bjrj * wldt
fjrv: 11
czwj: ctlr * wnmh
crwb: zqmf * whfd
ddtn: 2
tfcr: 2
lgqf: cjvp + mbdd
dpls: mqcj + htrg
fwmw: 2
fjng: 5
slbb: 4
mthg: 3
vjsg: gpjc * twns
drnt: nwrq - dwfp
lhbr: dpjv + vzfl
nfgv: vbrh * lpmh
lzvh: prwp / bvbp
njqv: 4
fzwh: vcrs + mgsd
fpgw: zzrq / wsmd
mhcd: trmd + gzcn
lbjf: 7
dwfp: nnfb * chrh
sztg: zbnv + ctbm
hzhf: 7
jhzj: mnwq * wlqd
wmbv: 5
gzsf: 2
jjch: dsjn * qpgm
hfdb: 7
nlwl: 3
wnjm: bhrd + sgjl
cwvp: bbpl * nzhs
hdjh: 11
bbpl: qqmc * snmj
rtmn: 9
ftpn: lrql - nrrj
npwq: 6
mbqp: 2
vvhl: mcfl * vpvb
cdmg: qmnw + dltq
mcfl: ztvl * flrq
qlpp: wzgn + wjjd
nwpf: bhzf + shzg
wbbv: 3
mmcr: ztbw * hjvp
pblr: sjhh * hpcs
mmmq: 9
hhtb: 4
whcf: ltgh * cwcg
jjgr: 5
nrwg: 1
qnms: 2
sqfb: 4
jqtt: hvsz * twjr
pwbl: 3
cvhr: 2
jrmq: 3
bfsb: zlbt * hrsn
trfc: 18
rjbc: 12
dlbf: 2
zbpj: 2
fwqv: 19
bgwb: nwvw * cbrv
hgjr: 2
gjbd: 3
hjzv: hdqg + lzps
mwmv: nlnw + tbtc
sdws: 1
tsbj: qdbt + trwt
rtnc: bbdm * bgwb
qclb: vvph * drch
mjjz: 9
bhjq: 3
vcbz: dncn * lldw
mhsb: bfrd * sfqj
szrd: mphf * hvmj
dwvm: 1
jgsz: 5
qvqz: qlrc * jllq
hgbb: vltb + tssz
ngpw: 3
hgff: 2
fddz: 3
cghg: 2
ntdl: pgmj * trfs
htdz: qfhf * crwj
lfgv: 2
mdmm: 11
fqjf: cshv * vbjz
qfst: sqgr + dcrf
fbfg: scwl - cmbw
cgvd: 2
tstq: 1
brcv: qtdg * sqfw
sjwq: 5
nmvg: pnbg + zhrb
bpsz: 3
clsj: 5
qsfp: gnfg + fvhd
chrh: 2
wdwf: vpjv + cvhj
zcws: 11
lcjr: 5
crpd: 6
jjpv: bvms - wwjr
mqrj: 20
vnrz: 6
nrrj: cqfg * qvrm
wgjb: 3
nljj: 5
lhtf: tzgb / psjq
hpdb: pgzh * vvdb
prpb: vwng * mnbd
lfwp: 2
mnwq: 8
frcq: 2
nmrt: mztr - tjjl
mrzq: 2
nzqz: 19
pmtp: nhjs * csbg
jttj: 6
vdsm: rhht + gmnz
wcvt: vlqf + zjrv
gtcw: 3
tnnc: drpc * gpwj
bhfb: 2
njcc: 7
flqq: wlcr / vnvl
rsnb: 17
dccg: cdlg * ggmm
vhss: 10
pvwn: 19
stpv: 4
jbwr: 5
djsq: 16
bwgm: cgvd * mwwt
lnzl: 5
rfmr: 2
grmh: 2
jbnf: 13
tgnl: 5
phmb: btdt * ntmv
zvbj: 10
ctdq: dnqf * swnb
rtwt: 2
fzdc: bqns + qnwn
mssb: lqnc + mmcr
dzhz: 3
dnmq: 13
qrgv: gztr + ltvl
dltq: 5
cvff: 2
bcbv: vvhl + wlzl
jvbh: 5
jdrw: lmzz * gbsb
qzzm: fwqc + qmtz
mfmv: ztbc + jvlz
nbsd: 3
bglc: tdnw + brzt
hwsb: pblp + dczv
wmzg: 2
mslq: jmqd * whfz
lnvq: vqcr + rtlf
pbhh: bflz * frpz
twgf: 10
qqjh: 4
lvvt: 2
zdjv: 2
bstf: phlq * hqnj
rtdf: htsd * ntzg
zvgh: mrpz + zspq
srwc: 5
bwlh: bjzb * zdzj
gscz: 3
jdwm: 5
rrpg: wnfd / njhn
mwgb: 5
vcqb: mjms / snbb
njhn: hrlt * vnvw
llrz: 3
btqs: rvwz / jpsm
dzhw: czrb * qsnc
vqdr: fqjf / grnp
fvfs: 6
pqfh: 5
zwqv: lrrd + jldf
thpf: jdwm * dqcp
mrzj: 4
gjrq: 3
zlqv: psph * rprv
jcpz: 3
sgrn: hcgb + ljhg
hnps: tjlv * wsjc
vqpf: 3
lqjn: 2
rgnt: 5
zpzp: 2
pswr: 2
vgcf: 9
slfg: 5
bshw: 7
hcgb: 5
lfph: hnmp * bmvb
hmrd: 2
pmlw: mnld * gnfz
qsjj: 7
mfnp: 2
vmqz: 2
qsvf: jmdf * wgjb
zdvp: rvjq + gmbj
hfdc: 5
vpbr: wtdg + qrnh
zfmc: 1
zlgw: wgmq * lmnn
vtln: 2
jldf: cmnh * rbcb
znvs: lwwj + wvvn
rtjd: nntd * hpzq
sjdd: qzqg * cnww
btsb: lmlr * gmgn
zrvc: 3
hrdh: sthr * hmwt
mlhq: 7
pmzs: zthj * whtn
jwtj: 2
hbbq: 4
gpjc: cjgp - rcfm
blzj: bpwh + ddff
mqcq: 19
ttvd: czgm * zhlj
nnmv: tplb * qzfj
zrwf: 2
tmfh: 2
mqmq: 11
gnjv: 3
gbpd: chth + wzrt
sztf: qqbf / dbww
hmmt: tfcn + ddjn
snvw: jsdt * fspt
fqfv: qhsq + swnv
tbzt: 3
prgr: 3
dtpg: 5
wqgd: 4
qrjr: 9
vqrw: 6
mzvc: qhzz * wgqs
jltc: 12
lqld: ffrs * qpbl
bcwn: cqqr / zzzc
bqjn: jcqf + fvlh
shtm: mlhh * fbdg
lpbs: fmzc + vmnl
jlpm: 14
bbvl: 2
wfdf: zfhs * ltdw
tcnv: ggdg * wmcv
znbn: 4
nznr: 14
sqtt: bltw * hvpt
rmmb: nbsd * ndjh
tmvt: 4
mlgg: scnr + bblj
jzvr: hcjq / ctqj
nsgd: 3
bgjp: fwqv - cjrh
tpfs: dszn * cmsl
tgsc: 18
qnwm: 8
tcfw: rpgs * fbbv
jdth: 12
bdnr: hvlt - qcgt
jchs: scts * jztg
gcns: brps * dchw
hdrg: 2
cjfg: rfhn + pslj
pblp: qqwr * vbrc
dlfg: nthv * chtn
dwvt: 6
sldh: 1
cdlg: 3
jzdv: lbqw * gjfh
hjhj: 3
fwlc: gztj + sqzj
ltmq: jfpf * cmwv
zlpf: 2
hqcs: rtmn + mhcm
mdbh: phmp / dsqp
gmnz: 1
wwhp: 2
tgdl: 5
cdtv: 15
nwsd: 3
clwh: 5
wpbb: 2
jsmh: jnsg * clsj
zsqb: qvfb + zphm
mchq: qnms * ntln
zhrn: ldqv * rmzh
wsqn: lnzs * npnt
hlzl: npcf - flmc
nlfw: hdfz * bjzd
tsjb: dznm + qfhv
qhvn: hcnp + bwqn
rgqs: 2
hjfs: scfs * mtbv
hfws: 3
qnrq: rglj * mqrj
sdzn: bgjj * btdd
vrgh: nrtr + zrjq
hzpm: dlvh * cjnw
mztr: wrfr * gvgc
tczr: 5
cgqs: 3
qfjv: zjmw * tcbw
bqfr: fjng + swcq
bzrn: wvqf * nlbs
drch: 4
tnmd: rtcm * pjsf
lldw: bfct + lrtt
cvrt: 5
crdm: mhcd + qmfh
zqgd: drnt * mfnj
vfhr: 2
vjlz: 4
wrst: gcwd * cqbr
vlqf: drzg + pmqr
nqbm: 3
qmcr: 7
gtrr: 2
zdvl: gsqp * wgpc
hpdp: 10
prpd: fwbj * dgtq
lngb: 2
csfn: 7
ztfw: 3
jmhn: tzzv + jnqp
smpr: 2
jqss: 7
bltz: zcpw * scvs
jsfc: mlbf / vntw
lndq: 6
tfcn: 12
bqwv: djql + slft
bnph: 1
tvrv: hrzh * npcg
zmrf: 1
cshv: fftm * ggcc
snmj: 9
nnfq: 3
bmvj: 13
ccpr: 1
zgfh: 3
bfqg: 2
bllq: 10
jfjf: 1
cfgg: 4
gvgc: 9
hcgp: znvs * gbgz
tptp: 8
vgjd: 2
hgmg: nzqw * sntr
dlpm: lwnq * qrgv
gqqr: gqmp + zghq
sntr: 2
fngz: 2
llcg: 1
qldd: bdcr + mlhq
hqnj: vpss + wsjt
rzqd: gght * djvg
qqjf: mfnz * ncsp
swps: 4
vzmc: 19
mdgn: 2
gwlf: czzj * jzvl
vwqb: jsbw * tgfj
lwsp: tzvw * zgfh
jwvq: 2
vljr: 19
jjns: gmqs + hbgd
zpfz: wzgz * wsmq
rvqh: 4
jtnw: 2
ffwp: 5
tqjz: vgjd * tlsc
cntb: 5
chfb: 2
mzcf: qzrf + dlgh
zhrb: 16
dlfz: lqtm * pnhc
vvph: 4
bbdf: 2
tzqz: 2
ptpl: zgqn * slmc
ptgr: 2
ssdw: hgnl + zfmc
sfzc: ldwp + cdds
wtbb: rhqz + lnzl
pzmn: 2
dcvd: hhqb * swcw
ppvc: 8
nhgz: 6
rnws: rjtc * dfjr
nrtr: tblf * rqzl
cbtd: 1
prcj: blzj * qnfl
jdqn: swps * srtj
nlbs: 10
tttz: 2
dzdv: 5
hnfl: 7
qzhb: gmsz + njzs
ncmp: 5
fnfv: 2
qmnw: 4
chtn: 5
dbpn: 16
msnn: fprp * jsfc
nfqb: 2
dslw: 5
jcsc: 2
zzng: mjzc + lvmh
crwn: gjrq * cgdd
wnnc: rrtr + lcwh
thwb: 4
bssw: fswn * llbf
wvcw: vljr + htgl
dsjn: 2
mrpw: 4
thtq: jdqn * zwbl
zcrl: zmcz * fjsz
swcw: 7
wjjd: sttd * ngpw
ltfv: srnz + ccch
wrbt: tmfh * gwld
sthr: 10
dmgs: 2
qjfj: csht * pvvt
mvns: 2
lvgs: 2
brvq: vcgb + pspq
gchw: vgcf + njsc
vbgc: 5
rhtv: 3
mzcw: jpzz * hbqd
zmsn: lrfr * wngf
swqh: ndcg * rdvh
rzjq: 3
fjss: mfjw + rstn
qvsp: ltdh + vdsm
bjvw: 3
ttqn: 4
fjsz: rtdf + dhdz
lzdv: dzjq + qhjl
jttt: 3
nscv: 7
tnwz: 13
qjwl: jbmf - qvrg
djql: 2
fmtc: sjbt * wbbv
bscb: mrnp / mrmm
mdbg: 3
ggsl: 6
zwrn: 2
lqnc: ndgc * bhfj
mplh: 3
qfjp: lwtd / zrff
qzrf: rrpg * vmvr
wfmw: sfvc * fcmr
zctz: 6
ffvc: 2
wpds: 13
vmfd: 2
ffdv: 2
lwhv: 2
scmj: 3
vhmn: pfwp + dcjs
zlzp: 5
scnr: zqjr * pqfp
tlgz: 6
pzcv: 11
jgcb: gfpc * cfwz
qcbc: zfwm * ffvc
mwgt: vbqt * qlzb
cljv: 1
nvfr: nwss * dmpl
tgnh: 19
zghq: sjpq + wfcz
jwwc: 14
dtbs: 20
mhzh: 13
mbmd: 3
rnjh: vwmb / lgzs
tmcj: 2
qnfl: 3
wgdc: 2
vstb: 5
jjcl: 4
glht: 5
djhj: jllb * hbqq
qjng: 8
fcnl: 4
vtzr: fjcc / pwdf
mbld: qwcd - bqwv
sgcc: rzjq * zrtr
gfgz: 2
lvmq: 13
lzps: 8
pbsd: zlzp + rjbc
ndcg: 2
rfhn: nnsh + bnph
twch: 6
jbqj: 4
tjdp: 2
mlfd: 7
tplh: whcj - trms
bflz: 2
qvrm: vzlt - jcfg
brvf: mtbg + vplr
jjgl: fvzh - bwbl
dhtf: csgw + zlgw
flwn: 6
vmvr: 3
wzgn: scjv + zdvl
ltbc: 2
hcvz: lhcm * tpfs
bfhg: 5
bnlp: llnc * frrd
ntgv: gmzb * dwvt
cwcg: 2
jbfl: 3
lfsr: 2
mcmg: hcpr + vtmn
cgqj: 2
fbbv: 13
ntzg: lvgs + hwnm
sdgf: 1
dqwn: 2
mphf: 2
zlpv: prpd - dphc
gbtv: ptgr + vstb
bnwn: 12
zpcw: 1
mjzc: lwbq + vvcp
tpbc: 5
rmbm: 5
lhfg: 2
hvww: qdph + rgnr
zqvq: 2
tttm: tvwc + wrst
zprb: lfsr * jtnf
qzpn: 3
jjmv: vhss - bttn
rfvr: 3
rpwg: 3
hlfl: 4
dsbr: hzvv + nhgc
lltb: 19
qvpv: 8
crph: jjjt * bqjt
hvmj: 3
gbhn: 3
rnft: mcvt * gcns
vjnf: mplh * hcsf
trcj: vfsl * dfpc
dmcn: frcq * mbld
rwns: grff * whpl
jnqp: jdgh + rnwp
sfrp: 3
mhlv: vbgj * jdfz
gbgz: 2
gmqs: jjzv + jgcb
pbqq: mwgp - tsbp
vcdg: 5
fwbj: 6
ldmv: sgtj * tjrj
gqgg: 3
wtlf: 4
qnvr: lwfm + ctzw
spwg: lngb + bnrr
gvnb: 5
wjsb: 1
jbpv: 3
gtjw: 20
pqvq: 8
cnlj: 2
gchz: pwvl + rcrh
gbnr: 2
gwqq: 2
mpdd: 4
djbw: sdjd * hztf
rcbb: 19
hmwt: 2
sjmz: 5
vcrq: zvbj * jwwc
mfjw: qfqv + bssg
rjdm: 4
gzhn: 2
lbqw: 3
cmwv: 2
bvsm: mflh * rqps
tnbr: 5
srft: 6
zwff: hltd + hjqb
twwv: 5
nnsj: trcj + qnrq
mvmf: 2
trnd: 4
pfwc: bnfv / lzcn
zdpn: 5
ndsm: lttm * dhvn
zthj: 2
rjnl: 11
ldjm: twpl + wpms
hjtv: 5
gzvn: stsz / vlss
zzzb: rmbn + thjf
wsbm: 2
zfhs: npjg * ztfw
lfbm: dpqg * gtgv
gjzp: lvvt * hgmj
htgl: tgsc - lndq
wbqz: 2
msfn: 19
cdgd: cvzn + tcvr
stdj: wsbm * gqcz
zdzj: 16
vfmq: 7
spcb: rdtg + gwrh
wwcs: 4
lrfr: dmwb + vdgc
bjzd: 2
nvld: ttqn * bnwn
rvmz: svjb - qbzf
wtdg: phwz + bhfb
cwgp: 2
gcrr: 16
pfwp: fzld + sdfb
tzwj: 2
fbgq: 2
zqzn: dmtr + cnsr
bmjj: mhjg * grjb
bbhq: bvzj * zfrq
mlsc: 2
vvcp: wnwq + jpjv
dhjp: 3
qfzj: lcvf * rjwg
ztqz: hvjb * ttfw
sbht: 3
dbvm: gpdv + sgpw
tqqh: 5
srdc: 4
bvms: dzfr * wtnn
thzg: 3
zntq: dzff * mvgt
dnrn: 2
smmq: gbzp * gtrr
wgss: jqtt + lvpf
rcnm: jwtg + htps
njrm: lffg * srwc
gmwl: 2
gpmz: 3
tsbp: 3
mdbr: 2
sdpp: 4
rgnr: vrgh * mflt
hdvz: pzbv * bdvg
hzmw: bqjn * ptrb
pjch: 5
clqj: lsdg * mmcc
ljhg: njnq + fgbl
zlbt: 15
nmgp: 8
wwmm: 2
hwqf: fhnr * gwqq
scts: 5
czzj: rwbt + nhvw
dcbm: vrcg + pbqq
cmql: 17
lhpr: 2
qqmc: jwnv + qvpv
fmzc: dtbc + whgn
lrrd: rmwh * jzww
jbbw: 5
drpc: 4
hspj: nnmv + nlwf
ngjc: 2
hvgq: hqcs * hwpq
rrwd: cfgq * vbhn
phft: htdz + rflz
dhfc: bnrz + pqgz
nbrt: ldfn + pfsq
tzds: 17
wlcc: 3
hgnl: 7
swnb: 3
mnbd: 16
scvq: 2
crrl: clgl + qddq
zmql: 1
nldh: 5
cpcn: czbc + thpf
tzzw: bnhm + bwlh
jqcj: 15
hgdl: 4
jjjt: 2
whcj: mggf * rgjs
jvnj: prpb + hpdp
bbdh: vcrq + wwpw
rgjs: dmcn + rtzl
hjfc: lzvh - rlmt
lssr: fqrv * wqwm
qzvh: pbpf * wshh
qvcr: 5
zqsw: wzrg + trmz
llzt: 2
zfcr: 6
qgbs: vwdj - frjt
flrq: whcf / zdnj
sbrn: 2
bfbn: 4
lfts: 2
mzwb: 3
htps: wwcs + gbnr
hqvs: njqv * fqmn
sljl: fhfg * vgwn
cvhj: qmsm * njcg
fwqh: vtgm * gbcl
sbvj: 3
rlqt: jtqr + gqqr
ldwp: 9
mzvs: dsmr + gqgg
hlwh: 2
fbsb: bwgm + qhhr
tzzv: vtsh * mvgc
nzhs: dddb * thzg
fcjj: prtl * mnfq
plvg: 14
qdph: hmwp * jvnj
qwnd: 5
hdlp: 2
tqzz: zjnw + qrsq
gjgv: 15
rgvf: 5
fjcc: hsrf + dlpm
tzgb: hzzf * zbrj
nrrr: 4
dgnd: cgtp * flrj
trvb: wvcw * jjgr
ggcc: 2
qqbf: dfzz * bqbt
vpqp: cqfs + sfzc
szjv: tttz * bmqp
mrsv: ndhs * dhnp
pbbp: znsz + fpgw
nvpf: 2
dcjm: bfbn * vgmt
jtrs: lrdv * jjgl
bhlh: 2
zmth: 5
bgwv: 2
fmwf: 18
zfdw: 5
lshr: bssw + fnrq
tgfj: lndz * bprw
sgbt: 5
dfpc: 2
ghcc: 2
hsvn: sptq * qjwl
hqhm: wtbb * shzb
zlmz: 11
znvd: btrb + tsvr
mrbj: rgqs + hmmh
dcrf: tnhf * qnvr
cwbn: 12
dfjr: hrdp - fpbf
dhtj: 6
prtl: mdmv * mwsp
cfdf: 3
dgtq: sbvj * hwqr
rvfw: 2
zcvc: jqcj * pbhs
ppvr: vcqb * slpm
gfvf: 2
czgm: 3
zbrj: mrsv / lwwb
ldgn: 4
vbrh: tltn + fmwf
zhpb: lchj + vprg
rsdd: bbtr / fnfv
rjdl: rjqm + rmzr
tmfb: 2
ltzc: mhws * bmqt
bcmt: 2
clvh: ldlr * cwqv
rzml: wpsm + czzm
shql: rlqt + dzjd
qgwz: 1
tvsv: 2
hblb: tqnd * dmhj
qqvm: fvfj * lmrn
sjhh: 2
drfv: 3
jtmh: hcgs + lrnh
blsf: 13
hzls: qnst * glqg
ltgh: hwsb + wcfh
ctbm: brvf * stzh
bnhm: 9
hbqd: wbvm * sptr
jgnr: mrpw * sztf
bbdm: 3
bgbh: 16
gczc: rswg * nhpv
tlsq: hwqf * brws
qhzz: 3
dztc: cdmg * nssj
zwqj: 5
hcnp: 8
zjtq: znnf + jdrw
wwjr: nrzt * dtcr
qqvl: 3
pjnl: bpwz * fhcv
hvdr: 5
jvfm: 5
dmzl: phwf / tzwj
lpvq: 3
zzpp: jmhn - mnrt
lhlp: hjmn * nfqb
bwdn: 2
wzrg: 2
jnsg: 3
dwhp: 2
sglv: lzcp * qpqh
nbfl: 5
wcfh: lzrz + bsdh
zzsz: 5
fqrv: 2
hbjt: zwgp * hjhj
ntln: 13
tdnw: 11
jhbj: srdc * hjfc
mzzd: zlqv * rchm
ttdt: chmd + qqjh
cgcm: 6
ngwj: 3
swnv: 3
jnsf: nntf + dtfj
tsvc: mzzd + npbc
qzbg: 3
cghs: 7
qwcd: lnhh / qsll
tltn: bmhn + qbsh
pqgz: 4
rwrh: 2
zvmf: nltl * lvzt
qjzc: 3
gvss: rlrr + hmmt
lmvz: 3
rftg: 13
wpdr: 3
qbqs: 1
qfhv: 3
pvqj: ghcc * gjgv
dbww: 2
prqz: 2
grjb: ptff + wrwt
rrtv: 10
ffgz: zzzb * nldh
bttn: 3
rttm: 3
dzjd: gzhn + nzbc
qwfj: pvtr * dzdv
btbb: rmpd + lclv
wgzn: 5
fzld: nvvv / dzcg
jlgn: gjgm / rjrf
pnbg: 7
lrql: dpzc / mrzq
cfjg: glfw * thrc
frgr: tmzz * bpmc
vpll: 2
pgzh: 2
qhnp: 13
htzb: gdsd * plfn
dczv: fwhd * sqtt
pngn: csvm * vqdd
mdzr: 2
npqp: dsrz * bqlh
bnfw: 3
wnmh: 2
wssv: qbhr / vvvs
nnjm: 3
vcfn: 13
rcfm: tftj - jltt
dhvn: jqbh + nnqn
gdzl: lwhv * bzps
lcpf: zqzw / clrl
bhrd: qltz * nlvv
jfpn: 1
dmcl: tsjb * vrzd
czrb: bncf * hgdl
hlzb: hqvs + qmcr
cdds: stpv * gwnz
bpmc: ngwj + fzdc
dctw: nwmp - mfjq
mmcc: 5
vsrf: zfbf * rnsn
tplb: mgnw * vpqz
vfzp: vvlw * thdm
jzww: 2
dlvh: zqsw + gbvl
whfz: dhfc / hdlp
llql: jlgn + bjdn
wngf: 2
hrzb: sglf + gndh
rqps: 5
htfq: 2
jnsh: djfz * fwzc
qdmt: 3
rpzm: 3
vqcr: whsj * mfqp
jzgp: 3
gngd: 13
fjnt: 1
bcfp: jrhp / sdsb
hmmh: 5
fldp: 4
lcwh: hbtg * hjfs
shzg: hnst + hvdj
dlnf: vnsp * mbjm
jjmj: dhqz - znbn
mlhh: 3
mrmm: 5
nqsv: 5
sbzz: qlpp - qpzb
gmhw: hjbf * hmnh
nrzt: 3
fpbf: 1
tsvr: pflr - wssv
tpdj: 5
fvlh: 11
bsnt: rsqv * ggvb
zfwm: qdqr - bbbm
jzhp: 8
qlzb: dbbw + mdhm
tqwn: ftft + dlbt
vgvp: fmtc + lddb
dtcr: dfpv / hwgh
dbjl: 2
szfd: 6
vzfl: ftpn * vcrl
rdtg: nlps * jczp
vldd: sbht * hqsf
jjqs: nmwc + znwp
slmc: 5
lnzs: nslf * qsdz
wfft: fpnf + bbwp
qczq: cgrs + wzzd
bssz: zrvc * sfrp
fvfc: 2
fdhj: mghf * dnqh
hwrj: mgfn + gtqm
lnpz: frst + hgvq
pfvv: pmzs + qjzc
gsqp: 2
tqhm: 12
qhhc: jtwc * mpbs
pjss: sncv - dsbr
tjjh: dmnl + zqzn
wtzc: 3
mdhb: lmjh * jmll
ztvl: 2
vntw: pbhh - nrwg
zdjn: lvmq + lfph
vpjv: sztg * lnvq
tnzz: 2
bmqt: 4
tlhq: lpjz * tmqv
lpzl: qfjp + thwb
ghlb: vjln * lstf
wjrb: 3
wbcn: wfts - tfvm
jswd: 5
vdjc: mzwb * wlnf
tlgw: 10
csht: dcvp * ftwr
zflg: trnd + gpsj
wsmq: 3
vcrs: 3
''')
