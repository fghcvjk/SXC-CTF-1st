#! /usr/bin/python2
# -*- coding: utf-8 -*-
import gmpy2
from Crypto.Util import number
from flag import flag,e1,e2

assert (e1 < 2**32)
assert (e2 < 2**32)

m = number.bytes_to_long(flag)
p = number.getPrime(1024)
q = number.getPrime(1024)
n1 = p*q
c1 = gmpy2.powmod(m,e1,n1)

n2 = number.getPrime(1024)*number.getPrime(1024)
c2 = map(int,[gmpy2.powmod(p, e1, n2),gmpy2.powmod(p, e2, n2)])
c3 = map(int,[gmpy2.powmod(e1, 3, n2),gmpy2.powmod(e2, 3, n2)])

print('n1 = ' + str(n1))
print('c1 = ' + str(c1))
print('n2 = ' + str(n2))
print('c2 = ' + (c2))
print('c3 = ' + (c3))
# n1 = 17963064878219297499926539755529525701375912229028373100173473134607394789664287607368340798794683194437682952690508928886652995386383146889003406172408614571972729531812623495934448286040540097840662578369651592616783708165933036306017892497833364373485432426417809013633924450913331047907013191887482793788688736422653892662900369700701081539738763728230752094073294005560908179016172875213907812943500460207818071050071895019325622709305548027158608131204996083137774696224909740835744016252811508782404134677682054379270633099277445509293373814980267901088167711756798567438727515561927878122737404945310578048219
# c1 = 2519784075571363990355801446319896012899269885206109823774950526790963683990153738128746190638393784786596405506731840240589533349004496866914346264165223649729391271273556253486062775839454219993404367212857109756953767455690796208791355456292865648813147954137342631589248190059107210837405220320124078796283385382994717993598412926549647978190991179177838292156516142496656655553613583148209957002024913648233539568864514049304210818483385640653620994626277688420873819215255064048179977060710057344959786809400706849894340484144098989681668420576351191631435372353088813222856086210998354107613629733847782962190
# n2 = 18724308600993680772040132476147443059937062865510694686877532603079614680086774925762072671394784787691065784432778464228230479469525602116950506124178922966302228834351364607333986401435253287986565305219407269279319145851605536263946222693062150972421981977212241191765587924831341467136660852112059970632881164690431105960074159318822853545203221878413076459098980779367764115932851271974512575031047448816911420663521305894273613218483567916755598148798190932027939210902403155767487515702073721374684377875350047635848757189883075996002319631998930528597791545501045272097478778892159675588840857142652895265911
# c2 = [3227115480108687251143827858010802848948769835037303555920483802259214819344453925631294417806432714176524195861938002549436386343852098195596387592472144546437874859798830812267011643855867112448231876484774166379425286268881326798711769931848606930434512049291154720821129654830620829493843059059835800242333615312846190103494997079811557982251508839708002883778910917631553992619052626191828854730582898255670700858011426887487070944722267353577011178466697504947762804170585435684678698950363434075952461947607646966414518037049739527149945887998812316417005423702083018805606242882095334884780205891592816168103L, 17139275485259110169718125211934888629708949924849742315041043571562307752055065297519271353044041441264892639110696891866965260187916302606640599942290472419225004160983308212078726494659784938191829066322525193057563553826485587827351089778042018829577434276292639964092632076137550347805354953807458891741631731341557365791973551073866525939105337652370251223107187937345980460911362790708353134912495192276504731259631723322913019046682545871283275754931576128656069033856416078373511440449107627433371949378696710812496517227289219196266427370667273925986284754478473526404645897976394395240810054198847661134728L]
# c3 = [281487861809153, 49947026556362417]