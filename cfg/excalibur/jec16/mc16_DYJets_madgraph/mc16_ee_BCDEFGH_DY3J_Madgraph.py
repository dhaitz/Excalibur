import configtools
import os
import sys

# -- import common information
sys.path.append(os.path.dirname(__file__))
from common import JEC_BASE, JEC_VERSION, JER, SE_PATH_PREFIXES

RUN='BCDEFGH'
CH='ee'
JEC='{}_{}'.format(JEC_BASE, JEC_VERSION)


def config():
    cfg = configtools.getConfig('mc', 2016, CH, JEC=JEC, JER=JER)
    cfg["InputFiles"].set_input(
        #bmspath="{}/tberger/Skimming/MC-Summer16_metfix/Zll_DY3JetsToLL_M-50_madgraphMLM-pythia8_RunIISummer16/*.root".format(SE_PATH_PREFIXES['srm_desy_dcache']),
        path="{}/dsavoiu/Skimming/ZJet_DY3JetsToLL_Summer16-madgraphMLM_asymptotic_2016_TrancheIV_v6-v1_egmSSbackport/*.root".format(SE_PATH_PREFIXES['xrootd_gridka_nrg']),
    )

    cfg = configtools.expand(cfg, ['basiccuts','finalcuts'], ['None', 'L1', 'L1L2L3'])

    cfg['PileupWeightFile'] = os.path.join(configtools.getPath() , 'data/pileup/PUWeights_'+RUN+'_13TeV_23Sep2016ReReco_DYJetsToLL_M-50_amcatnloFXFX-pythia8_RunIISummer16.root')
    cfg['NumberGeneratedEvents'] = 5856110
    cfg['GeneratorWeight'] = 1.0
    cfg['CrossSection'] = 101.8*1.23 # for: 3Jet_madgraphMLM

    return cfg
