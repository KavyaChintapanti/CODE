
class Per:
    def perrec(results):
        if results == 'aphids':
            reco = 'pyrethrin and Neem Oil'
        elif results == 'armyworm':
            reco = 'Pyrethroid pesticides'
        elif results == 'beetle':
            reco = 'Talstar Pro 96 Ounce (3/4 Gallon)'
        elif results == 'bollworm':
            reco = 'GAIAGEN Heli Lure'
        elif results == 'grasshopper':
            reco = 'Malathion'
        elif results == 'mites':
            reco = 'Central Coast Garden Green Cleaner 8 Ounce - all Natural Pesticide - Exterminates Broad Mites and Russet Mites - Soybean Oil Based'
        elif results == 'mosquito':
            reco = 'Wondercide Outdoor Pest Control Spray'
        elif results == 'sawfly':
            reco = 'Spinosad'
        else:
            reco = 'Cypermethrin'
        return reco
        