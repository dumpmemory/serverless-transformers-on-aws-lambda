import pytest
from src import config


@pytest.fixture
def requests():
    return {
        "texts": ['This framework generates embeddings for each input sentence',
                  'Sentences are passed as a list of string.',
                  'The quick brown fox jumps over the lazy dog.']
    }


@pytest.fixture
def response():
    return {
        'vectors': [[-1.762142330408096313e-01, 1.206010952591896057e-01, -2.936239838600158691e-01, -2.298580855131149292e-01, -8.229275792837142944e-02, 2.377093583345413208e-01, 3.399852216243743896e-01, -7.809641361236572266e-01, 1.181278675794601440e-01, 1.633740067481994629e-01, -1.377150118350982666e-01, 2.402825355529785156e-01, 4.251254796981811523e-01, 1.724179536104202271e-01, 1.052796989679336548e-01, 5.181643962860107422e-01, 6.222178414463996887e-02, 3.992859423160552979e-01, -1.816524118185043335e-01, -5.855786800384521484e-01, 4.497172683477401733e-02, -1.727504432201385498e-01, -2.684433758258819580e-01, -1.473859846591949463e-01, -1.892180442810058594e-01, 1.921506971120834351e-01, -3.838426470756530762e-01, -3.960070312023162842e-01, 4.306489229202270508e-01, -3.153194189071655273e-01, 3.659493327140808105e-01, 6.051584333181381226e-02, 3.573259115219116211e-01, 1.597363203763961792e-01, -3.009840846061706543e-01, 2.632503807544708252e-01, -3.943109810352325439e-01, 1.848553270101547241e-01, -3.995491266250610352e-01, -2.678897678852081299e-01, -5.451174378395080566e-01, -3.134060651063919067e-02, -4.306440055370330811e-01, 1.332782506942749023e-01, -1.747937947511672974e-01, -4.354656040668487549e-01, -4.773788452148437500e-01, 7.125558704137802124e-02, -7.370020449161529541e-02, 5.691370368003845215e-01, -2.825797796249389648e-01, 5.249750241637229919e-02, -8.200080394744873047e-01, 1.982968002557754517e-01, 1.695117801427841187e-01, 2.717802226543426514e-01, 2.646110653877258301e-01, -2.557394839823246002e-02, -1.740963160991668701e-01, 1.633144766092300415e-01, -3.952611088752746582e-01, -3.175597637891769409e-02, -2.625561356544494629e-01, 3.527543842792510986e-01, 3.014345467090606689e-01, -1.471974998712539673e-01, 2.100759595632553101e-01, -1.840105354785919189e-01, -4.128958582878112793e-01, 4.147755205631256104e-01, -1.897691041231155396e-01, -1.354821026325225830e-01, -3.792723119258880615e-01, -4.680226370692253113e-02, -3.336004167795181274e-02, 9.003944694995880127e-02, -3.301327526569366455e-01, -3.873167559504508972e-02, 3.750822842121124268e-01, -1.469965875148773193e-01, 4.349598586559295654e-01, 5.383257269859313965e-01, -2.654454112052917480e-01, 1.644457727670669556e-01, 4.170784354209899902e-01, -4.725078865885734558e-02, -7.487314194440841675e-02, -4.262605905532836914e-01, -1.969945430755615234e-01, 6.103179603815078735e-02, -4.742631316184997559e-01, -6.483347415924072266e-01, 3.714625239372253418e-01, 2.509568929672241211e-01, 1.225298494100570679e-01, 8.887653797864913940e-02, -1.067240089178085327e-01, 5.339851230382919312e-02, 9.745053946971893311e-02, -3.466571122407913208e-02, -1.028828322887420654e-01, 2.322889268398284912e-01, -2.537398934364318848e-01, -5.131123065948486328e-01, 1.852160990238189697e-01, -3.043577075004577637e-01, -3.552089631557464600e-02, -1.269750446081161499e-01, -7.716330140829086304e-02, -5.153301954269409180e-01, -2.280719429254531860e-01, 2.033434994518756866e-02, 7.381757348775863647e-02, -1.525584012269973755e-01, -4.008376300334930420e-01, -2.477492988109588623e-01, 3.974704742431640625e-01, -2.602606117725372314e-01, 2.509060800075531006e-01, 1.682287901639938354e-01, 1.339003145694732666e-01, -2.108344808220863342e-02, -4.700354337692260742e-01, 4.788500964641571045e-01, 2.803455591201782227e-01, -4.645468294620513916e-01, 3.217469453811645508e-01, 2.342072576284408569e-01, 2.457724511623382568e-01, -4.714821279048919678e-01, 5.004014968872070312e-01, 4.101898968219757080e-01, 5.152167677879333496e-01, 2.625494301319122314e-01, 2.115933038294315338e-02, -3.896875083446502686e-01, -2.417427897453308105e-01, -2.148346602916717529e-01, -8.626504242420196533e-02, -1.653234362602233887e-01, -5.218933522701263428e-02, 3.418747484683990479e-01, 4.503143727779388428e-01, -3.069733977317810059e-01, -2.022944092750549316e-01, 6.855217218399047852e-01, -5.338923335075378418e-01, 3.584715127944946289e-01, 1.452866494655609131e-01, -7.070577144622802734e-02, -1.505292356014251709e-01, -8.562794327735900879e-02, -7.678513973951339722e-02, 1.895446479320526123e-01, -1.040674969553947449e-01, 5.335438251495361328e-01, -5.278869867324829102e-01, 2.423308603465557098e-02, -2.643479108810424805e-01, -2.231865972280502319e-01, -3.812087774276733398e-01, 7.599139958620071411e-02, -4.644850194454193115e-01, -3.365494608879089355e-01, 4.212298393249511719e-01, 1.074794009327888489e-01, 1.904578208923339844e-01, 2.894973149523139000e-03, -1.085136681795120239e-01, 1.535454690456390381e-01, 3.160231411457061768e-01, -2.708382718265056610e-02, -5.405944585800170898e-01, 8.972890675067901611e-02, -1.155498400330543518e-01, 3.978038132190704346e-01, -4.976834058761596680e-01, -2.848933637142181396e-01, 4.998634755611419678e-02, 3.612796962261199951e-01, 6.905353069305419922e-01, 1.468216478824615479e-01, 1.733965277671813965e-01, -1.745821088552474976e-01, -3.157024085521697998e-01, 6.730007380247116089e-02, 2.172500193119049072e-01, 9.785352647304534912e-02, -1.294724792242050171e-01, -1.869295537471771240e-01, 1.348781287670135498e-01,
                         -1.538850963115692139e-01, 7.447167485952377319e-02, -1.855361759662628174e-01, -2.806282639503479004e-01, -1.141442880034446716e-01, 4.122495949268341064e-01, 6.394940614700317383e-02, -1.457153260707855225e-01, -9.820619970560073853e-02, -1.330819427967071533e-01, -1.884108334779739380e-01, -2.848415635526180267e-02, -3.495096787810325623e-02, 3.342579305171966553e-02, 6.988976150751113892e-02, 1.903543323278427124e-01, -2.967241406440734863e-01, 2.646947046741843224e-03, 1.091409251093864441e-01, 1.708933338522911072e-02, 2.605892121791839600e-01, 3.290384411811828613e-01, -6.615598499774932861e-02, 2.396654188632965088e-01, -2.261948734521865845e-01, -3.368677198886871338e-02, 1.494003832340240479e-01, -3.212654292583465576e-01, -2.685779333114624023e-01, 5.726315975189208984e-01, -4.923083186149597168e-01, 2.006668746471405029e-01, -3.492617011070251465e-01, -2.898878604173660278e-02, 6.090103387832641602e-01, -5.723330974578857422e-01, 2.350005209445953369e-01, 6.471671629697084427e-03, -3.149505332112312317e-02, 2.781099453568458557e-02, -3.903406262397766113e-01, -2.089497298002243042e-01, -3.044527471065521240e-01, -7.201950252056121826e-02, -8.298408985137939453e-02, 3.737927079200744629e-01, 7.389393448829650879e-02, -2.210726961493492126e-02, 9.881400316953659058e-02, -1.514267623424530029e-01, -1.404307633638381958e-01, 2.260178029537200928e-01, 2.760902643203735352e-01, -8.877505362033843994e-02, -1.128159686923027039e-01, -2.662860751152038574e-01, 2.778344750404357910e-01, -4.756131395697593689e-02, 6.710069626569747925e-02, -2.785863541066646576e-02, -2.399928681552410126e-02, 2.517086863517761230e-01, 4.687937498092651367e-01, -5.393254756927490234e-01, 1.105985268950462341e-01, -3.449472188949584961e-01, 4.159896969795227051e-01, 7.284827530384063721e-02, -3.196474611759185791e-01, 4.903741478919982910e-01, -7.303585298359394073e-03, -2.642561215907335281e-03, 9.637111425399780273e-01, 3.238849043846130371e-01, -7.796172052621841431e-02, -2.375894188880920410e-01, 2.340381741523742676e-01, -3.160540759563446045e-01, -1.656696782447397709e-03, -1.090706586837768555e+00, 3.384092152118682861e-01, 4.706051200628280640e-02, 1.074354574084281921e-01, -2.066721320152282715e-01, 4.264194052666425705e-03, -1.384751172736287117e-03, -5.314556956291198730e-01, -2.756482958793640137e-01, -1.646486371755599976e-01, -3.429162204265594482e-01, -4.261189103126525879e-01, 6.018121242523193359e-01, 4.559717774391174316e-01, -2.727017998695373535e-01, -3.458075225353240967e-02, 2.627523541450500488e-01, -6.341892760246992111e-03, 2.796310782432556152e-01, -2.535589039325714111e-01, -1.686263829469680786e-01, 3.829357400536537170e-02, 2.077634185552597046e-01, -4.315258562564849854e-01, -7.239980250597000122e-02, -1.268542557954788208e-01, 2.070293202996253967e-02, 5.744414329528808594e-01, 3.546725511550903320e-01, 9.283009171485900879e-02, 6.705061346292495728e-02, 1.115204244852066040e-01, -1.865123026072978973e-02, 4.623519778251647949e-01, 2.725045979022979736e-01, -3.604742288589477539e-01, 5.294152498245239258e-01, -1.003212062641978264e-03, -8.813624083995819092e-02, 1.499755829572677612e-01, 5.258591473102569580e-02, 4.635176062583923340e-01, -3.968313336372375488e-01, 2.426403164863586426e-01, -2.089123725891113281e-01, 3.656721115112304688e-01, -4.735508700832724571e-04, 5.339631438255310059e-01, -1.978794932365417480e-01, 3.115830123424530029e-01, -6.967152953147888184e-01, -4.295006096363067627e-01, -4.493593871593475342e-01, -2.713678032159805298e-02, -6.987117230892181396e-02, 2.061746418476104736e-01, -1.571076959371566772e-01, 4.435211718082427979e-01, -6.742671132087707520e-02, -3.009242713451385498e-01, 5.148594379425048828e-01, 3.360294699668884277e-01, 6.633765250444412231e-02, -1.152352169156074524e-01, -2.959796600043773651e-02, 2.794718444347381592e-01, -3.481988236308097839e-02, -7.293223589658737183e-02, -4.584729671478271484e-02, 1.542629599571228027e-01, 8.093562722206115723e-01, 5.203280448913574219e-01, -4.021146893501281738e-01, -3.231527656316757202e-02, -1.103639751672744751e-01, 7.505026459693908691e-02, -1.510986685752868652e-01, 8.457400202751159668e-01, -1.808441281318664551e-01, 3.225733637809753418e-01, 1.047080457210540771e-01, 3.196638524532318115e-01, -1.550855338573455811e-01, 1.692366600036621094e-01, -2.569966018199920654e-01, 2.012090384960174561e-01, 1.773930937051773071e-01, -2.743332386016845703e-01, -3.369442522525787354e-01, 5.023568868637084961e-01, -1.183573007583618164e-01, -2.011669576168060303e-01, -5.364859104156494141e-01, -7.698090374469757080e-02, 1.153794955462217331e-02, -2.364642918109893799e-01, -2.987704798579216003e-02, 1.313665360212326050e-01, 2.941844761371612549e-01, 9.909154474735260010e-02, -5.438975691795349121e-01, 1.408130675554275513e-01, 3.669986426830291748e-01, 5.048625171184539795e-02, 1.991224288940429688e-01, -2.806745469570159912e-01, 4.341922402381896973e-01, -1.402750909328460693e-01, 5.780487656593322754e-01, 1.777157634496688843e-01, 8.983647078275680542e-02, 3.296516537666320801e-01, 6.130084767937660217e-02, -3.249333500862121582e-01],
                        [3.220873475074768066e-01, -1.239313278347253799e-03, 1.793740540742874146e-01, -3.691916763782501221e-01, -6.460254639387130737e-02, 9.153671562671661377e-02, 2.411911040544509888e-01, -2.949422895908355713e-01, 7.728967815637588501e-02, 1.157702207565307617e-01, -4.479986801743507385e-02, 1.792827546596527100e-01, 1.475359350442886353e-01, 2.151165902614593506e-01, 3.681079149246215820e-01, 2.091092020273208618e-01, 2.719422578811645508e-01, 3.488005101680755615e-01, -5.725189447402954102e-01, -1.825320869684219360e-01, 4.448955357074737549e-01, 2.745294272899627686e-01, 4.266280680894851685e-02, -7.683566957712173462e-02, 1.868916153907775879e-01, 4.496503174304962158e-01, -1.693259030580520630e-01, -2.489633411169052124e-01, -2.047924995422363281e-01, 4.028501510620117188e-01, -2.101926207542419434e-01, 3.775680437684059143e-02, 7.848539203405380249e-02, 1.284843087196350098e-01, 2.593061327934265137e-02, 4.715599715709686279e-01, 1.785378158092498779e-01, -7.379743456840515137e-02, 8.130741119384765625e-02, -2.332873344421386719e-01, -4.980126619338989258e-01, -4.135714471340179443e-02, -1.209461018443107605e-01, 1.702897548675537109e-01, -1.915408521890640259e-01, -3.845985531806945801e-01, -7.747915387153625488e-01, -1.062273234128952026e-01, -2.304487377405166626e-01, 4.024147689342498779e-01, -8.745088577270507812e-01, 2.385370880365371704e-01, -4.712987244129180908e-01, 2.126221209764480591e-01, 3.340933322906494141e-01, -2.415401339530944824e-01, -1.483509540557861328e-01, -1.451357752084732056e-01, -3.483093380928039551e-01, -8.349202573299407959e-02, -6.909726858139038086e-01, -2.984526455402374268e-01, -1.223049387335777283e-01, 7.482658326625823975e-02, -1.877558678388595581e-01, -3.754654824733734131e-01, 2.136952728033065796e-01, -1.009642779827117920e-01, -1.223443225026130676e-01, 3.143149614334106445e-01, -2.398996949195861816e-01, 2.246076464653015137e-01, 3.996007889509201050e-02, 3.603481054306030273e-01, -5.663804411888122559e-01, 2.188350707292556763e-01, 1.102031245827674866e-01, -1.087081879377365112e-01, 7.084076106548309326e-02, -2.608161605894565582e-02, 1.837034225463867188e-01, 8.465936034917831421e-02, -2.047823071479797363e-01, -2.443560957908630371e-01, -8.180584013462066650e-02, -1.903086900711059570e-02, -3.591400757431983948e-02, 2.398450858891010284e-02, -2.855857014656066895e-01, 7.374799251556396484e-02, -2.974424064159393311e-01, -8.771786093711853027e-01, 4.710197150707244873e-01, -4.940467700362205505e-02, 3.639449179172515869e-01, 4.826440811157226562e-01, 1.564634218811988831e-02, 3.558915480971336365e-02, -2.620298564434051514e-01, -1.121847182512283325e-01, 2.411031164228916168e-02, 3.747780621051788330e-01, -9.897301346063613892e-02, -9.851840138435363770e-02, 1.500086337327957153e-01, 6.895607803016901016e-03, -1.265247017145156860e-01, -3.159892857074737549e-01, 3.144952654838562012e-01, -2.942563295364379883e-01, -2.694102823734283447e-01, 2.022118419408798218e-01, 1.432989835739135742e-01, -1.958461403846740723e-01, -3.410446345806121826e-01, -3.172732889652252197e-02, 7.365031838417053223e-01, 3.192348778247833252e-01, 2.438131272792816162e-01, 3.073262274265289307e-01, 9.933231025934219360e-02, 1.901090294122695923e-01, -1.069451048970222473e-01, 5.178655311465263367e-02, 3.233431279659271240e-02, -1.031463071703910828e-01, 2.649920284748077393e-01, 3.120644390583038330e-01, 4.315259754657745361e-01, -6.426120996475219727e-01, 8.409559726715087891e-02, -4.327352344989776611e-02, -4.991196468472480774e-02, -1.271858215332031250e-01, 1.378916352987289429e-01, 1.306246872991323471e-02, 3.438322246074676514e-01, 9.234275668859481812e-02, -9.922754019498825073e-02, -5.215995907783508301e-01, 2.584226131439208984e-01, -1.057167630642652512e-02, -4.781659226864576340e-03, 3.938866034150123596e-02, 1.908608973026275635e-01, 3.293388485908508301e-01, -2.434513717889785767e-01, -7.328316569328308105e-02, -3.928004205226898193e-01, 1.454180181026458740e-01, 3.283953368663787842e-01, -4.184615612030029297e-02, 7.407122105360031128e-02, -7.386051416397094727e-01, -9.075982123613357544e-02, 1.580233424901962280e-01, -9.780049324035644531e-02, -2.160598188638687134e-01, -3.002744615077972412e-01, 2.323656082153320312e-01, 1.072475314140319824e-02, 4.957046508789062500e-01, 4.974841699004173279e-02, 2.993140518665313721e-01, -5.382250621914863586e-02, 3.532811999320983887e-01, 3.419177234172821045e-01, 4.966728389263153076e-01, -4.860525131225585938e-01, -1.909886747598648071e-01, 8.154573440551757812e-01, 2.296263128519058228e-01, -3.207779824733734131e-01, -3.272672891616821289e-01, -3.677168786525726318e-01, 3.452117443084716797e-01, -2.620116993784904480e-02, -1.431507021188735962e-01, 1.064844354987144470e-01, -2.463801801204681396e-01, -9.366600215435028076e-02, 1.719863712787628174e-01, -8.508807420730590820e-02, 2.012029290199279785e-01, -5.879214033484458923e-02, -3.402101099491119385e-01, -1.956532895565032959e-01, 2.828088104724884033e-01, 2.012428641319274902e-01, -8.207251131534576416e-02, 9.779152274131774902e-02, -2.637499868869781494e-01,
                        1.217653453350067139e-01, -1.041472330689430237e-02, -4.385982751846313477e-01, 1.105825379490852356e-01, 4.801034629344940186e-01, -1.098195090889930725e-01, -6.375459432601928711e-01, 2.933678328990936279e-01, -1.920764893293380737e-01, 4.653698205947875977e-01, 2.704200744628906250e-01, 1.938849985599517822e-01, 1.737902462482452393e-01, -3.007701635360717773e-01, -2.751181833446025848e-02, -2.291271276772022247e-02, 3.678463995456695557e-01, 2.492175623774528503e-02, 5.370550751686096191e-01, 1.885121315717697144e-01, -1.334442049264907837e-01, 8.917348831892013550e-02, 5.542919784784317017e-02, -2.481835782527923584e-01, -4.199777916073799133e-02, 5.767389386892318726e-02, -1.827879101037979126e-01, -4.168645739555358887e-01, 1.607060581445693970e-01, -4.636249840259552002e-01, 1.176923438906669617e-01, -3.770689666271209717e-01, 2.960372157394886017e-02, 6.925609111785888672e-01, -4.830894172191619873e-01, 2.112836986780166626e-01, 1.821453720331192017e-01, -1.842960864305496216e-01, 6.817662715911865234e-02, -2.460883930325508118e-02, -1.907362788915634155e-01, -6.736993044614791870e-02, -5.670071244239807129e-01, -2.392930537462234497e-01, -8.497231453657150269e-02, 3.093983046710491180e-02, 3.107990920543670654e-01, 1.291628479957580566e-01, 5.248226970434188843e-02, -3.344979882240295410e-01, 1.881012320518493652e-01, 2.354713529348373413e-01, -1.834763679653406143e-03, 4.536155760288238525e-01, 2.488507777452468872e-01, -5.641095340251922607e-02, -2.977458834648132324e-01, -4.351175129413604736e-01, -7.969439774751663208e-02, -1.767016202211380005e-01, -1.334709078073501587e-01, 1.938273310661315918e-01, 2.200260609388351440e-01, -1.105752289295196533e-01, 2.647372484207153320e-01, -2.717908024787902832e-01, 3.410907089710235596e-02, -4.771438837051391602e-01, 4.471905529499053955e-01, -5.570406094193458557e-02, 3.964374661445617676e-01, 2.748323678970336914e-01, 3.330560624599456787e-01, -1.089023798704147339e-01, 2.788817584514617920e-01, 2.159695178270339966e-01, -5.252279341220855713e-02, -3.586752712726593018e-01, -6.906290650367736816e-01, 3.960205614566802979e-02, 6.527704186737537384e-03, -1.095331553369760513e-02, -1.002768501639366150e-01, 4.770006984472274780e-02, -3.414691686630249023e-01, -1.671415418386459351e-01, 7.136443257331848145e-02, -1.807848662137985229e-01, -3.024845421314239502e-01, -6.842871308326721191e-01, -9.592869877815246582e-02, -2.141110748052597046e-01, -6.552440524101257324e-01, 5.675646066665649414e-01, 2.694673240184783936e-01, -1.900700037367641926e-03, 8.618065118789672852e-01, 1.677159219980239868e-01, 3.102787584066390991e-02, -2.677303850650787354e-01, -7.830285280942916870e-02, -4.851088523864746094e-01, -2.673721611499786377e-01, -3.335425853729248047e-01, -5.738252401351928711e-01, 3.567825555801391602e-01, 8.993595838546752930e-02, -1.305717229843139648e-01, -1.513648182153701782e-01, -6.124149262905120850e-02, -1.303707212209701538e-01, 5.585607290267944336e-01, 6.141750812530517578e-01, -4.804052039980888367e-02, -6.388589739799499512e-02, 8.390594273805618286e-02, -2.514369189739227295e-01, -4.359832778573036194e-02, -1.852578520774841309e-01, 4.693385586142539978e-02, -3.438087105751037598e-01, -9.738498181104660034e-02, 1.683363318443298340e-01, 7.526867836713790894e-02, 1.769449561834335327e-01, 1.772719025611877441e-01, -3.423422947525978088e-02, 1.499355733394622803e-01, -1.377317905426025391e-01, -2.094969302415847778e-01, -6.127283573150634766e-01, 3.781396746635437012e-01, 3.901829719543457031e-01, -8.359315991401672363e-02, 3.152117878198623657e-02, 1.312240660190582275e-01, 3.882605433464050293e-01, 2.184422910213470459e-01, 9.724286198616027832e-02, 4.208936393260955811e-01, -3.264123499393463135e-01, -2.693341970443725586e-01, -3.909511864185333252e-01, -2.264865487813949585e-01, -3.202073872089385986e-01, -1.628742963075637817e-01, -3.581614047288894653e-02, 3.637387156486511230e-01, 1.858329921960830688e-01, -2.914021164178848267e-02, -4.657791256904602051e-01, 2.916888296604156494e-01, 3.725127875804901123e-01, -2.372660040855407715e-01, 3.386467695236206055e-03, 4.154096841812133789e-01, 3.300432115793228149e-02, 4.500397443771362305e-01, -8.159277588129043579e-02, 3.399033248424530029e-01, 2.449786067008972168e-01, 2.352412417531013489e-02, -1.464306265115737915e-01, -1.264452338218688965e-01, 3.112861812114715576e-01, -1.518262922763824463e-01, 1.009387709200382233e-02, 4.910853505134582520e-01, 1.436241269111633301e-01, 1.158903315663337708e-01, -2.323697209358215332e-01, 2.475174367427825928e-01, 1.836448311805725098e-01, -2.483685612678527832e-01, -1.122094392776489258e-01, -2.311335057020187378e-01, 8.428957313299179077e-02, -2.437865734100341797e-01, 1.330728679895401001e-01, 4.235569238662719727e-01, 3.334836065769195557e-01, -3.437012135982513428e-01, 3.443647548556327820e-02, 1.879549026489257812e-01, 2.003718763589859009e-01, -5.355946719646453857e-02, 2.848529219627380371e-01, 7.176562398672103882e-02, 5.487144365906715393e-02, -8.103788644075393677e-02, 2.707686424255371094e-01, 1.170023232698440552e-01],
                        [5.897930860519409180e-01, -2.359832376241683960e-01, -2.541170120239257812e-01, 3.116633975878357887e-03, -8.485706895589828491e-02, -2.679976820945739746e-01, -7.506710290908813477e-02, -3.002136647701263428e-01, 5.151664093136787415e-02, 1.658532172441482544e-01, 2.607674896717071533e-01, 3.825633525848388672e-01, 4.373287260532379150e-01, -9.301974624395370483e-02, -2.656879723072052002e-01, -9.716296195983886719e-02, -4.809605777263641357e-01, 1.187827885150909424e-01, 1.367550343275070190e-01, 4.712080582976341248e-02, -2.369651645421981812e-01, -5.233234763145446777e-01, -1.631881482899188995e-02, 6.127280369400978088e-02, -7.433295845985412598e-01, -1.189892366528511047e-01, -7.886531949043273926e-01, -4.810884296894073486e-01, 1.031494066119194031e-01, -3.237242400646209717e-01, 8.144375681877136230e-01, -3.977453410625457764e-01, -5.031558275222778320e-01, -7.972458004951477051e-01, -6.324826478958129883e-01, 3.232096731662750244e-01, -3.841938972473144531e-01, -1.118668839335441589e-01, -1.324360221624374390e-01, 2.069724537432193756e-02, -1.430956125259399414e-01, -3.701156005263328552e-02, 6.116622313857078552e-02, 1.633288562297821045e-01, -1.117428839206695557e-01, 2.523421943187713623e-01, -1.046407103538513184e+00, -3.725237548351287842e-01, 1.560198068618774414e-01, -2.999159693717956543e-01, 1.988387256860733032e-01, 2.343344241380691528e-01, -3.702580928802490234e-01, 3.173359930515289307e-01, 8.442859649658203125e-01, 6.977686285972595215e-02, 3.273648396134376526e-02, 9.948327392339706421e-02, -3.114135563373565674e-01, 5.051773190498352051e-01, 3.092621685937047005e-03, 3.801366388797760010e-01, 4.582764208316802979e-02, 6.333882454782724380e-03, -1.429482013918459415e-03, -1.356867849826812744e-01, -7.611397653818130493e-02, -2.584426701068878174e-01, -8.022130131721496582e-01, 5.508586764335632324e-01, -9.124376624822616577e-02, -2.178205102682113647e-01, -7.881092429161071777e-01, -5.118381381034851074e-01, 4.667254686355590820e-01, 5.527477860450744629e-01, -3.712476193904876709e-01, -1.864536553621292114e-01, 3.585702180862426758e-01, -1.958634704351425171e-01, 1.804253458976745605e-01, -4.254889488220214844e-01, -9.681382030248641968e-02, -5.536802113056182861e-02, 5.248928666114807129e-01, 2.448114603757858276e-01, 1.934617571532726288e-02, -2.963794171810150146e-01, -1.277786940336227417e-01, -3.053497672080993652e-01, 4.534939825534820557e-01, 7.469131797552108765e-02, -7.061695307493209839e-02, 2.624299228191375732e-01, 3.738394975662231445e-01, 1.430637687444686890e-01, 1.278782845474779606e-03, -4.177604615688323975e-01, -2.401406615972518921e-01, -2.509351670742034912e-01, 3.484380245208740234e-01, 3.114404380321502686e-01, 8.087333291769027710e-02, -5.764053463935852051e-01, 5.408530831336975098e-01, -1.802206784486770630e-02, -1.295981407165527344e-01, -7.399659603834152222e-02, 3.936978280544281006e-01, 6.488384604454040527e-01, -2.029980346560478210e-02, -5.665556192398071289e-01, 2.967598140239715576e-01, 5.200023055076599121e-01, 2.153875231742858887e-01, 1.036966815590858459e-01, 6.199258565902709961e-02, 1.896279491484165192e-02, -1.526914983987808228e-01, -1.064266324043273926e+00, 7.614958882331848145e-01, 2.073440998792648315e-01, 4.471894502639770508e-01, 1.449393630027770996e-01, 6.580228805541992188e-01, -9.440919756889343262e-02, -2.331637144088745117e-01, 4.215706884860992432e-01, 1.195765361189842224e-01, -3.257109224796295166e-01, 1.642551422119140625e-01, -4.950869977474212646e-01, -1.951612085103988647e-01, -5.618322491645812988e-01, -1.493323594331741333e-01, 6.109409928321838379e-01, -1.789793968200683594e-01, -1.805550791323184967e-02, -5.964048504829406738e-01, 4.918630048632621765e-02, 1.534783542156219482e-01, -4.282945692539215088e-01, 7.329528927803039551e-01, -3.529110848903656006e-01, -1.115965247154235840e-01, 6.127825006842613220e-02, -2.970442771911621094e-01, 4.396659433841705322e-01, -9.660355001688003540e-02, 6.557945609092712402e-01, -6.140334606170654297e-01, 2.576654590666294098e-02, 4.382747411727905273e-01, 1.733195222914218903e-02, -4.000226557254791260e-01, -8.178367465734481812e-02, -3.712696731090545654e-01, 8.230254054069519043e-02, -1.310442984104156494e-01, -5.326109528541564941e-01, -2.992832958698272705e-01, 6.993656754493713379e-01, -4.398765042424201965e-02, -1.570302397012710571e-01, 9.794142097234725952e-02, -3.017469309270381927e-02, -1.000270023941993713e-01, 1.999655365943908691e-01, -4.818853437900543213e-01, 1.794915199279785156e-01, 5.656598806381225586e-01, -1.195481792092323303e-01, -6.963727474212646484e-01, 5.259707570075988770e-02, -5.496182013303041458e-03, 1.673939079046249390e-01, -3.169286251068115234e-01, -9.747564792633056641e-02, 3.319365680217742920e-01, 4.719963073730468750e-01, 1.265397518873214722e-01, 1.913098245859146118e-01, 4.294907152652740479e-01, 5.529124140739440918e-01, 3.146334886550903320e-01, -3.143309056758880615e-01, -4.150866568088531494e-01, 3.289771378040313721e-01, 3.570270836353302002e-01, -1.920964270830154419e-01, 2.223942279815673828e-01, -4.871788918972015381e-01,
                        3.409155905246734619e-01, -2.213744521141052246e-01, -1.266756504774093628e-01, 2.112082839012145996e-01, -3.134789764881134033e-01, 8.468940854072570801e-01, 2.011267691850662231e-01, -4.259879291057586670e-01, 5.131570100784301758e-01, -1.235141396522521973e+00, 7.697179317474365234e-01, -1.741422861814498901e-01, -2.181101031601428986e-02, -3.568635880947113037e-02, -1.105949044227600098e+00, -5.720656514167785645e-01, 5.585205927491188049e-02, 1.246149912476539612e-01, -4.506591260433197021e-01, 6.429003924131393433e-02, -1.603386402130126953e-01, 3.993293344974517822e-01, -1.032289788126945496e-01, -2.025506459176540375e-02, -1.801048517227172852e-01, 6.234775856137275696e-02, -2.188893593847751617e-02, -1.579539030790328979e-01, 2.831696271896362305e-01, 2.385283075273036957e-02, 3.098120354115962982e-02, -7.853289693593978882e-02, 2.989652752876281738e-01, -6.237306818366050720e-02, 5.498673915863037109e-01, 1.786233633756637573e-01, 2.116472125053405762e-01, 4.448334872722625732e-01, 4.890750348567962646e-02, -1.623808294534683228e-01, -2.266986370086669922e-01, 1.887196898460388184e-01, 7.943605631589889526e-02, 1.359758377075195312e-01, -1.848446130752563477e-01, 1.113551020622253418e+00, 8.280951976776123047e-01, -3.120273053646087646e-01, 9.506001323461532593e-02, 5.096073076128959656e-02, 3.880488872528076172e-01, 2.500048279762268066e-01, 5.584861040115356445e-01, 3.108873963356018066e-01, -5.318577215075492859e-02, -7.675344496965408325e-02, 1.528232544660568237e-01, 9.189971536397933960e-02, -1.429156679660081863e-02, 6.657540202140808105e-01, -3.346028923988342285e-02, -4.470352232456207275e-01, 8.006748557090759277e-01, -4.799281060695648193e-01, 1.747820973396301270e-01, -3.056386411190032959e-01, 5.536521077156066895e-01, 4.238092899322509766e-01, 4.867432117462158203e-01, -4.967796802520751953e-01, -4.519478082656860352e-01, -9.556307792663574219e-01, -2.070993185043334961e-01, -2.260573953390121460e-01, -9.991831146180629730e-03, 9.879770278930664062e-01, 5.880774259567260742e-01, 8.305435627698898315e-02, -5.578136444091796875e-01, 2.113683819770812988e-01, -3.607222735881805420e-01, 5.266848206520080566e-01, 3.398357927799224854e-01, -1.575620472431182861e-01, 4.237726330757141113e-03, -5.354529991745948792e-02, -5.777673125267028809e-01, 5.595101118087768555e-01, -5.747127532958984375e-02, 1.683770418167114258e-01, 3.794685304164886475e-01, -2.577640712261199951e-01, 8.421474695205688477e-02, -1.522992998361587524e-01, -3.280776739120483398e-02, 1.008386313915252686e-01, -4.185833036899566650e-01, -4.449901580810546875e-01, -2.930993139743804932e-01, 6.144204735755920410e-01, 8.548156172037124634e-02, -6.349527090787887573e-02, -6.152555346488952637e-01, 7.954411506652832031e-01, -2.405838221311569214e-01, 2.063887566328048706e-01, -5.125258564949035645e-01, 6.312013268470764160e-01, 3.674431145191192627e-01, -4.400988817214965820e-01, 4.691397249698638916e-01, 2.308772653341293335e-01, -1.373799592256546021e-01, 2.169690132141113281e-01, 4.004325866699218750e-01, -2.490628510713577271e-02, -1.139675617218017578e+00, 2.653856761753559113e-02, -3.273023366928100586e-01, 9.984182566404342651e-02, 5.725682899355888367e-02, -8.472219109535217285e-01, 6.451983749866485596e-02, 4.569802582263946533e-01, 6.356298327445983887e-01, 4.518562257289886475e-01, -2.751905620098114014e-01, 2.134616822004318237e-01, 1.737425774335861206e-01, 4.282205998897552490e-01, -6.584535241127014160e-01, 4.000254571437835693e-01, -2.035577781498432159e-02, -6.730788350105285645e-01, -1.026923418045043945e+00, 1.687724739313125610e-01, -9.248701483011245728e-02, -7.997762560844421387e-01, 3.809339106082916260e-01, 5.171234011650085449e-01, 4.200939834117889404e-02, -4.867553710937500000e-02, -1.877224296331405640e-01, 1.633953303098678589e-01, -2.197492122650146484e-01, 2.193927615880966187e-01, 3.676529601216316223e-02, -2.975027859210968018e-01, -3.740966320037841797e-01, -5.209508538246154785e-01, -4.131466150283813477e-01, -4.894771575927734375e-01, -8.189660906791687012e-01, 8.531483262777328491e-02, 3.457696437835693359e-01, 1.250599324703216553e-01, 2.494525909423828125e-01, -2.525470256805419922e-01, -3.156108409166336060e-02, 2.757310569286346436e-01, -6.085720658302307129e-01, 3.357000648975372314e-01, 2.291317582130432129e-01, 6.607081294059753418e-01, -3.021580278873443604e-01, -5.315314233303070068e-02, 2.224752455949783325e-01, 6.138700246810913086e-02, 3.355513811111450195e-01, -8.485180139541625977e-02, 8.764573931694030762e-02, 1.087202429771423340e-01, -4.038927853107452393e-01, -1.494978666305541992e-01, 1.945850253105163574e-01, -8.106063008308410645e-01, 7.973096370697021484e-01, -4.116255939006805420e-01, 1.364154089242219925e-02, 2.347293049097061157e-01, -9.732253104448318481e-02, -2.904408872127532959e-01, 3.843209147453308105e-02, -7.090485841035842896e-02, -1.740449666976928711e-01, -4.485938549041748047e-01, -3.186723887920379639e-01, 4.165604412555694580e-01, -5.431653931736946106e-02, 1.403615623712539673e-01, 1.055916428565979004e+00, 5.301813483238220215e-01]
                        ]
    }
