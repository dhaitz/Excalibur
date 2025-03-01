
#pragma once

#include "Excalibur/Compile/interface/ZJetTypes.h"

#include "KappaTools/RootTools/interface/Matching.h"

/** Producer for reco jet gen jet matches
 *
 *  Possible config tags:
 *  - DeltaRMatchingRecoJetGenJet (default provided)
 */

class RecoJetGenJetMatchingProducer : public ZJetProducerBase
{
  public:
    std::string GetProducerId() const override;

    RecoJetGenJetMatchingProducer() : ZJetProducerBase() {}

    void Init(ZJetSettings const& settings) override;

    void Produce(ZJetEvent const& event,
                 ZJetProduct& product,
                 ZJetSettings const& settings) const override;

  private:
    std::vector<int> MatchCollection(ZJetEvent const& event,
                                     ZJetProduct& product,
                                     ZJetSettings const& settings,
                                     std::string const& corrLevel,
                                     double const deltaR) const;
};
