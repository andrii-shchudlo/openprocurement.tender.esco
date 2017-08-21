NPV_PERIODS = 21
NBU_DISCOUNT_RATE = 0.125
ANNUAL_COSTS_REDUCTION = [
    92.47, 250, 250, 250, 250, 250, 250, 250,
    250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250
]

CONTRACT_DURATION_CHANGING = {
    'yearlyPaymentsPercentage': 0.70,
    'annualCostsReduction': ANNUAL_COSTS_REDUCTION,
    'announcementDate': '2017-08-18',
    'contractDuration': [
        {'years': 15, 'days': 0},
        {'years': 0, 'days': 1},
        {'years': 3, 'days': 11},
        {'years': 3, 'days': 12},
        {'years': 3, 'days': 13},
        {'years': 3, 'days': 14},
        {'years': 3, 'days': 15},
        {'years': 4, 'days': 15},
        {'years': 5, 'days': 15},
        {'years': 6, 'days': 15},
        {'years': 7, 'days': 15},
    ],
    'NBUdiscountRate': NBU_DISCOUNT_RATE,
    'calculated': [
        {
            'amountContract': 2625,
            'amountPerformance': 650.193823614962
        },
        {
            'amountContract': 0.479452054794521,
            'amountPerformance': 1810.49202999925
        },
        {
            'amountContract': 530.27397260274,
            'amountPerformance': 1390.67464457115
        },
        {
            'amountContract': 530.753424657534,
            'amountPerformance': 1390.35279031706
        },
        {
            'amountContract': 531.232876712329,
            'amountPerformance': 1390.03093606298
        },
        {
            'amountContract': 531.712328767123,
            'amountPerformance': 1389.70908180889
        },
        {
            'amountContract': 532.191780821918,
            'amountPerformance': 1389.38722755481
        },
        {
            'amountContract': 707.191780821918,
            'amountPerformance': 1280.67201284187
        },
        {
            'amountContract': 882.191780821918,
            'amountPerformance': 1184.03626643037
        },
        {
            'amountContract': 1057.191780821920,
            'amountPerformance': 1098.13782517570
        },
        {
            'amountContract': 1232.191780821920,
            'amountPerformance': 1021.78365517155
        },
    ]
}
